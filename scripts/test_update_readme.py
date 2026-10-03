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


class ReplaceSectionTest(unittest.TestCase):
    def test_replaces_only_between_markers(self):
        readme = f"intro\n{ur.START}\nold\n{ur.END}\noutro\n"
        self.assertEqual(
            ur.replace_section(readme, "new"),
            f"intro\n{ur.START}\nnew\n{ur.END}\noutro\n",
        )

    def test_missing_or_misordered_markers(self):
        for readme in ("no markers", f"{ur.START}\nonly start", f"{ur.END}\n{ur.START}"):
            with self.subTest(readme=readme), self.assertRaises(ValueError):
                ur.replace_section(readme, "new")


if __name__ == "__main__":
    unittest.main()
