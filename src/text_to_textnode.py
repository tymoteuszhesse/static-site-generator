import re
from splitnodes import split_nodes_link, split_nodes_delimiter
from textnode import TextNode, TextType

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)  

def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)
    nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_link(nodes, extract_markdown_images, TextType.IMAGE, "!")
    nodes = split_nodes_link(nodes, extract_markdown_links, TextType.LINK)

    return nodes