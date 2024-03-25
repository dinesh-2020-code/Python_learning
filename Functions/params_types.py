def func(p1, p2, *args, k, **kwargs):
    """

    Args:
        p1: Positional param
        p2: Positional param p2
        *args: var-positional param
        k: keyword-argument
        **kwargs: var-keyword arguments

    Returns:

    """
    print("Positional-or-keyword:...{}, {}".format(p1, p2))
    print("var-positional (*args):..{}".format(args))
    print("keyword:.................{}".format(k))
    print("var-keyword:.............{}".format(kwargs))


def sum_numbers(*args: float) -> float:
    """Calculate sum of numbers passed to args
    Args:
        *args: tuple containing unpacked float values passed during calling of function

    Returns: Sum total of the numbers passed to args

    """
    tot_sum = 0
    for num in args:
        tot_sum += num
    return tot_sum


# func(1, 2, 3, 4, 5, k=6, key1=7, key2=8)  # the same name `k` must be used. If we use some another variable
# instead of `k`, python will raise TypeError: func() missing 1 required keyword-only argument: 'k'

print(sum_numbers(1, 2, 3))
print(sum_numbers(12.5, 3.147, 98.1))
print(sum_numbers(1.1, 2.2, 5.5))
