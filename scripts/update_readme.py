#!/usr/bin/env python3
"""Rewrites the generated parts of README.md: the latest gograph release and next
milestone, and the list of recent upstream pull requests.

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
GOGRAPH = f"{USER}/gograph"
LIMIT = 10
README = Path(__file__).resolve().parent.parent / "README.md"

MERGED_QUERY = f"is:pr is:merged is:public author:{USER} -user:{USER}"
OPEN_QUERY = f"is:pr is:open is:public author:{USER} -user:{USER}"
OPEN_SEARCH_URL = "https://github.com/search?" + urllib.parse.urlencode(
    {"q": OPEN_QUERY, "type": "pullrequests"}
)

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


def day(timestamp):
    date = datetime.fromisoformat(timestamp)
    return f"{date:%B} {date.day}"


def theme(description):
    """Returns the theme a milestone description starts with, such as "Dependency graph toolkit"."""
    return escape(re.split(r":|\.(?:\s|$)", description or "", maxsplit=1)[0].strip())


def gograph_status(release, milestones):
    """Describes the latest release and the earliest open milestone after it."""
    status = f"[{release['tag_name']}]({release['html_url']}) shipped on {day(release['published_at'])}."
    upcoming = [m for m in milestones if m["title"] != release["tag_name"]]
    if not upcoming:
        return status
    upcoming.sort(key=lambda m: (m["due_on"] is None, m["due_on"] or ""))
    milestone = upcoming[0]
    status += f" Next is [{milestone['title']}]({milestone['html_url']})"
    if milestone["due_on"]:
        status += f", due {day(milestone['due_on'])}"
    if summary := theme(milestone["description"]):
        status += f": {summary}"
    return status + "."


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


def render(prs, open_count):
    """Lists the pull requests grouped by project, in the order they're given."""
    groups = {}
    for pr in prs:
        repo = pr["repository_url"].removeprefix("https://api.github.com/repos/")
        groups.setdefault(repo, []).append(pr)

    lines = []
    for repo, items in groups.items():
        owner = repo.split("/")[0]
        lines.append(
            f'- <img src="https://github.com/{owner}.png?size=32" width="16" height="16" alt=""> **{repo}**'
        )
        for pr in items:
            lines.append(f"  - {escape(pr['title'])} ([#{pr['number']}]({pr['html_url']}))")
    if open_count:
        lines += ["", f"Plus [{open_count} more in review]({OPEN_SEARCH_URL})."]
    return "\n".join(lines)


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
    prs = latest_merged(search(MERGED_QUERY, token, 50)["items"], LIMIT)
    if not prs:
        sys.exit("No merged pull requests found, leaving README.md unchanged")
    open_count = search(OPEN_QUERY, token, 1)["total_count"]
    release = get(f"/repos/{GOGRAPH}/releases/latest", token)
    milestones = get(f"/repos/{GOGRAPH}/milestones", token, state="open", per_page=100)

    readme = README.read_text()
    updated = replace_section(readme, "gograph", gograph_status(release, milestones))
    updated = replace_section(updated, "recent-prs", "\n" + render(prs, open_count) + "\n")
    if updated == readme:
        print("README.md is up to date")
        return
    README.write_text(updated)
    print("README.md updated")


if __name__ == "__main__":
    main()
