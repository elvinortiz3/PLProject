from itertools import product
import re


# Function to exchange all operators with those evaluated by python.
def replace_operators(expr):
    REPLACEMENTS = {
        'A': ' a ',
        'B': ' b ',
        'C': ' c ',
        'D': ' d ',
        'E': ' e ',
        'F': ' f ',
        'G': ' g ',
    }
    return re.sub('|'.join(re.escape(sym) for sym in REPLACEMENTS.keys()),
                  lambda sym: REPLACEMENTS[sym.group(0)],
                  expr).strip()


# Function to find all variables in a logic expression.
def extract_variables(expr):
    ops = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    vars = sorted(set(re.findall(r'[a-z]+', expr)))

    for op in ops:
        while op in vars:
            vars.remove(op)

    return vars


# Converts the current tree to a list of expressions
def tree_to_string(env):
    expr_list = [list()]
    expr = [str(env[0])]
    string = str(env[1])
    for i in range(len(env[2])):
        node = env[2][i]
        if len(node) < 3:
            string = string + " " + str(node[0])
        else:
            string = string + " " + str(node[0])
            next_strings = tree_to_string(node)
            expr_list = expr_list + next_strings

    expr.append(string)
    expr_list[0] = expr
    return expr_list


# Function to convert the current group of expressions into one equivalent logical expression.
def env_to_expr(env):
    expression_list = tree_to_string(env)
    expression = expression_list[0][1]

    for i in range(1, len(expression_list)):
        if expression_list[i][0] in expression.split():
            temp_expr = (expression_list[i][1])
            temp_expr = '( ' + temp_expr + ' )'
            expression = expression.replace(expression_list[i][0], temp_expr)

    return expression