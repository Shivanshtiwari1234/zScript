import sys
import re
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Global and local scopes
global_vars = {}
local_vars = {}
functions = {}

def evaluate_expression(expr):
    expr = expr.replace('^', '**')
    try:
        return eval(expr, {}, {**global_vars, **local_vars})
    except (NameError, SyntaxError, ZeroDivisionError, TypeError, ValueError):
        return expr

def execute_lines(lines):
    i = 0
    while i < len(lines):
        line = lines[i].strip()

        # Ignore comments
        if line.startswith('//') or line == '':
            i += 1
            continue

        try:
            # Print statement
            if line.startswith('print(') and line.endswith(')'):
                content = line[6:-1]
                print(evaluate_expression(content))

            # Input statement
            elif line.startswith('input(') and line.endswith(')'):
                prompt = line[6:-1]
                val = input(prompt)
                local_vars['_'] = val

            # Global variable
            elif line.startswith('global '):
                parts = line[len('global '):].split('=', 1)
                if len(parts) == 2:
                    name = parts[0].strip()
                    value = evaluate_expression(parts[1].strip())
                    global_vars[name] = value
                else:
                    raise SyntaxError

            # Local variable
            elif line.startswith('local '):
                parts = line[len('local '):].split('=', 1)
                if len(parts) == 2:
                    name = parts[0].strip()
                    value = evaluate_expression(parts[1].strip())
                    local_vars[name] = value
                else:
                    raise SyntaxError

            # Forever loop
            elif line.startswith('forever:'):
                block = []
                i += 1
                while i < len(lines) and lines[i].startswith('    '):
                    block.append(lines[i][4:])
                    i += 1
                while True:
                    execute_lines(block)

            # Function definition
            elif line.startswith('function '):
                name = line[len('function '):].split('(')[0].strip()
                block = []
                i += 1
                while i < len(lines) and lines[i].startswith('    '):
                    block.append(lines[i][4:])
                    i += 1
                functions[name] = block
                continue

            # Function call
            elif re.match(r'^[a-zA-Z_][a-zA-Z0-9_]*\(\)$', line):
                name = line[:-2]
                if name in functions:
                    execute_lines(functions[name])
                else:
                    raise NameError

            else:
                raise SyntaxError

        except Exception as e:
            print(f"{Fore.RED}Error in line {i+1}: {lines[i].strip()} ({type(e).__name__}){Style.RESET_ALL}")

        i += 1

# Run zScript file
if len(sys.argv) != 2:
    print("Usage: python main.py <file.zs>")
    sys.exit(1)

file_path = sys.argv[1]

with open(file_path, 'r') as f:
    code_lines = f.readlines()

execute_lines(code_lines)
