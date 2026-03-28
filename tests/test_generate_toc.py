import unittest
from generate_toc import create_slug, generate_toc_from_lines

class TestTOCGenerator(unittest.TestCase):
    def test_create_slug(self):
        self.assertEqual(create_slug("Hello World"), "hello-world")
        self.assertEqual(create_slug("This is a Test!"), "this-is-a-test")
        self.assertEqual(create_slug("API v2.0"), "api-v20")

    def test_generate_toc(self):
        lines = [
            "# Main Title\n",
            "Some text here.\n",
            "## Subtitle\n",
            "More text.\n",
            "```python\n",
            "## In Code Block\n",
            "```\n",
            "### Deep Level\n"
        ]
        toc = generate_toc_from_lines(lines, max_level=3)
        self.assertEqual(len(toc), 3)
        self.assertEqual(toc[0], "- [Main Title](#main-title)")
        self.assertEqual(toc[1], "  - [Subtitle](#subtitle)")
        self.assertEqual(toc[2], "    - [Deep Level](#deep-level)")

if __name__ == '__main__':
    unittest.main()
