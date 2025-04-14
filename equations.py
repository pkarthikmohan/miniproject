import re
from sympy import symbols, Eq, solve, sympify

def extract_equation(user_input):
    user_input = user_input.lower()
    # Remove unnecessary command words
    command_words = ['solve', 'calculate', 'evaluate', 'what is', 'please', 'find', 'the value of', '?']
    for word in command_words:
        user_input = user_input.replace(word, '')
    user_input = user_input.strip()
    return user_input.replace('^', '**')

def solve_equation(equation_str):
    if '=' in equation_str:
        # It's an equation
        left, right = equation_str.split('=')
        left_expr = sympify(left)
        right_expr = sympify(right)
        vars_in_eq = list(left_expr.free_symbols.union(right_expr.free_symbols))
        if not vars_in_eq:
            raise ValueError("No variables found in the equation.")

        eq = Eq(left_expr, right_expr)
        solution = solve(eq, vars_in_eq[0])
        return f"Solution for {vars_in_eq[0]}: {solution}"
    else:
        # Just evaluate expression
        result = sympify(equation_str).evalf()
        return f"Result: {result}"





