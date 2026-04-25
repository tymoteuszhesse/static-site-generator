
from splitblocks import markdown_to_blocks, block_to_block_type, BlockType
from text_to_textnode import text_to_textnodes
from parentnode import ParentNode
from textnode import text_node_to_html_node, TextNode, TextType

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        block_type = block_to_block_type(block)
        match(block_type):
            case BlockType.HEADING:
                level = len(block) - len(block.lstrip("#"))
                text = block[level + 1:]
                children = text_to_children(text)
                nodes.append(ParentNode(f'h{level}', children))
            case BlockType.PARAGRAPH:
                lines = block.split("\n")
                text = " ".join(line.strip() for line in lines)
                children = text_to_children(text)
                nodes.append(ParentNode('p', children))
            case BlockType.QUOTE:
                lines = block.split("\n")
                text = " ".join(line.lstrip(">").strip() for line in lines)
                children = text_to_children(text)
                nodes.append(ParentNode('blockquote', children))
            case BlockType.CODE:
                lines = block.split("\n")
                text = "\n".join(lines[1:-1]) + "\n"
                raw_node = TextNode(text, TextType.TEXT)
                child = text_node_to_html_node(raw_node)
                code = ParentNode("code", [child])
                nodes.append(ParentNode('pre', [code]))
            case BlockType.UNORDERED_LIST:
                items = block.split("\n")
                li_nodes = [ParentNode("li", text_to_children(item[2:])) for item in items]
                nodes.append(ParentNode('ul', li_nodes))
            case BlockType.ORDERED_LIST:
                items = block.split("\n")
                li_nodes = [ParentNode("li", text_to_children(item.split(". ", 1)[1])) for item in items]
                nodes.append(ParentNode('ol', li_nodes))
    return ParentNode('div', nodes)
             
        
def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children     

def extract_title(markdown):
    lines = markdown.splitlines()
    for line in lines:
        if line.startswith("# "):
            return line.strip("#").strip()
    raise Exception("No h1 found")
        