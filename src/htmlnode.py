


class HTMLNode:
	def __init__(self, tag=None, value=None, children=None, props=None):
		self.tag = tag
		self.value = value
		self.children = children
		self.props = props

	def to_html(self):
		raise NotImplementedError("to_html method not implemented")

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

class LeafNode(HTMLNode):
	def __init__(self, tag, value, props=None):
		super().__init__(tag, value, None, props)

	def to_html(self):
		if self.value is None:
			raise ValueError("invalid HTML: no value")

		if self.tag is None:
			return self.value
		return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

	def __repr__(self):
		props_string = self.props_to_html()
		base = f"LeafNode: {self.tag}, {self.value}"
		if props_string:
			base += f", props: {props_string.strip()}"
		return base

class ParentNode(HTMLNode):
	def __init__(self, tag, children, props=None):
		super().__init__(tag=tag, value=None, children=children, props=props)

	def to_html(self):

		if self.tag is None:
			raise ValueError("invalid HTML: no tag")

		if self.children is None:
			raise ValueError("invalid HTML: Parent node must have children")

		inner =''.join(child.to_html() for child in self.children)
		return f'<{self.tag}>{self.props_to_html()}{inner}</{self.tag}>'

	def __repr__(self):
		base = f"LeafNode: {self.tag}, {self.children}"
		if self.props:
			base += f'{self.props}'
		return base


		








