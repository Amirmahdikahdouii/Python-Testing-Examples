from itertools import islice
from functools import partial


def slice_iterable(iterable, number:int):
    return list(islice(iterable, number))


def chunked(iterable, number, strick=False):
    if not isinstance(number, int) or number < 0:
        raise ValueError("Only Non-negative Intergers are allowed")
    iterator = iter(partial(slice_iterable, iter(iterable), number), [])
    if strick:
        def check_stricked():
            for iterable in iterator:
                if len(iterable) != number:
                    raise ValueError(f"iterable is not divisable by number= {number}")
                yield iterable
        return iter(check_stricked())
    return iterator