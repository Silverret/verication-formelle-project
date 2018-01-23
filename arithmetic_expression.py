Variables = {}

class ArithmeticExpression(object):
    """
    Mother class of every arithmetic expression.

    If the mother class is instantiated,
    a must be a string or an integer
    """
    def __init__(self, a=None):
        self.a = a

    def __call__(self):
        if isinstance(self.a, str):
            return Variables[self.a]
        elif isinstance(self.a, int):
            return self.a

class Add(ArithmeticExpression):
    """
    Add : a1 + a2

    a1 and a2 must be ArithmeticExpressions
    """
    def __init__(self, a1, a2):
        super().__init__()
        self.a1 = a1
        self.a2 = a2

    def __call__(self):
        return self.a1() + self.a2()

class Minus(ArithmeticExpression):
    """
    Minus : a1 - a2

    a1 and a2 must be ArithmeticExpressions
    """
    def __init__(self, a1, a2):
        super().__init__()
        self.a1 = a1
        self.a2 = a2

    def __call__(self):
        return self.a1() - self.a2()

class Time(ArithmeticExpression):
    """
    Time :  a1 * a2

    a1 and a2 must be ArithmeticExpressions
    """
    def __init__(self, a1, a2):
        super().__init__()
        self.a1 = a1
        self.a2 = a2

    def __call__(self):
        return self.a1() * self.a2()
