import math


class InverterCalculator:

    STANDARD_SIZES = [
        1,
        1.5,
        2,
        3,
        3.5,
        5,
        7.5,
        10,
        15,
        20,
        30,
        40,
        50,
        75,
        100,
    ]

    def __init__(self, connected_load):

        self.connected_load = connected_load

    def recommended_size(self):
        """
        Recommend inverter using
        80% loading rule.
        """

        kva = self.connected_load / 800

        for size in self.STANDARD_SIZES:

            if kva <= size:
                return size

        return math.ceil(kva)