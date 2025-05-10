import unittest

from block_markdown import BlockType, block_to_block_type, markdown_to_blocks


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


class TestBlockToBlockType(unittest.TestCase):
    def test_heading_one(self):
        md = "# This is a heading"
        self.assertEqual(block_to_block_type(md), BlockType.HEADING)

    def test_heading_two(self):
        md = "## This is a heading"
        self.assertEqual(block_to_block_type(md), BlockType.HEADING)

    def test_heading_six(self):
        md = "###### This is a heading"
        self.assertEqual(block_to_block_type(md), BlockType.HEADING)

    def test_paragraph_seven_hashes(self):
        md = "####### This is a paragraph"
        self.assertEqual(block_to_block_type(md), BlockType.PARAGRAPH)

    def test_code(self):
        md = "```This is a code block```"
        self.assertEqual(block_to_block_type(md), BlockType.CODE)

    def test_invalid_code(self):
        md = "``This is a paragraph``"
        self.assertEqual(block_to_block_type(md), BlockType.PARAGRAPH)
    
    def test_quote(self):
        md = ">This is a blockquote"
        self.assertEqual(block_to_block_type(md), BlockType.QUOTE)

    def test_ul(self):
        md = "- This is list item 1"
        self.assertEqual(block_to_block_type(md), BlockType.UNORDERED_LIST)

    def test_ol(self):
        md = "1. This is list item 1"
        self.assertEqual(block_to_block_type(md), BlockType.ORDERED_LIST)



if __name__ == "__main__":
    unittest.main()