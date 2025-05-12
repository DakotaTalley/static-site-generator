import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("p", "This is a paragraph")
        node2 = HTMLNode("p", "This is a paragraph")
        self.assertEqual(node, node2)

    def test_to_html(self):
        node = HTMLNode("p", "This is a paragraph")
        with self.assertRaises(NotImplementedError):
            node.to_html()

    def test_props_to_html_single_prop(self):
        node = HTMLNode("a", "This is a link", None, {"href": "www.google.com"})
        self.assertEqual(node.props_to_html(), " href=\"www.google.com\"")

    def test_props_to_html_multiple_props(self):
        node = HTMLNode("p", "This is a paragraph with a class and id", None, {"class": "class_name", "id": "id_name"})
        self.assertEqual(node.props_to_html(), " class=\"class_name\" id=\"id_name\"")

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode("a", "This is a link", {"href": "www.google.com"})
        node2 = LeafNode("a", "This is a link", {"href": "www.google.com"})
        self.assertEqual(node, node2)

    def test_no_tag(self):
        node = LeafNode(None, "This is a link", {"href": "www.google.com"})
        self.assertEqual(node.to_html(), "This is a link")

    def test_no_value(self):
        node = LeafNode("a", None, {"href": "www.google.com"})
        with self.assertRaises(ValueError):
            node.to_html()

    def test_to_html(self):
        node = LeafNode("a", "This is a link", {"href": "www.google.com"})
        self.assertEqual(node.to_html(), "<a href=\"www.google.com\">This is a link</a>")
    
    def test_to_html_no_props(self):
        node = LeafNode("p", "This is a paragraph")
        self.assertEqual(node.to_html(), "<p>This is a paragraph</p>")

    def test_to_html_no_value(self):
        node = LeafNode(None, "This node has no tag")
        self.assertEqual(node.to_html(), "This node has no tag")

class TestParentNode(unittest.TestCase):
    def test_eq(self):
        child_node = LeafNode("span", "child")
        node = ParentNode("p", [child_node])
        node2 = ParentNode("p", [child_node])
        self.assertEqual(node, node2)
    
    def test_no_tag(self):
        child_node = LeafNode("span", "child")
        node = ParentNode(None, [child_node])
        with self.assertRaises(ValueError):
            node.to_html()

    def test_no_children(self):
        node = ParentNode("p", None)
        with self.assertRaises(ValueError):
            node.to_html()
    
    def test_to_html_single_child(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_multiple_children(self):
        child_node = LeafNode("span", "child1")
        child_node2 = LeafNode("span", "child2")
        parent_node = ParentNode("div", [child_node, child_node2])
        self.assertEqual(parent_node.to_html(), "<div><span>child1</span><span>child2</span></div>")
    
    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "bold text")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span><b>bold text</b></span></div>")

if __name__ == "__main__":
    unittest.main()