import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode
from src.textnode import TextNode


class TestHTMLNode(unittest.TestCase):

	def test_repr_a(self):
		html_node1 = HTMLNode(
			"a",
			"text for a",
			props={
				"href": "https://www.google.com"
			}
		)

		self.assertEqual(
			repr(html_node1),
			"HTMLNode: a, text for a, children: None, props: href=\"https://www.google.com\""
		)


	def test_repr_p(self):
		html_node1 = HTMLNode(
			"a",
			"text for a",
			props={
				"href": "https://www.google.com"
			}
		)

		html_node2 = HTMLNode(
			"p",
			"text for p",
			[html_node1]
		)

		self.assertEqual(
			repr(html_node2),
			f"HTMLNode: p, text for p, children: [{repr(html_node1)}]"
		)

	def test_props_to_html1(self):
		html_node1 = HTMLNode(
			"a",
		    "text for a",
		    props={
			    "href": "https://www.google.com"
		    }
		)

		self.assertEqual(
			html_node1.props_to_html(),
			" href=\"https://www.google.com\""
		)

	def test_props_to_html2(self):
		html_node1 = HTMLNode(
			"a",
			"text for a",
			props={
				"href": "https://www.google.com"
			}
		)

		html_node2 = HTMLNode(
			"p",
			"text for p",
			[html_node1]
		)

		self.assertEqual(
			html_node2.props_to_html(),
			""
		)
class TestLeafNode(unittest.TestCase):
	def test_to_html_p(self):
		node = LeafNode('p'
		                , "This is a paragraph"
		                )
		self.assertEqual(
			node.to_html(),
			"<p>This is a paragraph</p>"
		)

	def test_to_html_a(self):
		node = LeafNode(
			'a',
			"I am an anchor",
			{"href": "www.anchor_page.com"}
		)
		self.assertEqual(
			node.to_html(),
			"<a href=\"www.anchor_page.com\">I am an anchor</a>"
		)

	def test_to_html_abbr(self):
		node = LeafNode(
			'abbr',
		    "CSS"
		)
		self.assertEqual(
			node.to_html(),
			"<abbr>CSS</abbr>"
		)

	def test_repr_abbr(self):
		node = LeafNode(
			'abbr',
		    "CSS"
		)
		self.assertEqual(
			repr(node),
			"LeafNode: abbr, CSS"
		)

	def test_repr_a(self):
		node = LeafNode(
			'a',
			"I am an anchor",
			{"href": "www.ancor_page.com"}
		)
		self.assertEqual(
			repr(node),
		    "LeafNode: a, I am an anchor, props: href=\"www.ancor_page.com\""
		)

class TestParentNode(unittest.TestCase):
	def test_to_html1(self):
		node = ParentNode(
			"p",
			[
				LeafNode("b", "Bold text"),
				LeafNode(None, "Normal text"),
				LeafNode("i", "italic text"),
				LeafNode(None, "Normal text"),
			],
		)
		self.assertEqual(
			'<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>',
			node.to_html()
		)

	def test_to_html_no_tag(self):
		node = ParentNode(
			None,
		    [
				LeafNode("b", "Bold text"),
			]
		)
		self.assertRaises(ValueError, node.to_html)

	def test_to_html_no_children(self):
		node = ParentNode(
			'p',
			None
		)
		self.assertRaises(ValueError, node.to_html)

	def test_to_html_with_children(self):
		child_node = LeafNode("span", "child")
		parent_node = ParentNode("div", [child_node])
		self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

	def test_to_html_with_grandchildren(self):
		grandchild_node = LeafNode("b", "grandchild")
		child_node = ParentNode("span", [grandchild_node])
		parent_node = ParentNode("div", [child_node])
		self.assertEqual(
			parent_node.to_html(),
			"<div><span><b>grandchild</b></span></div>",
		)



if __name__ == "__main__":
	unittest.main()