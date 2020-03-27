
def sqrt_list(n: int) -> int:
    """
    Return the sum of the squares of the integer less than n.
    """

    sqrts = [n * n for n in range(1, n)]
    return sum(sqrts)
