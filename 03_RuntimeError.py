def division(x, y):
    try:
        print(x/y)
    except ZeroDivisionError:
        print('Division by 0 is not possible...')
    except TypeError:
        print('TypeError occurred, please check input values...')


def main():
    # Create a list of numbers and call the division function. Does the programm face an error?
    # TODO: Adapt the division function, that a warning is printed out but the programm still resumes
    numbers = list(range(-5, 5, 2))
    for n in numbers:
        division(n, n - 1)

    # Call the function again with other params. Why do we face an error again?
    # TODO: Adapt the function once again, that it is also capable of handling this type of error
    division(5, None)


if __name__ == '__main__':
    main()
