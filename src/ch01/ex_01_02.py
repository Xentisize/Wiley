def is_even(k: int) -> bool:
    """
    Check if the integer is an even number.
    
    Since multiplication, division and modulo cannot be used,
    I tried to substract the number by 2 until the remainder 
    becomes either 1 or 0 so I can see if it is an even number.

    Since the algorithm does not work with negative number, I take 
    the absolute value of the number before substraction.
    """
    k = abs(k)
    while k >= 2:
        k -= 2
    if k == 1:
        return False
    else:
        return True
