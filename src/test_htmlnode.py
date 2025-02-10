from htmlnode import HTMLNode
import unittest

class TestHTMLNode(unittest.TestCase):

    def test_repr(self):
        node = HTMLNode()
        expected = f"HTMLNode None, None, None, None"
        self.assertEqual(str(node), expected)

    def test_repr_with_values(self):
        props = {"href":"https://www.google.com"}
        node = HTMLNode(tag = "a", value = "test", props = props)
        expected = f"HTMLNode a, test, None, {props}"
        self.assertEqual(str(node), expected)

    def test_props_to_html(self):
        props1 = {"href":"https://www.google.com"}
        node1 = HTMLNode(tag = "a", value = "test", props = props1)
        self.assertEqual(node1.props_to_html(), " href=\"https://www.google.com\"")

        props2 = {"href":"https://www.google.com", "target":"_blank"}
        node2 = HTMLNode(tag = "a", value = "test", props = props2)
        self.assertEqual(node2.props_to_html()," href=\"https://www.google.com\" target=\"_blank\"")

if __name__ == "__main__":
    unittest.main()