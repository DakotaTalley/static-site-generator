import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("p", "This is a paragraph")
        node2 = LeafNode("a", "This is a link", {"href": "www.google.com"})
        node3 = LeafNode(None, "This node has no tag")
        self.assertEqual(node.to_html(), "<p>This is a paragraph</p>")
        self.assertEqual(node2.to_html(), "<a href=\"www.google.com\">This is a link</a>")
        self.assertEqual(node3.to_html(), "This node has no tag")

if __name__ == "__main__":
    unittest.main()