from textnode import TextNode, TextType

def main():
    text_node = TextNode("This is a url node", TextType.LINK, "www.google.com")
    print(text_node)

main()