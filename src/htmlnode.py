

class HTMLNode:
	def __init__(self, tag=None, value=None, children=None, props=None):
		self.tag = tag
		self.value = value
		self.children = children
		self.props = props

	def to_html(self):
		raise NotImplemented("to_html method not implemented")

	def props_to_html(self):
		if not self.props:
			return ""
		return "".join(f" {k}=\"{self.props[k]}\"" for k in sorted(self.props))

	def __repr__(self):
		if self.children is None:
			children_repr = "None"
		elif isinstance(self.children, list):
			children_repr = "[" + ", ".join(repr(c) for c in self.children) + "]"
		else:
			children_repr = repr(self.children)
		props_string = self.props_to_html()
		base = f"HTMLNode: {self.tag}, {self.value}, children: {children_repr}"
		if props_string:
			base += f", props: {props_string.strip()}"
		return base


