from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("tag is required for parent node")
        if self.children is None:
            raise ValueError("children is required for parent node")
        html_string = f"<{self.tag}"
        if self.props is not None:
            html_string += self.props_to_html()
        html_string += ">"
        for item in self.children:
            html_string += item.to_html()
        html_string += f"</{self.tag}>"
        return html_string
