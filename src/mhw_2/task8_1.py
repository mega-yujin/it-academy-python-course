"""You are given an expression with numbers, brackets and operators.
For this task only the brackets matter.
Brackets come in three flavors: "{}" "()" or "[]".
Brackets are used to determine scope or to restrict some expression.
If a bracket is open, then it must be closed with a bracket of the same type.
The scope of a bracket must not be intersected by another bracket.
In this task you should make a decision,
whether to correct an expression or not based on the brackets.
Do not worry about operators and operands
"""


def checkio(expression: str) -> bool:
    """
    Checks if brackets are placed correctly in expression
    :param expression: str: Expression to check
    :return: bool: True if correct
    """
    stack = []
    bracket_pairs = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in bracket_pairs.values():  # If it's an opening bracket
            stack.append(char)
        elif char in bracket_pairs.keys():  # If it's a closing bracket
            if stack and stack[-1] == bracket_pairs[char]:
                stack.pop()
            else:
                return False

    return len(stack) == 0


print(checkio(input('Введите строку: ')))
