import numbers
from decimal                                    import Decimal


class KapsRounding(object):
    """docstring for ZigRounding"""

    def __init__(self, value):
        super(KapsRounding, self).__init__()
        self.value = value

    def round_2_places(self):

        if isinstance(self.value, numbers.Number):
            self.value = self.value
        elif str(self.value).isdigit():
            self.value = Decimal(self.value)
        else:
            self.value = Decimal(0.00)

        rounded_value = round(self.value, 2)

        return rounded_value
