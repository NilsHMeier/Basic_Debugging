import unittest
from Utils.Classes import Car


class TestCarMethods(unittest.TestCase):

    def test_string_method(self):
        car_a = Car(name='Audi', max_speed=220, acceleration=15)
        self.assertEqual(car_a.__str__(),
                         'Car "Audi" with max speed 220 and current speed 0.')

    def test_acceleration(self):
        car_a = Car(name='Audi', max_speed=220, acceleration=15)
        self.assertEqual(car_a.accelerate(4), 60)
        self.assertEqual(car_a.accelerate(30), 220)

    def test_deceleration(self):
        car_a = Car(name='Audi', max_speed=220, acceleration=15)
        car_a.accelerate(10)
        self.assertEqual(car_a.decelerate(5), 75)
        self.assertEqual(car_a.decelerate(10), 0)

    def test_multiple_cars(self):
        car_a = Car(name='Audi', max_speed=220, acceleration=15)
        car_b = Car(name='Renault', max_speed=140, acceleration=6)
        car_a.accelerate(8)
        self.assertEqual(car_b.accelerate(5), 30)


if __name__ == '__main__':
    unittest.main()
