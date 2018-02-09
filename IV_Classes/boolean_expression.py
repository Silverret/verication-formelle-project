from IV_Classes.arithmetic_expression import ArithmeticExpression


def get_conditions_util(bexp, conditions):
    if isinstance(bexp, And) or isinstance(bexp, Or):
        get_conditions_util(bexp.b1, conditions)
        get_conditions_util(bexp.b2, conditions)
    elif isinstance(bexp, Not):
        get_conditions_util(bexp.b, conditions)
    else:
        conditions.add(bexp)

def get_conditions(bexp):
    conditions = set()
    get_conditions_util(bexp, conditions)
    return conditions

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
    
    def __repr__(self):
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

    def __repr__(self):
        return f"Equal({self.a1},{self.a2})"

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

    def __repr__(self):
        return f"InferiorOrEqual({self.a1},{self.a2})"

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

    def __repr__(self):
        return f"Not({self.b})"

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

    def __repr__(self):
        return f"And({self.b1},{self.b2})"


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

    def __repr__(self):
        return f"Or({self.b1},{self.b2})"
