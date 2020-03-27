def sqrt_odd_list(n: int) -> int:
    """
    Return the summation of all squared odd number smaller than n.
    """
    sqrt_odd = [num * num for num in range(1, n) if num % 2 == 1]
    return sum(sqrt_odd)
