
class ArithmeticExpression(object):
    """
    Mother class of every arithmetic expression.
    """
    def __init__(self, a=None):
        self.a = a

    def __call__(self):
        return self.a
    
    def __repr__(self):
        return str(self.a)

    def replace(self, old_a, new_a):
        if not self.a == old_a:
            return self
        return ArithmeticExpression(new_a)

class Variable(ArithmeticExpression):
    """
    Variable
    """
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.value = None

    def __call__(self):
        if not isinstance(self.value, int):
            raise ArithmeticError
        return self.value

    def __repr__(self):
        return "Variable." + self.name
    
    def replace(self, old_a, new_a):
        if self.name == old_a.name:
            return new_a
        return self

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

    def replace(self, old_a, new_a):
        return Add(self.a1.replace(old_a, new_a), self.a2.replace(old_a, new_a))

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

    def replace(self, old_a, new_a):
        return Minus(self.a1.replace(old_a, new_a), self.a2.replace(old_a, new_a))

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

    def replace(self, old_a, new_a):
        return Time(self.a1.replace(old_a, new_a), self.a2.replace(old_a, new_a))
