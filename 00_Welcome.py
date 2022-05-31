def main():
    print('Debugging is easy and can be done by everyone.')
    return 0


if __name__ == '__main__':
    try:
        assert main() is None
    except AssertionError as e:
        print('Exception caught...')
    finally:
        print("Now it's your turn!")
