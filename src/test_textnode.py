import unittest
from textnode import TextType, TextNode, text_node_to_html_node
from htmlnode import LeafNode

class TestTextNode(unittest.TestCase):
	def test_eq(self):
		node1 = TextNode("this is a bold text", TextType.BOLD)
		node2 = TextNode("this is a bold text", TextType.BOLD)
		node3 = TextNode("this is a link", TextType.LINK, "boot.com")
		node4 = TextNode("this is a link", TextType.LINK)
		node5 = TextNode("this is another bold text", TextType.BOLD)
		self.assertEqual(node1, node2)
		self.assertNotEqual(node1, node3)
		self.assertIsInstance(node1, TextNode)
		self.assertNotEqual(node3, node4)
		self.assertNotEqual(node1, node5)


	def test_repr(self):
		node1 = TextNode("this is a link", TextType.LINK, "boot.com")
		self.assertEqual(repr(node1),"TextNode(this is a link, link, boot.com)")

class TestTextNodeToHTML(unittest.TestCase):
	def test_text(self):
		text_node = TextNode('This is a text node', TextType.TEXT)
		html_node = text_node_to_html_node(text_node)
		self.assertEqual(
			'This is a text node', html_node.value
		)
		self.assertEqual(None, html_node.tag)

	def test_link(self):
		link_node = TextNode('This is a link node', TextType.LINK, "https://www.google.com")
		html_node = text_node_to_html_node(link_node)
		self.assertEqual(
			'This is a link node', html_node.value
		)
		self.assertEqual(
			'a', html_node.tag
		)
		self.assertEqual(
			{
			    "href": "https://www.google.com"
		    }, html_node.props
		)

	def test_leaf(self):
		bold_text_node = TextNode('This is bold text node', TextType.BOLD)
		html_node = text_node_to_html_node(bold_text_node)
		self.assertIsInstance(html_node, LeafNode)
		self.assertEqual(html_node.tag, 'b')
		self.assertEqual(html_node.value, 'This is bold text node')



if __name__ == "__main__":
	unittest.main()