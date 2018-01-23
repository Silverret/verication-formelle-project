from arithmetic_expression import ArithmeticExpression

class BooleanExpression(object):
    """
    Mother class of every boolean expression.

    If the mother class is instantiated,
    operande1 must be a string in ["true", "false"])
    """
    def __init__(self, operande1=None):
        self.operande1 = operande1
        if not operande1 is None:
            if operande1 not in ["true", "false"]:
                raise "BooleanExpression Exception : Must be 'false' or 'true'."

    def __call__(self):
        return eval(self.operande1.title())

class Equal(BooleanExpression):
    """
    Equal : a1 = a2

    a1 and a2 can be :
        - ArithmeticExpressions
        - integers (transformed in ArithmeticExpressions)
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
        return self.a1() == self.a2()

class InferiorOrEqual(BooleanExpression):
    """
    Inferior : a1 <= a2

    a1 and a2 can be :
        - ArithmeticExpressions
        - integers (transformed in ArithmeticExpressions)
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
        return self.a1() <= self.a2()

class Not(BooleanExpression):
    """
    Not : NOT b

    b must be a BooleanExpression
    """
    def __init__(self, b):
        super().__init__()
        self.b = b

    def __call__(self):
        return not self.b()

class And(BooleanExpression):
    """
    And : b1 AND b2

    b1 and b2 must be BooleanExpressions
    """
    def __init__(self, b1, b2):
        super().__init__()
        self.b1 = b1
        self.b2 = b2

    def __call__(self):
        return self.b1() and self.b2()


class Or(BooleanExpression):
    """
    Or : b1 OR b2

    b1 and b2 must be BooleanExpressions
    """
    def __init__(self, b1, b2):
        super().__init__()
        self.b1 = b1
        self.b2 = b2

    def __call__(self):
        return self.b1() or self.b2()
