import math

cos = math.cos
sin = math.sin
sqrt = math.sqrt
exp = math.exp
E = math.e
PI = math.pi


def ackley(x, y):
    a = -20 * exp(-0.2 * sqrt(0.5 * (x ** 2 + y ** 2)))
    b = - exp(0.5 * (cos(2 * x * PI) + cos(2 * y * PI)))
    c = E + 20

    return a + b + c


def beale(x, y):
    return (1.5 - x - x * y) ** 2 + (2.25 - x + x * (y) ** 2) ** 2 + (2.625 - x + x * (y ** 3)) ** 2


def goldstein_price(x, y):
    a = (1 + ((x + y + 1) ** 2) * (19 - 14 * x + 3 * x ** 2 - 14 * y + 6 * x * y + 3 * y ** 2))
    b = (30 + ((2 * x - 3 * y) ** 2) * (18 - 32 * x + 12 * x ** 2 + 48 * y - 36 * x * y + 27 * y ** 2))

    return a * b


def booth(x, y):
    return (x + 2 * y - 7) ** 2 + (2 * x + y - 5) ** 2


def bukin(x, y):
    return 100 * sqrt(abs(y - 0.01 * (x ** 2))) + 0.01 * abs(x + 10)


def matyas(x, y):
    return 0.26 * (x ** 2 + y ** 2) - 0.48 * x * y


def levi_13(x, y):
    a = sin(3 * PI * x) ** 2
    b = ((x - 1) ** 2) * (1 + sin(3 * PI * y) ** 2)
    c = ((y - 1) ** 2) * (1 + sin(2 * PI * y) ** 2)

    return a + b + c


def three_hump_camel(x, y):
    return 2 * x ** 2 - 1.05 * x ** 4 + (x ** 6 / 6) + x * y + y ** 2


def easom(x, y):
    return - cos(x) * cos(y) * exp(-((x - PI) ** 2 + (y - PI) ** 2))


def cross_in_tray(x, y):
    return -.0001 * (abs(sin(x) * sin(y) * exp(abs(100 - (sqrt(x ** 2 + y ** 2) / PI)))) + 1) ** 0.1


def eggholder(x, y):
    a = -(y + 47) * sin(sqrt(abs(x / 2 + (y + 47))))
    b = -x * sin(sqrt(abs(x - (y + 47))))

    return a + b


def holder_table(x, y):
    return -abs(sin(x) * cos(y) * exp(abs(1 - (sqrt(x ** 2 + y ** 2) / PI))))


def mccormick(x, y):
    return sin(x + y) + (x - y) ** 2 - 1.5 * x + 2.5 * y + 1


def schaffer_2(x, y):
    return 0.5 + (sin(x ** 2 - y ** 2) ** 2 - 0.5) / (1 + 0.001 * (x ** 2 + y ** 2)) ** 2


def schaffer_4(x, y):
    return 0.5 + (cos(sin(abs(x ** 2 - y ** 2))) ** 2 - 0.5) / (1 + 0.001 * (x ** 2 + y ** 2)) ** 2


mapping = {
    ackley: {
        "min": [(0, 0)],
        "domain": [(-5, 5), (-5, 5)]
    },
    beale: {
        "min": [(3, 0.5)],
        "domain": [(-4.5, 4.5), (-4.5, 4.5)]
    },
    goldstein_price: {
        "min": [(0, -1)],
        "domain": [(-2, 2), (-2, 2)]
    },
    booth: {
        "min": [(1, 3)],
        "domain": [(-10, 10), (-10, 10)]
    },
    bukin: {
        "min": [(-10, 1)],
        "domain": [(-15, 5), (-3, 3)]
    },
    matyas: {
        "min": [(0, 0)],
        "domain": [(-10, 10), (-10, 10)]
    },
    levi_13: {
        "min": [(1, 1)],
        "domain": [(-10, 10), (-10, 10)]
    },
    three_hump_camel: {
        "min": [(0, 0)],
        "domain": [(-5, 5), (-5, 5)]
    },
    easom: {
        "min": [(PI, PI)],
        "domain": [(-100, 100), (-100, 100)]
    },
    cross_in_tray: {
        "min": [(1.34941, 1.34941), (-1.34941, 1.34941), (1.34941, -1.34941), (-1.34941, -1.34941)],
        "domain": [(-10, 10), (-10, 10)]
    },
    eggholder: {
        "min": [(512, 404.2319)],
        "domain": [(-512, 512), (-512, 512)]
    },
    holder_table: {
        "min": [(8.05504, 9.66459), (-8.05504, 9.66459), (8.05504, -9.66459), (-8.05504, -9.66459)],
        "domain": [(-10, 10), (-10, 10)]
    },
    mccormick: {
        "min": [(-0.54719, -1.54719)],
        "domain": [(-1.5, 4), (-3, 4)]
    },
    schaffer_2: {
        "min": [(0, 0)],
        "domain": [(-100, 100), (-100, 100)]
    },
    schaffer_4: {
        "min": [(0, 1.25313)],
        "domain": [(-100, 100), (-100, 100)]
    },
}
