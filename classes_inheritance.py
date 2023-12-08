class Device:
    def __init__(self, screen_size: float, acc_capacity: int):
        """
        Электронное устройство.

        :param screen_size: Размер экрана.
        :param acc_capacity: Ёмкость батареи.
        """
        self.screen_size = screen_size
        self.acc_capacity = acc_capacity

    def method(self, a, b, c):
        return self.screen_size * a * b * c


class Smartphone(Device):
    def __init__(self, screen_size: float, acc_capacity: int, has_camera: bool):
        super().__init__(screen_size, acc_capacity)
        self.has_camera = has_camera

    def __repr__(self) -> str:
        return super().__repr__()

    def method(self, a, b, c):
        return super().method(a, b, c) / 2


phone = Smartphone(5.4, 4200, True)
print(phone.screen_size)

