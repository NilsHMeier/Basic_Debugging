class Car:

    def __init__(self, name: str, max_speed: int, acceleration: float):
        self.name = name
        self.speed = 0
        self.max_speed = max_speed
        self.acceleration = acceleration

    def __str__(self):
        return f'Car "{self.name}" with max speed {self.max_speed} and current speed {self.speed}.'

    def accelerate(self, time: float) -> float:
        speed_change = self.acceleration * time
        self.speed += speed_change
        if self.speed > self.max_speed:
            self.speed = self.max_speed
        return self.speed

    def decelerate(self, time: float) -> float:
        speed_change = self.acceleration * time
        self.speed -= speed_change
        if self.speed < 0:
            self.speed = 0
        return self.speed

    @property
    def get_speed(self) -> float:
        return self.speed
