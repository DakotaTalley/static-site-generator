import unittest

from textnode import TextNode, TextType
from inline_markdown import extract_markdown_images, extract_markdown_links, split_nodes_delimiter


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

    def test_extract_markdown_images_none(self):
        text = "This is text"
        self.assertEqual(extract_markdown_images(text), [])

    def test_extract_markdown_images_single(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
        self.assertEqual(extract_markdown_images(text), [
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
        ])

    def test_extract_markdown_images_double(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual(extract_markdown_images(text), [
            ("rick roll", "https://i.imgur.com/aKaOqIh.gif"),
            ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")
        ])

    def test_extract_markdown_links_none(self):
        text = "This is text"
        self.assertEqual(extract_markdown_links(text), [])

    def test_extract_markdown_links_single(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev)"
        self.assertEqual(extract_markdown_links(text), [
            ("to boot dev", "https://www.boot.dev"),
        ])

    def test_extract_markdown_links_double(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        self.assertEqual(extract_markdown_links(text), [
            ("to boot dev", "https://www.boot.dev"),
            ("to youtube", "https://www.youtube.com/@bootdotdev")
        ])

    def test_extract_markdown_links_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        self.assertEqual(extract_markdown_links(text), [])


if __name__ == "__main__":
    unittest.main()