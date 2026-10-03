#!/usr/bin/env python3
"""Rewrites the list of recent upstream pull requests in README.md.

Set GITHUB_TOKEN to raise the search API rate limit. The queries are limited to
public repositories, so a token with access to private repositories is safe to use.
"""

import json
import os
import sys
import urllib.parse
import urllib.request
from pathlib import Path

USER = "hmdsefi"
LIMIT = 10
START = "<!-- recent-prs:start -->"
END = "<!-- recent-prs:end -->"
README = Path(__file__).resolve().parent.parent / "README.md"

MERGED_QUERY = f"is:pr is:merged is:public author:{USER} -user:{USER}"
OPEN_QUERY = f"is:pr is:open is:public author:{USER} -user:{USER}"
OPEN_SEARCH_URL = "https://github.com/search?" + urllib.parse.urlencode(
    {"q": OPEN_QUERY, "type": "pullrequests"}
)

ESCAPED = "\\*_[]<>"


def search(query, token, per_page):
    url = "https://api.github.com/search/issues?" + urllib.parse.urlencode(
        {"q": query, "sort": "created", "order": "desc", "per_page": per_page}
    )
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


def replace_section(readme, block):
    start = readme.find(START)
    end = readme.find(END)
    if start == -1 or end == -1 or end < start:
        raise ValueError(f"README.md must contain {START} followed by {END}")
    return readme[: start + len(START)] + "\n" + block + "\n" + readme[end:]


def main():
    token = os.environ.get("GITHUB_TOKEN")
    prs = latest_merged(search(MERGED_QUERY, token, 50)["items"], LIMIT)
    if not prs:
        sys.exit("No merged pull requests found, leaving README.md unchanged")
    open_count = search(OPEN_QUERY, token, 1)["total_count"]

    readme = README.read_text()
    updated = replace_section(readme, render(prs, open_count))
    if updated == readme:
        print("README.md is up to date")
        return
    README.write_text(updated)
    print("README.md updated")


if __name__ == "__main__":
    main()
