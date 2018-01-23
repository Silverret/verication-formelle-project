class Instruction:
    def __init__(self, var1=None, var2=None):
        self.var1 = var1
        self.var2 = var2
    
class Skip(Instruction):
    def __init__(self):
        super().__init__()

class Assign(Instruction):
    def __init__(self, var1, var2):
        super().__init__(var1, var2)

class If(Instruction):
    def __init__(self, var1, var2 = None):
        super().__init__(var1, var2)

class While(Instruction):
    def __init__(self, var1, var2 = None, ):
        super().__init__(var1, var2)