import unittest

from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

    def test_not_eq_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node2", TextType.BOLD)
        self.assertNotEqual(node, node2)   

    def test_not_eq_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, "https://www.google.com")
        self.assertNotEqual(node, node2)

    def test_text_type(self):
        text_type_bold = TextType.BOLD
        self.assertEqual(text_type_bold.value, "bold")

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        leaf_node = text_node_to_html_node(node)
        html = leaf_node.to_html()
        self.assertEqual(html, "This is a text node")

    def test_bold(self):
        node = TextNode("This is a text node", TextType.BOLD)
        leaf_node = text_node_to_html_node(node)
        html = leaf_node.to_html()
        self.assertEqual(html, "<b>This is a text node</b>")

    def test_italic(self):
        node = TextNode("This is a text node", TextType.ITALIC)
        leaf_node = text_node_to_html_node(node)
        html = leaf_node.to_html()
        self.assertEqual(html, "<i>This is a text node</i>")

    def test_code(self):
        node = TextNode("This is a text node", TextType.CODE)
        leaf_node = text_node_to_html_node(node)
        html = leaf_node.to_html()
        self.assertEqual(html, "<code>This is a text node</code>")

    def test_link(self):
        node = TextNode("This is a text node", TextType.LINK, "https://www.google.com")
        leaf_node = text_node_to_html_node(node)
        html = leaf_node.to_html()
        self.assertEqual(html, '<a href="https://www.google.com">This is a text node</a>')

    def test_image(self):
        node = TextNode("This is an image", TextType.IMAGE, "https://www.google.com")
        leaf_node = text_node_to_html_node(node)
        html = leaf_node.to_html()
        self.assertEqual(html, '<img src="https://www.google.com" alt="This is an image"></img>')    

if __name__ == "__main__":
    unittest.main()