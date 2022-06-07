def main():
    # TODO: Fix the errors in this script
    name = input('What is your name? ')
    print('Nice to meet you {name}!')

    age = int(input('What is your age?'))
    if age >= 18:
        print('You are already of age, nice.')
    else:
        print('You are not of age yet...')


if __name__ == '__main__':
    main()