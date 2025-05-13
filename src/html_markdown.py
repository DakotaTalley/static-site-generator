from block_markdown import BlockType, block_to_block_type, markdown_to_blocks
from htmlnode import ParentNode
from inline_markdown import text_to_textnodes
from textnode import TextNode, TextType, text_node_to_html_node


def markdown_to_html_node(markdown):
    block_nodes = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.PARAGRAPH:
                block = block.replace("\n", " ")
                nodes = text_to_children(block)
                block_nodes.append(ParentNode("p", nodes))
            case BlockType.HEADING:
                heading_tuple = strip_and_count_heading(block)
                nodes = text_to_children(heading_tuple[1])
                block_nodes.append(ParentNode(heading_tuple[0], nodes))
            case BlockType.CODE:
                code_text = block.strip("```").lstrip("\n")
                node = TextNode(code_text, TextType.CODE)
                block_nodes.append(
                    ParentNode(
                        "pre", 
                        [text_node_to_html_node(node)]
                    )
                )
            case BlockType.QUOTE:
                block = block.replace("> ", "")
                nodes = text_to_children(block)
                block_nodes.append(ParentNode("blockquote", nodes))
            case BlockType.UNORDERED_LIST:
                li_nodes = []
                lines = block.split("\n")
                for line in lines:
                    line = line.lstrip("- ")
                    nodes = text_to_children(line)
                    li_nodes.append(ParentNode("li", nodes))
                block_nodes.append(ParentNode("ul", li_nodes))
            case BlockType.ORDERED_LIST:
                li_nodes = []
                lines = block.split("\n")
                for i in range(len(lines)):
                    line = lines[i].lstrip(f"{i + 1}. ")
                    nodes = text_to_children(line)
                    li_nodes.append(ParentNode("li", nodes))
                block_nodes.append(ParentNode("ol", li_nodes))  
    return ParentNode("div", block_nodes)

def text_to_children(text):
    html_nodes = []
    text_nodes = text_to_textnodes(text)
    for node in text_nodes:
        html_nodes.append(text_node_to_html_node(node))
    return html_nodes

def strip_and_count_heading(text):
    count = 0
    stripped_text = text
    while True:
        if stripped_text[0] == " ":
            return (f"h{count}", stripped_text[1:])
        stripped_text = stripped_text[1:]
        count += 1
