class Instruction:
    def __init__(self):
        pass
    
class Skip(Instruction):
    """
    Skip : instruction which does nothing
    """
    def __init__(self):
        super().__init__()

class Assign(Instruction):
    """
    Assign : x := y

    x must be :
        - a string (<=> variable)
    y can be :
        - a string (<=> variable)
        - a integer (<=> value)
        - an arithmetic expression
    """
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y

class If(Instruction):
    """
    If : if b then c1 else c2

    b is a boolean expression
    c1, c2 are instructions
    """
    def __init__(self, b, c1, c2):
        super().__init__()
        self.b = b
        self.c1 = c1
        self.c2 = c2

class While(Instruction):
    """
    While : while b do c

    b is a boolean expression
    c is an instruction
    """
    def __init__(self, b, c):
        super().__init__()
        self.b = b
        self.c = c

class Seq(Instruction):
    """
    Seq : (c1;c2)

    c1 and c2 are instructions
    """
    def __init__(self, c1, c2):
        super().__init__()
        self.c1 = c1
        self.c2 = c2
    