from leafnode import LeafNode
import unittest

class TestLeafNode(unittest.TestCase):

    def test_repr(self):
        node = LeafNode("p", "some value")
        expected = f"HTMLNode p, some value, None, None"
        self.assertEqual(str(node), expected)

    def test_props_to_html(self):
        props = {"href":"https://www.google.com"}
        node = LeafNode(tag = "a", value = "leaf test", props = props)
        self.assertEqual(node.props_to_html(), " href=\"https://www.google.com\"")


    def test_to_html_a(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), "<a href=\"https://www.google.com\">Click me!</a>")    

    def test_to_html_p(self):
        node = LeafNode("p", "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text.</p>")     

if __name__ == "__main__":
    unittest.main()