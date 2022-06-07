from Utils.Classes import Car


def main():
    # Test different methods of Car class using assertions
    car_a = Car(name='Audi', max_speed=220, acceleration=15)
    try:
        assert car_a.__str__() == 'Car "Audi" with max speed 220 and current speed 0.'
        print('Test passed')
    except AssertionError:
        print('Test failed...')

    try:
        assert car_a.accelerate(10) == 150
        print('Test passed')
    except AssertionError:
        print('Test failed...')

    # TODO: Generate more test cases and write the corresponding assertion test


if __name__ == '__main__':
    main()
