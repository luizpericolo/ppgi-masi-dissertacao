# coding: utf-8
from timer import timeit
from bsp import BSPTree
from rect import print_rects


@timeit
def create_map():
    t = BSPTree()
    t._do_split()

    for leaf in t.leaves:
        print leaf.label
        print leaf.rect

    rects = t.rects

    print_rects(rects, "bsp_test.bmp")

if __name__ == "__main__":
    create_map()
