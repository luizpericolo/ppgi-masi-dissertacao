# coding: utf-8
import time


def timeit(fn):
    def timed(*args, **kwargs):
        ts = time.time()
        result = fn(*args, **kwargs)
        te = time.time()

        print("{}({}, {}) - {:2.4f} seconds".format(fn.__name__, args, kwargs, te - ts))
        return(result)

    return timed
