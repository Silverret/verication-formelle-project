
class ArithmeticExpression(object):
    """
    Mother class of every arithmetic expression.

    If the mother class is instantiated,
    a must be an integer
    """
    def __init__(self, a=None):
        self.a = a

    def __call__(self):
        return self.a
    
    def __repr__(self):
        return str(self.a)

class Variable(ArithmeticExpression):
    """
    Variable
    """
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.value = None

    def __call__(self):
        return self.value

    def __repr__(self):
        return "Variable." + self.name

class Add(ArithmeticExpression):
    """
    Add : a1 + a2

    a1 and a2 must be ArithmeticExpressions
    """
    def __init__(self, a1, a2):
        super().__init__()
        if isinstance(a1, int):
            a1 = ArithmeticExpression(a1)
        if isinstance(a2, int):
            a2 = ArithmeticExpression(a2)
        self.a1 = a1
        self.a2 = a2

    def __call__(self):
        return self.a1() + self.a2()

    def __repr__(self):
        return f"Add({self.a1},{self.a2})"

class Minus(ArithmeticExpression):
    """
    Minus : a1 - a2

    a1 and a2 must be ArithmeticExpressions
    """
    def __init__(self, a1, a2):
        super().__init__()
        if isinstance(a1, int):
            a1 = ArithmeticExpression(a1)
        if isinstance(a2, int):
            a2 = ArithmeticExpression(a2)
        self.a1 = a1
        self.a2 = a2

    def __call__(self):
        return self.a1() - self.a2()

    def __repr__(self):
        return f"Minus({self.a1},{self.a2})"

class Time(ArithmeticExpression):
    """
    Time :  a1 * a2

    a1 and a2 must be ArithmeticExpressions
    """
    def __init__(self, a1, a2):
        super().__init__()
        if isinstance(a1, int):
            a1 = ArithmeticExpression(a1)
        if isinstance(a2, int):
            a2 = ArithmeticExpression(a2)
        self.a1 = a1
        self.a2 = a2

    def __call__(self):
        return self.a1() * self.a2()

    def __repr__(self):
        return f"Time({self.a1},{self.a2})"
