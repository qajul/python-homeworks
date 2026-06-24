class Romb:

    def __init__(self, side_a, angle_a):
        self.side_a = side_a
        self.angle_a = angle_a

    def __setattr__(self, name, value):

        if name == "side_a":
            if value <= 0:
                raise ValueError("side_a повинна бути більшою за 0")

        if name == "angle_a":
            if value <= 0 or value >= 180:
                raise ValueError("angle_a повинен бути більше ніж 0 і менше 180")

            super().__setattr__("angle_b", 180 - value)

        super().__setattr__(name, value)


r = Romb(20, 40)

print("Сторона:", r.side_a)
print("Кут A:", r.angle_a)
print("Кут B:", r.angle_b)