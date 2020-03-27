
def sqrt_list(n: int) -> int:
    """
    Return the sum of the squares of the integer less than n.

    The solution has already satsfied the requirement of ex_01_05
    """

    sqrts = [n * n for n in range(1, n)]
    return sum(sqrts)
