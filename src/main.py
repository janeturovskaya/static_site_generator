from htmlnode import LeafNode
from textnode import TextNode, TextType



def main():
	node = TextNode("some text", TextType.LINK, "https://www.boot.dev")
	print(node)

if __name__ == "__main__":
	main()