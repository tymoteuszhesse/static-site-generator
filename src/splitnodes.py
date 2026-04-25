from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
        else:
            splitted = node.text.split(delimiter) 
            if len(splitted) %2 == 0:
                raise SyntaxError("invalid markdown syntax")              
            elif len(splitted) == 1:
                new_nodes.append(TextNode(splitted[0], TextType.TEXT))
            else:
                for index in range(0, len(splitted)): 
                    if index %2 != 0:
                        new_nodes.append(TextNode(splitted[index], text_type))
                    else:
                        new_nodes.append(TextNode(splitted[index], TextType.TEXT)) 
    return new_nodes
        
def split_nodes_link(old_nodes, regex_fun, text_type, special_char=""):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text != "":
            links = regex_fun(old_node.text)
            if len(links) == 0:
                new_nodes.append(old_node)
            else:
                for link in links:
                    text_before_index = old_node.text.index(f"{special_char}[{link[0]}")
                    index_to_remove = old_node.text.index(f"({link[1]})")
                    new_nodes.append(TextNode(old_node.text[:text_before_index], TextType.TEXT)),
                    new_nodes.append(TextNode(link[0], text_type, link[1])),
                    old_node.text = old_node.text[index_to_remove:].replace(f"({link[1]})", "")
                if old_node.text != "":
                    new_nodes.append(TextNode(old_node.text, TextType.TEXT))
    return new_nodes

