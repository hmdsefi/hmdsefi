import unittest
import urllib.parse

import update_readme as ur


def pr(repo, number, title, merged_at="2026-10-01T10:00:00Z"):
    return {
        "title": title,
        "number": number,
        "html_url": f"https://github.com/{repo}/pull/{number}",
        "repository_url": f"https://api.github.com/repos/{repo}",
        "pull_request": {"merged_at": merged_at},
    }


def logo(owner):
    return f'<img src="https://github.com/{owner}.png?size=32" width="16" height="16" alt="">'


class QueryTest(unittest.TestCase):
    def test_only_public_pull_requests_to_other_projects(self):
        # A token that can read private repos must not leak their titles into the README.
        for query in (ur.MERGED_QUERY, ur.OPEN_QUERY):
            terms = query.split()
            self.assertIn("is:public", terms)
            self.assertIn("-user:hmdsefi", terms)


class OwnForksTest(unittest.TestCase):
    def test_only_forks_of_my_repos(self):
        repos = [
            {"full_name": "ashhforrd/gograph", "fork": True, "source": {"full_name": "hmdsefi/gograph", "owner": {"login": "hmdsefi"}}},
            {"full_name": "someone/aibrix", "fork": True, "source": {"full_name": "vllm-project/aibrix", "owner": {"login": "vllm-project"}}},
            {"full_name": "vllm-project/aibrix", "fork": False},
        ]
        self.assertEqual(ur.own_forks(repos), {"ashhforrd/gograph"})

    def test_without_repos_ignores_case(self):
        items = [pr("Ashhforrd/gograph", 1, "fork"), pr("vllm-project/aibrix", 2, "upstream")]
        self.assertEqual(
            [p["number"] for p in ur.without_repos(items, {"ashhforrd/gograph"})], [2]
        )


class LatestMergedTest(unittest.TestCase):
    def test_newest_merge_first_and_limited(self):
        items = [
            pr("a/x", 1, "one", "2026-10-01T10:00:00Z"),
            pr("a/x", 2, "two", "2026-10-03T10:00:00Z"),
            pr("b/y", 3, "three", "2026-10-02T10:00:00Z"),
        ]
        self.assertEqual([p["number"] for p in ur.latest_merged(items, 2)], [2, 3])

    def test_skips_unmerged(self):
        items = [pr("a/x", 1, "one", None), pr("a/x", 2, "two")]
        self.assertEqual([p["number"] for p in ur.latest_merged(items, 10)], [2])

    def test_keeps_the_newest_of_the_most_recent_projects(self):
        items = [
            pr("a/x", 1, "a1", "2026-10-05T10:00:00Z"),
            pr("a/x", 2, "a2", "2026-10-04T10:00:00Z"),
            pr("a/x", 3, "a3", "2026-10-03T10:00:00Z"),
            pr("b/y", 4, "b1", "2026-10-02T10:00:00Z"),
            pr("c/z", 5, "c1", "2026-10-01T10:00:00Z"),
            pr("b/y", 6, "b2", "2026-09-30T10:00:00Z"),
        ]
        got = ur.latest_merged(items, 4, min_projects=3)
        self.assertEqual([p["number"] for p in got], [1, 2, 4, 5])

    def test_fewer_projects_than_the_minimum(self):
        items = [pr("a/x", n, str(n), f"2026-10-0{n}T10:00:00Z") for n in range(1, 5)]
        got = ur.latest_merged(items, 3, min_projects=4)
        self.assertEqual([p["number"] for p in got], [4, 3, 2])


class RenderTest(unittest.TestCase):
    def test_groups_by_project_in_order_of_newest_merge(self):
        prs = [
            pr("vllm-project/aibrix", 2896, "Run tests in CI"),
            pr("hyperledger/fabric", 5598, "Reject bad policies"),
            pr("vllm-project/aibrix", 2878, "Stop empty patches"),
        ]
        self.assertEqual(
            ur.render(prs),
            "\n".join(
                [
                    f"- {logo('vllm-project')} **vllm-project/aibrix**",
                    "  - Run tests in CI ([#2896](https://github.com/vllm-project/aibrix/pull/2896))",
                    "  - Stop empty patches ([#2878](https://github.com/vllm-project/aibrix/pull/2878))",
                    f"- {logo('hyperledger')} **hyperledger/fabric**",
                    "  - Reject bad policies ([#5598](https://github.com/hyperledger/fabric/pull/5598))",
                ]
            ),
        )


class FooterTest(unittest.TestCase):
    def test_open_count_and_merged_links_leave_out_forks(self):
        forks = {"ashhforrd/gograph"}
        self.assertEqual(
            ur.footer(15, forks),
            f"Plus [15 more in review]({ur.search_url(ur.OPEN_QUERY, forks)}).\n\n"
            f"[All my merged pull requests to other projects]({ur.search_url(ur.MERGED_QUERY, forks)})",
        )

    def test_no_open_count_line_when_none_open(self):
        self.assertNotIn("in review", ur.footer(0, set()))

    def test_search_url(self):
        url = ur.search_url(ur.OPEN_QUERY, {"b/gograph", "a/gograph"})
        query = urllib.parse.parse_qs(urllib.parse.urlparse(url).query)
        self.assertEqual(query["type"], ["pullrequests"])
        self.assertEqual(query["q"], [ur.OPEN_QUERY + " -repo:a/gograph -repo:b/gograph"])


class EscapeTest(unittest.TestCase):
    def test_escapes_markdown_outside_code_spans(self):
        self.assertEqual(
            ur.escape("[fix]: keep `a_b` and <nil> *x*"),
            r"\[fix\]: keep `a_b` and \<nil\> \*x\*",
        )

    def test_unbalanced_backtick_is_escaped(self):
        self.assertEqual(ur.escape("fix `a_b"), r"fix \`a\_b")


