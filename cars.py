"""This script describes a beheavior of two types of cars"""

from php import BaseCar

class GasCar(BaseCar):
    """GasCar class which inherits from BaseCar abstract class"""

    def drive(self):
        return 'brrrum'

    def __add__(self, obj):
        if isinstance(obj, BaseCar):
            raise CarAccident()


class DieselCar(BaseCar):
    """DieselCar class which inherits from BaseCar abstract class"""

    def drive(self):
        return 'pyr pyr pyr'

    def __add__(self, obj):
        if isinstance(obj, BaseCar):
            raise CarAccident()


class CarAccident(Exception):
    """Exception that raises a 'crash' messages"""

    def __init__(self):
        super(CarAccident, self).__init__()
        self.message = 'Crash!'
