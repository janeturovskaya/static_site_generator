import unittest
from textnode import TextType, TextNode, text_node_to_html_node
from htmlnode import LeafNode
from textnode import split_nodes_delimiter, split_nodes_link, extract_markdown_images, extract_markdown_links, split_nodes_images

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

class TestSplitNodes(unittest.TestCase):
	def test_split_code1(self):
		node = TextNode("This is text with a `code block` word", TextType.TEXT)
		new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
		self.assertEqual([
			TextNode("This is text with a ", TextType.TEXT),
			TextNode("code block", TextType.CODE),
			TextNode(" word", TextType.TEXT)
		],
			new_nodes)

	def test_split_code2(self):
		node = TextNode("`code block` `code block`", TextType.TEXT)
		new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
		self.assertEqual([
			TextNode("code block", TextType.CODE),
			TextNode(" ", TextType.TEXT),
			TextNode("code block", TextType.CODE)
		],
		new_nodes)

	def test_split_bold(self):
		node = TextNode("**bold text** text", TextType.TEXT)
		new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
		self.assertEqual([
			TextNode("bold text", TextType.BOLD),
			TextNode(" text", TextType.TEXT)
		],
		new_nodes)

	def test_split_italic(self):
		node = TextNode("_italic text_ text", TextType.TEXT)
		new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
		self.assertEqual([
			TextNode("italic text", TextType.ITALIC),
			TextNode(" text", TextType.TEXT)
		],
		new_nodes)

	def test_split_link_one(self):
		node = TextNode(
			"This is text with a link [to boot dev](https://www.boot.dev)",
			TextType.TEXT,
		)
		new_nodes = split_nodes_link([node])
		self.assertEqual([
			TextNode('This is text with a link ', TextType.TEXT),
			TextNode('to boot dev', TextType.LINK, 'https://www.boot.dev')
		],
		new_nodes)

	def test_split_link_one_in_middle(self):
		node = TextNode(
			"This is text with a link [to boot dev](https://www.boot.dev) more text",
			TextType.TEXT,
		)
		new_nodes = split_nodes_link([node])
		self.assertEqual([
			TextNode('This is text with a link ', TextType.TEXT),
			TextNode('to boot dev', TextType.LINK, 'https://www.boot.dev'),
			TextNode(' more text', TextType.TEXT)
		],
		new_nodes)

	def test_split_link_two(self):
		node = TextNode(
			"This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
			TextType.TEXT,
		)
		new_nodes = split_nodes_link([node])
		self.assertEqual([
			TextNode('This is text with a link ', TextType.TEXT),
			TextNode('to boot dev', TextType.LINK, 'https://www.boot.dev'),
			TextNode(' and ', TextType.TEXT),
			TextNode('to youtube', TextType.LINK, 'https://www.youtube.com/@bootdotdev')
		],
		new_nodes)

	def test_split_images(self):
		node = TextNode(
			"This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
			TextType.TEXT,
		)
		new_nodes = split_nodes_images([node])
		self.assertListEqual(
			[
				TextNode("This is text with an ", TextType.TEXT),
				TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
				TextNode(" and another ", TextType.TEXT),
				TextNode(
					"second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
				),
			],
			new_nodes,
		)




if __name__ == "__main__":
	unittest.main()