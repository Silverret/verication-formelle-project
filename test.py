from IV_Classes.arithmetic_expression import ArithmeticExpression, Add, Minus, Time, Variable
from IV_Classes.boolean_expression import BooleanExpression, And, Or, Not, Equal, InferiorOrEqual, get_conditions

# Simple test avec des entiers
a1 = ArithmeticExpression(3)
a2 = ArithmeticExpression(10)

a3 = Minus(a2, a1)
print("a3 == 7 : ", a3()==7)


# Test avec des variables
a1 = ArithmeticExpression(3)
a2 = Variable('X')
a2.value = 9

a3 = Time(a1, a2)
print("a3 == 27 : ", a3()==27)

a1 = 3 # News here : on peut juste mettre l'int pour plus de lisibilité!

a3 = Time(a1, a2) # Time(3, 'X')
print("a3 == 24 : ", a3()==24)


# Petits tests sur les boolean expressions
b = Equal(a3, 24)
print(" b : ", b())

# Finally
print("Equal(a3, 24) : ", Equal(a3, 24)())

# Test deuxième partie : trouver les conditions à partir des décisions
b1 = Equal(24, a3)
b2 = Not(InferiorOrEqual(a3, 25))
b3 = Or(b1, And(b2, Equal(a3, 23)))

conditions1 = get_conditions(b3)
conditions2 = get_conditions(Not(b3))

print(conditions1)
print(conditions2)
print(conditions1 == conditions2)