class ArithmeticExpression:
    """
    Mother class of every arithmetic expression.

    a and b can be :
        - arithmetic expression
        - an integer
        - a variable
    """
    def __init__(self, a, b):
        pass

class Add(ArithmeticExpression):
    """
    Add : a + b
    """
    def __init__(self, a, b):
        super().__init__(a, b)


class Minus(ArithmeticExpression):
    """
    Minus : a - b
    """
    def __init__(self, a, b):
        super().__init__(a, b)

class Time(ArithmeticExpression):
    """
    Time : a * b
    """
    def __init__(self, a, b):
        super().__init__(a, b)
