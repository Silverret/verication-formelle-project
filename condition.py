class BooleanOperator:
    """
    Equal
    """
    EQUAL = "="

    """
    Inferior
    """
    INFERIOR = "<="

    """
    NOT
    """
    NOT = "not"

    """
    AND
    """
    AND = "and"

    """
    OR
    """
    OR = "or"


class Condition:
    """
    Condition class :
    operande1 can be :
        - a string (if it is a variable),
        - a integer (if it is a value),
        - a condition (for complex condition),
        - a bool (if its is 'True' or 'False')
    operande2 can be :
        - None,
        - a string (if it is a variable),
        - a integer (if it is a value),
        - a condition (for complex condition),
        - a bool (if its is 'True' or 'False')
    operator can be :
        - None,
        - one of the operators detailed above
    """

    def __init__(self, operande1, operande2=None, operator=None):
        self.operande1 = operande1
        self.operande2 = operande2
        self.operator = operator
