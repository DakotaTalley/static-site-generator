import re
from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
        else:
            new_nodes.extend(recursive_delimiter_node_split(node, delimiter, text_type))
        
    return new_nodes

def recursive_delimiter_node_split(node, delimiter, text_type):
    if node.text.find(delimiter) == -1:
        return [node]
    split_node = node.text.split(delimiter, maxsplit=2)
    if len(split_node) < 3:
        raise Exception("invalid Markdown syntax")
    node_list = [
        TextNode(split_node[0], TextType.TEXT),
        TextNode(split_node[1], text_type)
    ]
    node_list.extend(recursive_delimiter_node_split(
            TextNode(split_node[2], TextType.TEXT),
            delimiter,
            text_type
        ))
    
    return node_list

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches