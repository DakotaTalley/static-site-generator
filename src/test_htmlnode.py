import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "This is a paragraph")
        node2 = HTMLNode("p", "This is a paragraph")
        self.assertEqual(node, node2)

    def test_props_to_html_single_prop(self):
        node = HTMLNode("a", "This is a link", None, {"href": "www.google.com"})
        self.assertEqual(node.props_to_html(), " href=\"www.google.com\"")

    def test_props_to_html_multiple_props(self):
        node = HTMLNode("p", "This is a paragraph with a class and id", None, {"class": "class_name", "id": "id_name"})
        self.assertEqual(node.props_to_html(), " class=\"class_name\" id=\"id_name\"")

if __name__ == "__main__":
    unittest.main()