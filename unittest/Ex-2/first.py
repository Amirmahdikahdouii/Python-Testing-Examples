_marker = object()


def first(iterable, default=_marker):
    """
    In This Function, we try to make itertools.first() method behaviour.
    >>> first([1,2,3])
    3

    >>> first((4,5,6), None)
    4
    """
    try:
        return next(iter(iterable))
    except StopIteration as e:
        if default == _marker:
            raise ValueError(
                "first() trying to return empty iterable first value "
                "and default was not set") from e
        return default
