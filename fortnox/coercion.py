from decimal import Decimal


class Coercion(object):
    """
    Class used to make coertion between data returned from Base and data usable for developer
    """

    @staticmethod
    def to_decimal(value):
        """
        Coerce a value into a Decimal

        :param str value: a value to be coerced
        """
        return Decimal(str(value))

    @staticmethod
    def to_string(value):
        """
        Coerce a value into a String

        :param float value: a value to be coerced
        """
        return str(value)
