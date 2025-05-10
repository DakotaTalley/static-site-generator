import re
from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "Paragraph"
    HEADING = "Heading"
    CODE = "Code"
    QUOTE = "Quote"
    UNORDERED_LIST = "Unordered List"
    ORDERED_LIST = "Ordered List"

def markdown_to_blocks(markdown):
    blocks = []
    split_markdown = markdown.split("\n\n")
    for block in split_markdown:
        block = block.strip()
        if block != "":
            blocks.append(block)
    return blocks

def block_to_block_type(markdown_block):
    if len(re.findall(r"^(#{1,6} )", markdown_block)) > 0:
        return BlockType.HEADING
    if markdown_block[0:3] == "```" and markdown_block[-3:] == "```":
        return BlockType.CODE
    if markdown_block[0] == ">":
        return BlockType.QUOTE
    if markdown_block[0:2] == "- ":
        return BlockType.UNORDERED_LIST
    if markdown_block[0:3] == "1. ":
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH