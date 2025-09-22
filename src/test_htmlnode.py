import unittest
from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):

	def test_repr(self):
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
			repr(html_node1),
			"HTMLNode: a, text for a, children: None, props: href=\"https://www.google.com\""
		)
		self.assertEqual(
			repr(html_node2),
			f"HTMLNode: p, text for p, children: [{repr(html_node1)}]"
		)

	def test_props_to_html(self):
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
			html_node1.props_to_html(),
			" href=\"https://www.google.com\""
		)
		self.assertEqual(
			html_node2.props_to_html(),
			""
		)



if __name__ == "__main__":
	unittest.main()