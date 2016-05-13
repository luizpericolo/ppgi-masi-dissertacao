# coding: utf-8

import random
from PIL import Image, ImageDraw

SIZE = (400, 400)


class Rect:
    MIN_WIDTH = SIZE[0] / 10
    MIN_HEIGHT = SIZE[1] / 10

    def __init__(self, x, y, width, height):
            self.x = x
            self.y = y
            self.width = width
            self.height = height

    def _get_center(self):
        """
        Returns the center of a rect
        """

        return self.x + self.width / 2, self.y + self.height / 2

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

        return Rect(self.x, self.y, width_1, self.height), Rect(self.x + width_1, self.y, width_2, self.height)

    def _horizontal_split(self, height_1, height_2):
        """ Performs a horizontal split of the rect with the supplied height values. """

        return Rect(self.x, self.y, self.width, height_1), Rect(self.x, self.y + height_1, self.width, height_2)

    def split(self):
        """ Splits a rect in two either vertically or horizontally """

        horizontal = random.random() > 0.5

        if horizontal:
            # XXX: Está dando empty range as vezes
            top_height = random.randrange(10, self.height)
            bottom_height = self.height - top_height

            return self._horizontal_split(height_1=top_height, height_2=bottom_height)

        else:
            # XXX: Está dando empty range as vezes
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


def print_rects(rects, name="test.bmp"):
    im = Image.new('RGB', SIZE)
    draw = ImageDraw.Draw(im)

    fill = 'blue'
    outline = 'black'

    for rect in rects:
        coords = list(rect._switch_coordinates())
        draw.rectangle(coords, fill, outline)

    im.save(name)
