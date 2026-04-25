from htmlnode import HTMLNode
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        result = ""
        if self.tag is None:
            raise ValueError("missing tag")
        if self.children is None:
            raise ValueError("missing children")
        for child in self.children:
            result += child.to_html()
        result = f"<{self.tag}{self.props_to_html()}>{result}</{self.tag}>"
        return result