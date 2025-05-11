from block_markdown import BlockType, block_to_block_type, markdown_to_blocks
from inline_markdown import text_to_textnodes
from parentnode import ParentNode
from textnode import text_node_to_html_node


def markdown_to_html_node(markdown):
    block_nodes = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        match block_type:
            case BlockType.PARAGRAPH:
                nodes = text_to_children(block)
                block_nodes.append(ParentNode("p", nodes))
    return ParentNode("div", block_nodes)

def text_to_children(text):
    html_nodes = []
    text_nodes = text_to_textnodes(text)
    for node in text_nodes:
        html_nodes.append(text_node_to_html_node(node))
    return html_nodes