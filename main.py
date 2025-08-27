# main.py
from lexer import Lexer
from parser import Parser
from interpreter import Interpreter

def run_zscript(code):
    lexer = Lexer(code)
    tokens = lexer.tokenize()
    parser = Parser(tokens)
    tree = parser.parse()
    interpreter = Interpreter()
    interpreter.interpret(tree)

if __name__ == "__main__":
    with open("examples/hello.zs") as f:
        code = f.read()
    run_zscript(code)
