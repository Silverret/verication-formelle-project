from arithmetic_expression import ArithmeticExpression, Add, Minus, Time, VARIABLES
from boolean_expression import BooleanExpression, And, Or, Not, Equal, InferiorOrEqual

# Simple test avec des entiers
a1 = ArithmeticExpression(3)
a2 = ArithmeticExpression(10)

a3 = Minus(a2, a1)
print("a3 == 7 : ", a3()==7)


# Test avec des variables
VARIABLES['X'] = 9 # Variables est un dict du module arithmetic_expression
a1 = ArithmeticExpression(3)
a2 = ArithmeticExpression('X')

a3 = Time(a1, a2)
print("a3 == 27 : ", a3()==27)


VARIABLES['X'] -= 1
a1 = 3 # News here : on peut juste mettre l'int pour plus de lisibilité!
a2 = ArithmeticExpression('X')

a3 = Time(a1, a2) # Time(3, 'X')
print("a3 == 24 : ", a3()==24)


# Petits tests sur les boolean expressions
b = Equal(a3, 24)
print(" b : ", b())

# Finally
print("Equal(a3, 24) : ", Equal(a3, 24)())

