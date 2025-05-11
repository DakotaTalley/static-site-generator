import unittest

from html_markdown import markdown_to_html_node

class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_paragraph(self):
        md = "This is **bolded** paragraph"

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph</p></div>",
        )
    
    def test_paragraphs(self):
        md = """
This is **bolded** paragraph

This is a _second_ paragraph
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph</p><p>This is a <i>second</i> paragraph</p></div>",
        )