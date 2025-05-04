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
        html_string = ""
        for key in self.props.keys():
            html_string += f" {key}=\"{self.props[key]}\""
        return html_string

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"