import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode("a", "This is a paragraph")
        node2 = HTMLNode("a", "This is a paragraph")
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()