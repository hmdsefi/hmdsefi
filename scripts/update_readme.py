#!/usr/bin/env python3
"""Rewrites the generated parts of README.md: the latest release and next milestone
of each project in PROJECTS, and the list of recent upstream pull requests.

Set GITHUB_TOKEN to raise the API rate limit. The pull request queries are limited
to public repositories, so a token with access to private repositories is safe to use.
"""

import json
import os
import re
import sys
import urllib.parse
import urllib.request
from datetime import datetime
from pathlib import Path

USER = "hmdsefi"
LIMIT = 10
README = Path(__file__).resolve().parent.parent / "README.md"

# Projects whose release line is generated, and whether their milestone descriptions
# start with a theme ("Dependency graph toolkit: ...") to show after the due date.
PROJECTS = {"faultline": False, "gograph": True}

MERGED_QUERY = f"is:pr is:merged is:public author:{USER} -user:{USER}"
OPEN_QUERY = f"is:pr is:open is:public author:{USER} -user:{USER}"

ESCAPED = "\\*_[]<>"


def get(path, token, **params):
    url = "https://api.github.com" + path
    if params:
        url += "?" + urllib.parse.urlencode(params)
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        },
    )
    if token:
        request.add_header("Authorization", f"Bearer {token}")
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def search(query, token, per_page):
    return get("/search/issues", token, q=query, sort="created", order="desc", per_page=per_page)


def search_url(query, excluded):
    """Links to a GitHub search for query, leaving out the excluded repositories."""
    q = " ".join([query] + [f"-repo:{repo}" for repo in sorted(excluded)])
    return "https://github.com/search?" + urllib.parse.urlencode({"q": q, "type": "pullrequests"})


def repo_of(item):
    return item["repository_url"].removeprefix("https://api.github.com/repos/")


def own_forks(repos):
    """Returns the names of the repositories that are forks of one of USER's repositories."""
    return {
        repo["full_name"]
        for repo in repos
        if repo.get("fork") and repo["source"]["owner"]["login"].lower() == USER.lower()
    }


def without_repos(items, repos):
    excluded = {repo.lower() for repo in repos}
    return [item for item in items if repo_of(item).lower() not in excluded]


def day(timestamp):
    date = datetime.fromisoformat(timestamp)
    return f"{date:%B} {date.day}"


def theme(description):
    """Returns the theme a milestone description starts with, such as "Dependency graph toolkit"."""
    return escape(re.split(r":|\.(?:\s|$)", description or "", maxsplit=1)[0].strip())


def latest_release(releases):
    """Returns the newest published release of the main module, or None.

    Tags with a slash, such as harness/etcdraft/v0.1.0, belong to nested modules.
    """
    published = [
        r for r in releases if not r["draft"] and not r["prerelease"] and "/" not in r["tag_name"]
    ]
    return max(published, key=lambda r: r["published_at"], default=None)


def release_status(release, milestones, with_theme):
    """Describes the latest release and the earliest open milestone after it."""
    parts = []
    upcoming = milestones
    if release:
        tag = release["tag_name"]
        parts.append(f"[{tag}]({release['html_url']}) shipped on {day(release['published_at'])}.")
        # A milestone titled after the release, like "v0.1.1 (hardening)", can stay open after it ships.
        upcoming = [m for m in milestones if m["title"].split()[0] != tag]
    if upcoming:
        milestone = min(upcoming, key=lambda m: (m["due_on"] is None, m["due_on"] or ""))
        next_up = f"Next is [{escape(milestone['title'])}]({milestone['html_url']})"
        if milestone["due_on"]:
            next_up += f", due {day(milestone['due_on'])}"
        if with_theme and (summary := theme(milestone["description"])):
            next_up += f": {summary}"
        parts.append(next_up + ".")
    return " ".join(parts)


def latest_merged(items, limit):
    """Returns the most recently merged pull requests, newest first."""
    merged = [item for item in items if item["pull_request"].get("merged_at")]
    merged.sort(key=lambda item: item["pull_request"]["merged_at"], reverse=True)
    return merged[:limit]


def escape(title):
    """Escapes Markdown in a pull request title, leaving `code spans` as they are."""
    if title.count("`") % 2:
        return "".join("\\" + c if c in ESCAPED + "`" else c for c in title)
    parts = title.split("`")
    for i in range(0, len(parts), 2):
        parts[i] = "".join("\\" + c if c in ESCAPED else c for c in parts[i])
    return "`".join(parts)


def render(prs):
    """Lists the pull requests grouped by project, in the order they're given."""
    groups = {}
    for pr in prs:
        groups.setdefault(repo_of(pr), []).append(pr)

    lines = []
    for repo, items in groups.items():
        owner = repo.split("/")[0]
        lines.append(
            f'- <img src="https://github.com/{owner}.png?size=32" width="16" height="16" alt=""> **{repo}**'
        )
        for pr in items:
            lines.append(f"  - {escape(pr['title'])} ([#{pr['number']}]({pr['html_url']}))")
    return "\n".join(lines)


def footer(open_count, forks):
    """Links to the open and the merged pull requests, leaving out the forks."""
    paragraphs = []
    if open_count:
        paragraphs.append(f"Plus [{open_count} more in review]({search_url(OPEN_QUERY, forks)}).")
    paragraphs.append(
        f"[All my merged pull requests to other projects]({search_url(MERGED_QUERY, forks)})"
    )
    return "\n\n".join(paragraphs)


def replace_section(readme, name, content):
    """Replaces the text between <!-- name:start --> and <!-- name:end --> with content."""
    start_marker, end_marker = f"<!-- {name}:start -->", f"<!-- {name}:end -->"
    start = readme.find(start_marker)
    end = readme.find(end_marker)
    if start == -1 or end == -1 or end < start:
        raise ValueError(f"README.md must contain {start_marker} followed by {end_marker}")
    return readme[: start + len(start_marker)] + content + readme[end:]


def main():
    token = os.environ.get("GITHUB_TOKEN")
    merged = search(MERGED_QUERY, token, 100)["items"]
    open_prs = search(OPEN_QUERY, token, 100)["items"]
    repos = sorted({repo_of(item) for item in merged + open_prs})
    forks = own_forks([get(f"/repos/{repo}", token) for repo in repos])

    prs = latest_merged(without_repos(merged, forks), LIMIT)
    if not prs:
        sys.exit("No merged pull requests found, leaving README.md unchanged")
    open_count = len(without_repos(open_prs, forks))

    readme = README.read_text()
    updated = readme
    for project, with_theme in PROJECTS.items():
        releases = get(f"/repos/{USER}/{project}/releases", token, per_page=30)
        milestones = get(f"/repos/{USER}/{project}/milestones", token, state="open", per_page=100)
        status = release_status(latest_release(releases), milestones, with_theme)
        updated = replace_section(updated, project, status)
    block = render(prs) + "\n\n" + footer(open_count, forks)
    updated = replace_section(updated, "recent-prs", "\n" + block + "\n")
    if updated == readme:
        print("README.md is up to date")
        return
    README.write_text(updated)
    print("README.md updated")


if __name__ == "__main__":
    main()
