class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def __eq__(self, text_node):
        return (
            self.tag == text_node.tag and
            self.value == text_node.value and
            self.children == text_node.children and
            self.props == text_node.props
        )

    def props_to_html(self):
        if self.props is None:
            return ""
        html_string = ""
        for prop in self.props:
            html_string += f" {prop}=\"{self.props[prop]}\""
        return html_string

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("all leaf nodes must have a value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
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
    
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"