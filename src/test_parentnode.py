from parentnode import ParentNode
from leafnode import LeafNode
import unittest

class TestParentNode(unittest.TestCase):

    def test_to_html(self):
        node = ParentNode("p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],)
        expected = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), expected)

    def test_to_html_with_a(self):
        node = ParentNode("a",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],{"href": "https://www.google.com"})
        expected = '<a href="https://www.google.com"><b>Bold text</b>Normal text<i>italic text</i>Normal text</a>'
        self.assertEqual(node.to_html(), expected)

    def test_to_html_with_props(self):
        node = ParentNode("p",
    [
        LeafNode("a", "link", {"href": "https://www.google.com"}),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],)
        expected = '<p><a href="https://www.google.com">link</a>Normal text<i>italic text</i>Normal text</p>'
        self.assertEqual(node.to_html(), expected)        

    def test_to_html_nested_parents(self):
        nested_node = ParentNode("p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],)
        node = ParentNode("p",
    [
        nested_node,
        LeafNode("b", "Bold text"),
    ],)
        expected = "<p><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p><b>Bold text</b></p>"
        self.assertEqual(node.to_html(), expected)

    def test_to_html_no_children(self):
        node = ParentNode("p",
    None)
        with self.assertRaisesRegex(ValueError, "missing children"): node.to_html()  

    def test_to_html_no_tag(self):
        node = ParentNode(None,
        [
        LeafNode("a", "link", {"href": "https://www.google.com"}),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ])
        with self.assertRaisesRegex(ValueError, "missing tag"): node.to_html()  

if __name__ == "__main__":
    unittest.main()