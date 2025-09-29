from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
	TEXT = "plain text"
	BOLD = "bold text"
	ITALIC = "italic text"
	CODE = "code text"
	LINK = "link"
	IMAGE = "image"

class TextNode:
	def __init__(self, text, text_type, url=None):
		self.text = text
		self.text_type = text_type
		self.url = url

	def __eq__(self, other):
		return (
				self.text_type == other.text_type
				and self.text == other.text
				and self.url == other.url
		)

	def __repr__(self):
		return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node):
	match text_node.text_type:
		case TextType.TEXT:
			return LeafNode(None, text_node.text)
		case TextType.BOLD:
			return LeafNode('b', text_node.text)
		case TextType.ITALIC:
			return LeafNode('i', text_node.text)
		case TextType.CODE:
			return LeafNode('code', text_node.text)
		case TextType.LINK:
			return LeafNode('a', text_node.text, props={'href': text_node.url})
		case TextType.IMAGE:
			return LeafNode('img', '', {'src': text_node.url, 'alt': text_node.text})
		case _:
			raise Exception('Unknown TextNode type')

from textnode import TextNode, TextType
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
	new_nodes = []
	for node in old_nodes:
		if node.text_type != TextType.TEXT:
			new_nodes.append(node)
		else:
			splitted = node.text.split(delimiter)
			for i in range(len(splitted)):
				if i % 2 == 0:
					if splitted[i] != '':
						new_nodes.append(TextNode(splitted[i], TextType.TEXT))
				else:
					new_nodes.append(TextNode(splitted[i], text_type))

	return new_nodes

def extract_markdown_images(text):
	matches = re.findall(r"!\[([^\[\]]*)]\(([^()]*)\)", text)
	return matches

def extract_markdown_links(text):
	matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
	return matches

def split_nodes_link(old_nodes):
	new_nodes = []
	for node in old_nodes:
		matches = extract_markdown_links(node.text)
		if not matches:
			new_nodes.append(node)
		else:
			original_text = node.text
			for u in range(len(matches)):
				text, url = matches[u][0], matches[u][1]
				delimiter = f'[{text}]({url})'
				splitted = original_text.split(delimiter, 1)

				if splitted[0] != '':
					new_nodes.append(TextNode(splitted[0], TextType.TEXT))
				new_nodes.append(TextNode(text, TextType.LINK, url))

				if u == len(matches) - 1: #if no more links in the text
					if splitted[1]: #if second part contains text
						new_nodes.append(TextNode(splitted[1], TextType.TEXT))

				else:
					original_text = splitted[1]
	return new_nodes

def split_nodes_images(old_nodes):
	new_nodes = []
	for node in old_nodes:
		matches = extract_markdown_images(node.text)
		if not matches:
			new_nodes.append(node)
		else:
			original_text = node.text
			for u in range(len(matches)):
				text, url = matches[u][0], matches[u][1]
				delimiter = f'![{text}]({url})'
				splitted = original_text.split(delimiter, 1)

				if splitted[0] != '':
					new_nodes.append(TextNode(splitted[0], TextType.TEXT))
				new_nodes.append(TextNode(text, TextType.IMAGE, url))

				if u == len(matches) - 1: #if no more links in the text
					if splitted[1]: #if second part contains text
						new_nodes.append(TextNode(splitted[1], TextType.TEXT))

				else:
					original_text = splitted[1]
	return new_nodes










