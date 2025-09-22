# main.py
from sys import argv
import colorama
from lexer import Lexer
from parser import Parser
from interpreter import Interpreter
from os import getcwd

colorama.init(autoreset = True)

def run_zscript(zScriptCode):
    lexer = Lexer(zScriptCode)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    tree = parser.parse()
    interpreter = Interpreter()
    interpreter.interpret(tree)

if __name__ == "__main__":
    try:
        try:
            with open(str(f"{getcwd()}\\{argv[1]}")) as f:
                code = f.read()
        except FileNotFoundError:
            print(colorama.Fore.RED + f"No such file found: {argv[1]}\n")
    except Exception as error:
        print(colorama.Fore.RED + f"Unexpected error: {error}\n")
