import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("a", "This is a link", {"href": "www.google.com"})
        node2 = LeafNode("a", "This is a link", {"href": "www.google.com"})
        self.assertEqual(node, node2)

    def test_to_html(self):
        node = LeafNode("a", "This is a link", {"href": "www.google.com"})
        self.assertEqual(node.to_html(), "<a href=\"www.google.com\">This is a link</a>")
    
    def test_to_html_no_props(self):
        node = LeafNode("p", "This is a paragraph")
        self.assertEqual(node.to_html(), "<p>This is a paragraph</p>")

    def test_to_html_no_value(self):
        node = LeafNode(None, "This node has no tag")
        self.assertEqual(node.to_html(), "This node has no tag")

if __name__ == "__main__":
    unittest.main()