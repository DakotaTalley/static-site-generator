import re
from textnode import TextNode, TextType

def text_to_textnodes(text):
    text_node = TextNode(text, TextType.TEXT)
    split_bold = split_nodes_delimiter([text_node], "**", TextType.BOLD)
    split_italic = split_nodes_delimiter(split_bold, "_", TextType.ITALIC)
    split_code = split_nodes_delimiter(split_italic, "`", TextType.CODE)
    split_link = split_nodes_link(split_code)
    split_image = split_nodes_image(split_link)

    return split_image

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
        else:
            new_nodes.extend(recursive_delimiter_node_split(node, delimiter, text_type))
        
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
        else:
            new_nodes.extend(recursive_image_link_node_split(node, extract_markdown_images, TextType.IMAGE))
        
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type is not TextType.TEXT:
            new_nodes.append(node)
        else:
            new_nodes.extend(recursive_image_link_node_split(node, extract_markdown_links, TextType.LINK))
        
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

def recursive_image_link_node_split(node, extractor, text_type):
    markdown_tags = extractor(node.text)
    if len(markdown_tags) == 0:
        return [node]
    
    if text_type == TextType.LINK:
        delimiter = f"[{markdown_tags[0][0]}]({markdown_tags[0][1]})"
    else:
        delimiter = f"![{markdown_tags[0][0]}]({markdown_tags[0][1]})"
    
    sections = node.text.split(delimiter, 1)
    text_node = TextNode(sections[0], TextType.TEXT)
    new_node = TextNode(markdown_tags[0][0], text_type, markdown_tags[0][1])
    node_list = [text_node, new_node]

    if sections[1] == "":
        return node_list
    
    node_list.extend(recursive_image_link_node_split(
            TextNode(sections[1], TextType.TEXT),
            extractor,
            text_type
        ))
    
    return node_list

def extract_markdown_images(text):
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches