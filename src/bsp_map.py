# coding: utf-8
from timer import timeit
from bsp import BSPTree, print_bsp


@timeit
def create_map():
    t = BSPTree()
    t._do_split()

    for leaf in t.leaves:
        print(leaf.label)
        print(leaf.rect)

    print_bsp(t, "bsp_tree_test.bmp")

    print("Leaves: ")
    for leaf in t.leaves:
        print(leaf)

if __name__ == "__main__":
    create_map()
