from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            return ValueError("all leaf nodes must have a value")
        if self.tag == None:
            return self.value
        html_node = f"<{self.tag}"
        if self.props is not None:
            for key in self.props.keys():
                html_node += f" {key}=\"{self.props[key]}\""
        html_node += f">{self.value}</{self.tag}>"
        return html_node