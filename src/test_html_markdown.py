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
    
    def test_paragraphs_with_newlines(self):
        md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_heading_one(self):
        md = "# This is a heading"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>This is a heading</h1></div>",
        )

    def test_heading_two(self):
        md = "## This is a heading"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h2>This is a heading</h2></div>",
        )

    def test_heading_six(self):
        md = "###### This is a heading"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h6>This is a heading</h6></div>",
        )
    
    def test_heading_seven(self):
        md = "####### This is a heading"
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>####### This is a heading</p></div>",
        )

    def test_codeblock(self):
        md = """
```
This is text that _should_ remain
the **same** even with inline stuff
```
"""

        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><pre><code>This is text that _should_ remain\nthe **same** even with inline stuff\n</code></pre></div>",
        )

    def test_blockquote(self):
        md = """
> This is a blockquote
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote</blockquote></div>",
        )

    def test_blockquote_multiline(self):
        md = """
> This is a blockquote
> 
> And has multiple lines
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote\n\nAnd has multiple lines</blockquote></div>",
        )

    def test_unordered_list(self):
        md = """
- List Item 1
- List Item 2
- List Item 3
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>List Item 1</li><li>List Item 2</li><li>List Item 3</li></ul></div>",
        )

    def test_unordered_list_nav(self):
        md = """
- [Home](/home)
- [About](/about)
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            '<div><ul><li><a href="/home">Home</a></li><li><a href="/about">About</a></li></ul></div>',
        )

    def test_ordered_list(self):
        md = """
1. List Item 1
2. List Item 2
3. List Item 3
"""
        node = markdown_to_html_node(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ol><li>List Item 1</li><li>List Item 2</li><li>List Item 3</li></ol></div>",
        )