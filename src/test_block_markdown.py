import unittest

from block_markdown import markdown_to_blocks


class TestMarkdownToBlocks(unittest.TestCase):
    def test_empty(self):
        md = ""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [])

    def test_single_block(self):
        md = """
This is a **bolded** paragraph
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, ["This is a **bolded** paragraph"])

    def test_multiple_blocks(self):
        md = """
# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and _italic_ words inside of it."
            ])
        
    def test_multiple_blocks_line_breaks(self):
        md = """
# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

- This is the first list item in a list block
- This is a list item
- This is another list item
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and _italic_ words inside of it.",
                "- This is the first list item in a list block\n- This is a list item\n- This is another list item"
            ])
        
    def test_extra_whitespace(self):
        md = """
    This paragraph has additional whitespace at the end and beginning    
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [
                "This paragraph has additional whitespace at the end and beginning"
            ])
        
    def test_extra_newlines(self):
        md = """
This paragraph has additional newlines at the end




"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(blocks, [
                "This paragraph has additional newlines at the end"
            ])


if __name__ == "__main__":
    unittest.main()