def release(tag, published_at, draft=False, prerelease=False):
    return {
        "tag_name": tag,
        "html_url": f"https://github.com/hmdsefi/gograph/releases/tag/{tag}",
        "published_at": published_at,
        "draft": draft,
        "prerelease": prerelease,
    }


def milestone(number, title, due_on, description):
    return {
        "title": title,
        "html_url": f"https://github.com/hmdsefi/gograph/milestone/{number}",
        "due_on": due_on,
        "description": description,
    }


class LatestReleaseTest(unittest.TestCase):
    def test_newest_release_of_the_main_module(self):
        releases = [
            release("harness/etcdraft/v0.1.1", "2026-10-20T10:00:00Z"),
            release("v0.2.0-rc.1", "2026-10-19T10:00:00Z", prerelease=True),
            release("v0.2.0", "2026-10-21T10:00:00Z", draft=True),
            release("v0.1.1", "2026-10-18T10:00:00Z"),
            release("v0.1.0", "2026-10-11T10:00:00Z"),
        ]
        self.assertEqual(ur.latest_release(releases)["tag_name"], "v0.1.1")

    def test_no_release(self):
        self.assertIsNone(ur.latest_release([release("harness/etcdraft/v0.1.0", "2026-10-11T10:00:00Z")]))


class ReleaseStatusTest(unittest.TestCase):
    def test_release_and_earliest_upcoming_milestone(self):
        milestones = [
            milestone(1, "v0.9.0", "2026-10-27T00:00:00Z", "Dependency graph toolkit: section 4."),
            milestone(3, "v0.11.0", "2026-12-08T00:00:00Z", "Routes and bounded search. Freeze."),
            milestone(2, "v0.10.0", "2026-11-17T00:00:00Z", "Foundations and performance: section 3."),
        ]
        # The v0.9.0 milestone is still open right after the release, so it isn't "next".
        self.assertEqual(
            ur.release_status(release("v0.9.0", "2026-10-27T11:31:00Z"), milestones, with_theme=True),
            "[v0.9.0](https://github.com/hmdsefi/gograph/releases/tag/v0.9.0) shipped on October 27."
            " Next is [v0.10.0](https://github.com/hmdsefi/gograph/milestone/2), due November 17:"
            " Foundations and performance.",
        )

    def test_without_theme_and_milestone_titled_after_the_release(self):
        milestones = [
            milestone(1, "Phase 2: Existing-code shims", None, "Goroutine mode, netsim."),
            milestone(2, "v0.1.1 (hardening and agent plugin)", "2026-10-19T00:00:00Z", "Right after v0.1.0: tests."),
        ]
        self.assertEqual(
            ur.release_status(release("v0.1.0", "2026-10-11T13:57:28Z"), milestones, with_theme=False),
            "[v0.1.0](https://github.com/hmdsefi/gograph/releases/tag/v0.1.0) shipped on October 11."
            " Next is [v0.1.1 (hardening and agent plugin)](https://github.com/hmdsefi/gograph/milestone/2),"
            " due October 19.",
        )
        self.assertTrue(
            ur.release_status(release("v0.1.1", "2026-10-19T10:00:00Z"), milestones, with_theme=False).endswith(
                " Next is [Phase 2: Existing-code shims](https://github.com/hmdsefi/gograph/milestone/1)."
            )
        )

    def test_no_open_milestones(self):
        self.assertEqual(
            ur.release_status(release("v0.8.2", "2026-10-02T11:31:00Z"), [], with_theme=True),
            "[v0.8.2](https://github.com/hmdsefi/gograph/releases/tag/v0.8.2) shipped on October 2.",
        )

    def test_milestone_without_due_date_or_description(self):
        status = ur.release_status(
            release("v0.8.2", "2026-10-02T11:31:00Z"), [milestone(1, "v0.9.0", None, "")], with_theme=True
        )
        self.assertTrue(status.endswith(" Next is [v0.9.0](https://github.com/hmdsefi/gograph/milestone/1)."))

    def test_no_release_yet(self):
        self.assertEqual(
            ur.release_status(None, [milestone(1, "v0.1.0", "2026-10-11T00:00:00Z", "")], with_theme=True),
            "Next is [v0.1.0](https://github.com/hmdsefi/gograph/milestone/1), due October 11.",
        )


class ThemeTest(unittest.TestCase):
    def test_theme(self):
        cases = {
            "Dependency graph toolkit: section 4 of the roadmap": "Dependency graph toolkit",
            "Routes and bounded search. Feature freeze Thu Dec 3": "Routes and bounded search",
            "Go 1.26 minimum: raise the floor": "Go 1.26 minimum",
            "[CI] and `go vet`: more": r"\[CI\] and `go vet`",
            "": "",
            None: "",
        }
        for description, want in cases.items():
            with self.subTest(description=description):
                self.assertEqual(ur.theme(description), want)


class ReplaceSectionTest(unittest.TestCase):
    def test_replaces_only_between_markers(self):
        readme = "intro <!-- x:start -->old<!-- x:end --> outro\n"
        self.assertEqual(
            ur.replace_section(readme, "x", "new"),
            "intro <!-- x:start -->new<!-- x:end --> outro\n",
        )

    def test_missing_or_misordered_markers(self):
        for readme in ("no markers", "<!-- x:start -->only start", "<!-- x:end --><!-- x:start -->"):
            with self.subTest(readme=readme), self.assertRaises(ValueError):
                ur.replace_section(readme, "x", "new")


if __name__ == "__main__":
    unittest.main()
