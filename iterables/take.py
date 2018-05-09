"""Module for demonstrating generaator execution."""


def take(count, iterable):
    """Take items from te front of iterable.

    Args:
        count: The maximum number of items to retrieve.
        iterable: The source series.

    Yields:
        At most 'count' items from 'iterable'.
    """
    counter = 0
    for item in iterable:
        if counter == count:
            return
        counter += 1
        yield item


def run_take():
    items = [2, 4, 6, 8, 10]
    items = {2, 3, 4, 5, 6, 7, 7, 7, 7}
    items = list(items)
    print(type(items))
    for item in take(3, items):
        print(item)


def distinct(iterable):
    """Return unique items by eliminating duplicates.

    Args:
        iterable: The source series.

    Yields:
        Unique elments in order from 'iterable'.
    """
    seen = set()
    for item in iterable:
        if item in seen:
            continue
        yield item
        seen.add(item)


def run_distinct():
    items = [5, 7, 7, 6, 5, 5]
    for item in distinct(items):
        print(item)


def calc_square():
    """Uses hardly any memory and each use of generator
    has to be re-caled since they are once use objects. """

    s = sum(x*x for x in range(1,10000001))
    print(s)


if __name__ == '__main__':
    # run_take()
    # run_distinct()
    calc_square()