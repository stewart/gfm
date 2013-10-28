import unittest
from gfm import *

class TestGitHubFlavoredMarkdown(unittest.TestCase):
    def test_does_not_touch_single_underscores_inside_words(self):
        self.assertEqual("foo_bar", gfm("foo_bar"))

    def test_does_not_touch_underscores_in_code_blocks(self):
        self.assertEqual("    foo_bar_baz", gfm("    foo_bar_baz"))

    def test_does_not_touch_underscores_in_pre_blocks(self):
        self.assertEqual(
            "\n\n<pre>\nfoo_bar_baz\n</pre>",
            gfm("<pre>\nfoo_bar_baz\n</pre>")
        )

    def test_does_not_treat_pre_blocks_with_pre_text_differently(self):
        a = "\n\n<pre>\nthis is `a\\_test` and this\\_too\n</pre>"
        b = "hmm<pre>\nthis is `a\\_test` and this\\_too\n</pre>"
        self.assertEqual(gfm(a)[2:-1], gfm(b)[3:-1])

    def test_does_escape_two_or_more_underscores_inside_words(self):
        self.assertEqual("foo\\_bar\\_baz", gfm("foo_bar_baz"))

    def test_does_turn_newlines_into_br_tags_in_simple_cases(self):
        self.assertEqual("foo  \nbar", gfm("foo\nbar"))

    def test_does_convert_newlines_in_all_groups(self):
        self.assertEqual(
            "apple  \npear  \norange\n\nruby  \npython  \nerlang",
            gfm("apple\npear\norange\n\nruby\npython\nerlang")
        )

    def test_does_convert_newlines_in_long_groups(self):
        self.assertEqual(
            "apple  \npear  \norange  \nbanana\n\nruby  \npython  \nerlang",
            gfm("apple\npear\norange\nbanana\n\nruby\npython\nerlang")
        )

    def test_does_not_convert_newlines_in_lists(self):
        self.assertEqual("# foo\n# bar", gfm("# foo\n# bar"))
        self.assertEqual("* foo\n* bar", gfm("* foo\n* bar"))

if __name__ == "__main__":
    unittest.main()
