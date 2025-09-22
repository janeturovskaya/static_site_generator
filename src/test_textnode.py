import unittest
from textnode import TextType, TextNode

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



if __name__ == "__main__":
	unittest.main()