import ast

def convert_to_list(value):
    try:
        return ast.literal_eval(value)
    except (SyntaxError, ValueError):
        return value