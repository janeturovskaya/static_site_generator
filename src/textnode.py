from enum import Enum

class TextType(Enum):
	PLAIN = "plain text"
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
		return self == other

	def __repr__(self):
		return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

