# coding: utf-8
import random
from rect import Rect, SIZE
from PIL import Image, ImageDraw, ImageFont


class BSPTree:
    def __init__(self, n_max_nodes=32):
        self.MAX_NODES = n_max_nodes
        self.root = TreeNode(label="A")
        self._nodes = [self.root]
        self._leaves = [self.root]
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
            print("Processing node {}.".format(node))
            self.leaves.remove(node)

            l_child = TreeNode(label=self._get_next_label())
            r_child = TreeNode(label=self._get_next_label())

            if random.random() > 0.5:
                split_func = node.rect.split_half
            else:
                split_func = node.rect.split

            l_child.rect, r_child.rect = split_func()

            if l_child.is_suitable():
                print("Criado {}".format(l_child))
                self.nodes.append(l_child)
                self.leaves.append(l_child)

            if r_child.is_suitable():
                print("Criado {}".format(r_child))
                self.nodes.append(r_child)
                self.leaves.append(r_child)

    def _get_next_node(self):
        assert self.idx < len(self.nodes), u"Trying to access invalid position {}".format(self.idx)
        res = self.nodes[self.idx]
        self.idx += 1
        return res

    @property
    def leaves(self):
        return self._leaves

    @property
    def nodes(self):
        return self._nodes

    @property
    def rects(self):
        return [leaf.rect for leaf in self._leaves]


class TreeNode:
    def __init__(self, label=""):
        self.rect = Rect(0, 0, *SIZE)
        self.label = label

    def is_suitable(self):
        """ Testing if this instance is suitable. Wraps is_suitable() from Rect """

        return self.rect.is_suitable()

    def __str__(self):
        return u"<{}> {}".format(self.label, self.rect)


def print_bsp(tree, name="bsp_tree_test.bmp"):
    font = ImageFont.truetype("Ubuntu-R.ttf", 14)
    im = Image.new('RGB', SIZE)
    draw = ImageDraw.Draw(im)

    fill = 'blue'
    outline = 'black'

    for node in tree.leaves:
        coords = list(node.rect._switch_coordinates())
        draw.rectangle(coords, fill, outline)
        draw.text(xy=node.rect._get_center(), text=node.label.upper(), fill=(0, 0, 0), font=font)

    im.save(name)
