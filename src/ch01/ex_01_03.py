import typing


def minmax(data: typing.List) -> typing.Tuple:
    """
    Return the minimum and maximum value in a list by a Tuple.
    """

    minimum = data[0]
    maximum = 0

    for number in data:
        if number <= minimum:
            minimum = number
        elif number >= maximum:
            maximum = number

    return (minimum, maximum)
