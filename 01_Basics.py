import numpy as np


def calculate(x: int) -> float:
    return x**2 / (x-1)


def main():
    # TODO: Run this script using the debugger. Set breakpoints within the for loop and check the variable values for
    #  each loop through.
    numbers = np.arange(-5, 5, 2)
    results = []
    for n in numbers:
        result = calculate(n)
        results.append(result)
    print(results)


if __name__ == '__main__':
    main()


