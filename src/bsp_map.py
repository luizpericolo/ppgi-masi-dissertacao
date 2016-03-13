#coding: utf-8
import random
from PIL import Image, ImageDraw

class Rect:

	MIN_WIDTH = 10
	MIN_HEIGHT = 10

	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height

	def _switch_coordinates(self):
		"""
			Switches from a x, y, width, height parametrization to a x1, x2, y1, y2 parametrization.
			x1, y1 is the left-topmost point of the rect, whereas x2, y2 is the right-bottommost point of the rect.
		"""

		x1 = self.x
		y1 = self.y

		x2 = self.x + self.width 
		y2 = self.y + self.height

		return x1, y1, x2, y2

	def is_suitable(self):
		""" 
			Tests if this instance is suitable:
				* if both width and height are greater than or equal to their min values.
		"""

		return self.width >= self.MIN_WIDTH and self.height >= self.MIN_HEIGHT

	def _vertical_split(self, width_1, width_2):
		""" Performs a vertical split of the rect with the supplied width values. """

		return Rect(self.x, self.y, width_1, self.height), \
			Rect(self.x + width_1, self.y, width_2, self.height)

	def _horizontal_split(self, height_1, height_2):
		""" Performs a horizontal split of the rect with the supplied height values. """

		return Rect(self.x, self.y, self.width, height_1), \
			Rect(self.x, self.y + height_1, self.width, height_2)

	def split(self):
		""" Splits a rect in two either vertically or horizontally """

		horizontal = random.random() > 0.5

		if horizontal:
			top_height = random.randrange(10, self.height)
			bottom_height = self.height - top_height

			return self._horizontal_split(height_1=top_height, height_2=bottom_height)

		else:
			left_width = random.randrange(10, self.width)
			right_width = self.width - left_width

			return self._vertical_split(width_1=left_width, width_2=right_width)

	def split_half(self):
		""" Splits a rect in two halves of equal area, either vertically or horizontally """

		horizontal = random.random() > 0.5

		if horizontal:
			top_height = bottom_height = self.height / 2

			return self._horizontal_split(height_1=top_height, height_2=bottom_height)

		else:
			left_width = right_width = self.width / 2

			return self._vertical_split(width_1=left_width, width_2=right_width)

	def __str__(self):
		return u"<x: {} y: {} width: {} height: {}>".format(self.x, self.y, self.width, self.height)

class TreeNode:
	def __init__(self, label=""):

		self.rect = Rect(0, 0, 100, 100)
		self.label = label

	def is_suitable(self):
		""" Testing if this instance is suitable. Wraps is_suitable() from Rect """

		return self.rect.is_suitable()

class BSPTree:

	def __init__(self, n_max_nodes=20):
		self.MAX_NODES = n_max_nodes
		self.root = TreeNode(label="A")
		self.nodes = [self.root]
		self.leaves = [self.root]
		self.idx = 0
		self.last_label = "A"

	def _get_next_label(self):
		label = chr(ord(self.last_label)+1)
		self.last_label = label
		return label

	def add_n_nodes(self, n_nodes=10):
		for i in range(n_nodes):
			node = TreeNode(label=self._get_next_label())
			self.nodes.append(node)

	def _stop_condition_met(self):
		return len(self.nodes) >= self.MAX_NODES or len(self.nodes) == 0

	def _do_split(self):
		while not self._stop_condition_met():
			node = self._get_next_node()
			print "Processing node {}.".format(node.label)
			self.leaves.remove(node)

			l_child = TreeNode(label=self._get_next_label())
			r_child = TreeNode(label=self._get_next_label())

			if random.random() > 0.5:
				split_func = node.rect.split_half
			else:
				split_func = node.rect.split

			l_child.rect, r_child.rect = split_func()

			if l_child.is_suitable():
				self.nodes.append(l_child)
				self.leaves.append(l_child)

			if r_child.is_suitable():
				self.nodes.append(r_child)
				self.leaves.append(r_child)

	def _get_next_node(self):
		assert self.idx < len(self.nodes), u"Trying to access invalid position {}".format(self.idx)
		res = self.nodes[self.idx]
		self.idx += 1
		return res

	def get_leaves(self):
		return self.leaves

	def get_nodes(self):
		return self.nodes

def print_rects(rects, name="test.bmp"):
	size = (100, 100)
	im = Image.new('RGB', size)
	draw = ImageDraw.Draw(im)

	fill = 'blue'
	outline = 'black'

	for rect in rects:
		coords = list(rect._switch_coordinates())
		draw.rectangle(coords, fill, outline)

	im.save(name)

t = BSPTree()
t._do_split()

rects = []

for leaf in t.get_leaves():
	print leaf.label
	print leaf.rect
	rects.append(leaf.rect)

print_rects(rects, "bsp_test.bmp")
