def sum_squares(n: int) -> float:
    """
    Return the sum of all squared numbers up to including n.

    :param n: Upper limit for square numbers as integer.
    :return: Sum of all squared numbers to n as float.
    """
    summed_squared = 0
    for i in range(n + 1):
        square = i ** 2
        summed_squared += square
    return summed_squared


def main():
    # TODO: Test the function with different values for n. Does the function return the correct values? If not, start
    #  debugging and fix the problem(s).
    print(sum_squares(3))  # 1 + 4 + 9 = 14
    print(sum_squares(5))  # 1 + 4 + 9 + 16 + 25 = 55


if __name__ == '__main__':
    main()
