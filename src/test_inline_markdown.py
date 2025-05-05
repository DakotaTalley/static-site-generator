import unittest

from textnode import TextNode, TextType
from inline_markdown import split_nodes_delimiter


class TestSplitNodesDelimiter(unittest.TestCase):
    def test_without_delimiter(self):
        node = TextNode("This is a paragraph", TextType.TEXT)
        self.assertEqual(split_nodes_delimiter(
            [node], "**", TextType.BOLD), 
            [TextNode("This is a paragraph", TextType.TEXT)]
        )

    def test_with_bold_delimiter(self):
        node = TextNode("This is a **paragraph** with bold", TextType.TEXT)
        self.assertEqual(split_nodes_delimiter(
            [node], "**", TextType.BOLD), 
            [
                TextNode("This is a ", TextType.TEXT),
                TextNode("paragraph",TextType.BOLD),
                TextNode(" with bold", TextType.TEXT)
            ]
        )

    def test_with_italic_delimiter(self):
        node = TextNode("This is a _paragraph_ with italics", TextType.TEXT)
        self.assertEqual(split_nodes_delimiter(
            [node], "_", TextType.ITALIC), 
            [
                TextNode("This is a ", TextType.TEXT),
                TextNode("paragraph",TextType.ITALIC),
                TextNode(" with italics", TextType.TEXT)
            ]
        )

    def test_with_code_delimiter(self):
        node = TextNode("This is `code` text", TextType.TEXT)
        self.assertEqual(split_nodes_delimiter(
            [node], "`", TextType.CODE), 
            [
                TextNode("This is ", TextType.TEXT),
                TextNode("code",TextType.CODE),
                TextNode(" text", TextType.TEXT)
            ]
        )

    def test_invalid_markdown_closing_tag(self):
        node = TextNode("This is a **paragraph with bold", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter(node)

    def test_with_and_without_delimiter(self):
        node = TextNode("This is a paragraph", TextType.TEXT)
        node2 = TextNode("This is a **paragraph** with bold", TextType.TEXT)
        self.assertEqual(split_nodes_delimiter(
            [node, node2], "**", TextType.BOLD), 
            [
                TextNode("This is a paragraph", TextType.TEXT),
                TextNode("This is a ", TextType.TEXT),
                TextNode("paragraph",TextType.BOLD),
                TextNode(" with bold", TextType.TEXT)
            ]
        )

    def test_multiple_same_delimeters(self):
        node = TextNode("This is a **paragraph** with **bold** text", TextType.TEXT)
        split_node = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(split_node, 
            [
                TextNode("This is a ", TextType.TEXT),
                TextNode("paragraph",TextType.BOLD),
                TextNode(" with ", TextType.TEXT),
                TextNode("bold", TextType.BOLD),
                TextNode(" text", TextType.TEXT)
            ]
        )
    
    def test_multiple_different_delimeters(self):
        node = TextNode("This is a bold **paragraph** and _italic_ text", TextType.TEXT)
        split_node = split_nodes_delimiter([node], "**", TextType.BOLD)
        split_node = split_nodes_delimiter(split_node, "_", TextType.ITALIC)
        self.assertEqual(split_node, 
            [
                TextNode("This is a bold ", TextType.TEXT),
                TextNode("paragraph",TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" text", TextType.TEXT)
            ]
        )


if __name__ == "__main__":
    unittest.main()