import unittest

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


class RenderTest(unittest.TestCase):
    def test_groups_by_project_in_order_of_newest_merge(self):
        prs = [
            pr("vllm-project/aibrix", 2896, "Run tests in CI"),
            pr("hyperledger/fabric", 5598, "Reject bad policies"),
            pr("vllm-project/aibrix", 2878, "Stop empty patches"),
        ]
        self.assertEqual(
            ur.render(prs, 0),
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

    def test_open_count_line(self):
        out = ur.render([pr("a/x", 1, "one")], 15)
        self.assertTrue(out.endswith(f"\n\nPlus [15 more in review]({ur.OPEN_SEARCH_URL})."))
        self.assertIn("is%3Aopen", ur.OPEN_SEARCH_URL)

    def test_no_open_count_line_when_none_open(self):
        self.assertNotIn("in review", ur.render([pr("a/x", 1, "one")], 0))


class EscapeTest(unittest.TestCase):
    def test_escapes_markdown_outside_code_spans(self):
        self.assertEqual(
            ur.escape("[fix]: keep `a_b` and <nil> *x*"),
            r"\[fix\]: keep `a_b` and \<nil\> \*x\*",
        )

    def test_unbalanced_backtick_is_escaped(self):
        self.assertEqual(ur.escape("fix `a_b"), r"fix \`a\_b")


def release(tag, published_at):
    return {
        "tag_name": tag,
        "html_url": f"https://github.com/hmdsefi/gograph/releases/tag/{tag}",
        "published_at": published_at,
    }


def milestone(number, title, due_on, description):
    return {
        "title": title,
        "html_url": f"https://github.com/hmdsefi/gograph/milestone/{number}",
        "due_on": due_on,
        "description": description,
    }


class GographStatusTest(unittest.TestCase):
    def test_release_and_earliest_upcoming_milestone(self):
        milestones = [
            milestone(1, "v0.9.0", "2026-10-27T00:00:00Z", "Dependency graph toolkit: section 4."),
            milestone(3, "v0.11.0", "2026-12-08T00:00:00Z", "Routes and bounded search. Freeze."),
            milestone(2, "v0.10.0", "2026-11-17T00:00:00Z", "Foundations and performance: section 3."),
        ]
        # The v0.9.0 milestone is still open right after the release, so it isn't "next".
        self.assertEqual(
            ur.gograph_status(release("v0.9.0", "2026-10-27T11:31:00Z"), milestones),
            "[v0.9.0](https://github.com/hmdsefi/gograph/releases/tag/v0.9.0) shipped on October 27."
            " Next is [v0.10.0](https://github.com/hmdsefi/gograph/milestone/2), due November 17:"
            " Foundations and performance.",
        )

    def test_no_open_milestones(self):
        self.assertEqual(
            ur.gograph_status(release("v0.8.2", "2026-10-02T11:31:00Z"), []),
            "[v0.8.2](https://github.com/hmdsefi/gograph/releases/tag/v0.8.2) shipped on October 2.",
        )

    def test_milestone_without_due_date_or_description(self):
        status = ur.gograph_status(
            release("v0.8.2", "2026-10-02T11:31:00Z"), [milestone(1, "v0.9.0", None, "")]
        )
        self.assertTrue(status.endswith(" Next is [v0.9.0](https://github.com/hmdsefi/gograph/milestone/1)."))


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
