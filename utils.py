from colorama import Fore, Style, init
init(autoreset=True)

# Error display helper
def show_error(line_num, code_line, error_type):
    print(f"{Fore.RED}Error in line {line_num}: {code_line} ({error_type}){Style.RESET_ALL}")

# Safe evaluation of arithmetic expressions
def evaluate_expression(expr, global_vars, local_vars):
    try:
        # Allowed operations only
        allowed_chars = "0123456789+-*/^(). _abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        if not all(c in allowed_chars for c in expr):
            raise ValueError("Invalid character in expression")

        # Replace ^ with ** for Python exponentiation
        expr = expr.replace("^", "**")

        # Merge local and global scope for eval
        scope = {}
        scope.update(global_vars)
        scope.update(local_vars)

        return eval(expr, {"__builtins__": None}, scope)

    except Exception as e:
        raise ValueError(f"Evaluation error: {e}")

# Validate variable names
def is_valid_var_name(name):
    return name.isidentifier() and not name.isnumeric()

# Strip comments from a line
def strip_comment(line):
    return line.split("//")[0].strip()
