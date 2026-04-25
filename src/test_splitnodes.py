import unittest
from textnode import TextNode, TextType
from splitnodes import split_nodes_delimiter, split_nodes_link
from text_to_textnode import extract_markdown_images, extract_markdown_links

class TestSplitNodes(unittest.TestCase):

    def test_split_nodes_delimiter_with_single_node(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_delimiter_with_single_node_with_code(self):
        node = TextNode("code block", TextType.CODE)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        expected_nodes = [
            TextNode("code block", TextType.CODE),
        ]
        self.assertEqual(new_nodes, expected_nodes)        

    def test_split_nodes_delimiter_with_multiple_nodes(self):
        node0 = TextNode("This is text with a `code block` word", TextType.TEXT)
        node1 = TextNode("This is a code block", TextType.CODE)
        node2 = TextNode("This is text with a `code block` word", TextType.TEXT)
        nodes = [node0, node1, node2]
        new_nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
        expected_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
            TextNode("This is a code block", TextType.CODE),
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, expected_nodes)     

    def test_split_nodes_delimiter_with_invalid_markdown(self):
        node = TextNode("This is text with a `code block` `word", TextType.TEXT)  
        with self.assertRaisesRegex(SyntaxError, "invalid markdown syntax"): split_nodes_delimiter([node], "`", TextType.CODE)  
    
    def test_split_nodes_delimiter_with_invalid_text(self):
        node = TextNode("This is text with a `", TextType.TEXT)  
        with self.assertRaisesRegex(SyntaxError, "invalid markdown syntax"): split_nodes_delimiter([node], "`", TextType.CODE) 

    def test_split_nodes_link(self):
        old_node = TextNode("This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)", TextType.TEXT)
        new_nodes = split_nodes_link([old_node], extract_markdown_links, TextType.LINK)
        expected_nodes = [
            TextNode("This is text with a link ", TextType.TEXT),
            TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
            TextNode(" and ", TextType.TEXT),
            TextNode(
                "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
        )]
        self.assertEqual(new_nodes, expected_nodes)

    def test_split_nodes_images(self):
        old_node = TextNode("This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg) testtest", TextType.TEXT)
        new_nodes = split_nodes_link([old_node], extract_markdown_images, TextType.IMAGE, "!")
        expected_nodes = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("rick roll", TextType.IMAGE, "https://i.imgur.com/aKaOqIh.gif"),
            TextNode(" and ", TextType.TEXT),
            TextNode(
                "obi wan", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"
        ),
            TextNode(" testtest", TextType.TEXT)]
        self.assertEqual(new_nodes, expected_nodes)
        
def test_split_images(self):
    node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,
    )
    new_nodes = split_nodes_link([node], extract_markdown_images, TextType.IMAGE, "!")
    self.assertListEqual(
        [
            TextNode("This is text with an ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.TEXT),
            TextNode(
                "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
            ),
        ],
        new_nodes,
    )

if __name__ == "__main__":
    unittest.main()