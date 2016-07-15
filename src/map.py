import random

from PIL import Image, ImageDraw


class Room:
    """
    Parametrized by x, y, width, height where:
    * x, y is the left-topmost point of the room.
    * width is the width of the room.
    * height is the height of the room.
    """

    def __init__(self, r_id, x, y, width, height):
        self.id = r_id
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def print_room(self):
        print(u"<id: {}, x: {}, y: {}, width: {}, height: {}>".format(self.id, self.x, self.y, self.width, self.height))

    def intersect(self, room):
        """ Method that checks wether two rooms intersect or not. """

        x1, y1, x2, y2 = self._switch_coordinates()
        r_x1, r_y1, r_x2, r_y2 = room._switch_coordinates()

        if (x1 < r_x2 and x2 > r_x1 and y1 < r_y2 and y2 > r_y1):
            return True

        return False

    def _switch_coordinates(self):
        # Switching from a x, y, width, height parametrization to a x1, x2, y1, y2 parametrization for faster testing purposes
        # x1, y1 is the left-topmost point of the rect, whereas x2, y2 is the right-bottommost point of the rect.

        x1 = self.x
        y1 = self.y

        x2 = self.x + self.width
        y2 = self.y + self.height

        return x1, y1, x2, y2

    @property
    def center(self):
        return (self.x + self.width / 2, self.y + self.height / 2)

    class Map:

    def __init__(self, max_width=50, max_height=50):
        self.rooms = []
        self.corridors = []
        self.room_map = {}
        self.max_width = max_width
        self.max_height = max_height

    def add_room(self, room_id, x, y, width, height):
        """ Creates and adds a room to the map. """

        while True:
            can_place = True
            x = random.randrange(0, 100)
            y = random.randrange(0, 100)
            new_room = Room(room_id, x, y, width, height)
                for room in self.rooms:
                    if new_room.intersect(room):
                        can_place = False
                        break
                if can_place:
                    self.rooms.append(new_room)
                    self.room_map[room_id] = new_room
                    break

    def print_rooms(self):
        """ Prints a map's room list. """

        for room in self.rooms:
            room.print_room()

    def print_corridors(self):
        """ Prints a map's corridor list. """
        for corridor in self.corridors:
            corridor.print_corridor()

    def add_corridor(self, origin, destination):
        origin_room = self.room_map.get(origin)
        destination_room = self.room_map.get(destination)
        new_corridor = Corridor(origin_room, destination_room)

        self.corridors.append(new_corridor)

    def import_from_graph(self, graph):
        for node in graph.nodes:
            w, h = self.get_random_room_dimensions()

            # XXX: Improve this x=None, y=None.
            # Check add_room.
            self.add_room(node, None, None, w, h)

        for edge in graph.edges:
            origin, destination = edge
            self.add_corridor(origin, destination)

    def get_random_room_dimensions(self):
        """ Returns a tuple (w, h) with random values. """

        return random.randrange(self.max_width / 2, self.max_width), random.randrange(self.max_height / 2, self.max_height)

    def print_map(self):
        size = (100 + self.max_width, 100 + self.max_height)
        im = Image.new('RGB', size)
        draw = ImageDraw.Draw(im)

        fill = 'blue'
        outline = 'black'

        for room in self.rooms:
            coords = list(room._switch_coordinates())
            draw.rectangle(coords, fill, outline)

        corridor_fill = 'yellow'
        for corridor in self.corridors:
            draw.line(corridor.coords, fill)

        im.save('test.bmp')


class Corridor:

    def __init__(self, origin, destination):
        self._origin = origin
        self._destination = destination

    @property
    def coords(self):
        return tuple(self._origin.center) + tuple(self._destination.center)

    def print_corridor(self):
        print(u"From room {origin} to room {destination}".format(origin=self._origin.id, destination=self._destination.id))
