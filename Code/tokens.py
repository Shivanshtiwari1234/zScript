# tokens.py

class TokenType:
    NUMBER = 'NUMBER'
    STRING = 'STRING'
    IDENTIFIER = 'IDENTIFIER'
    KEYWORD = 'KEYWORD'
    OPERATOR = 'OPERATOR'
    ASSIGN = 'ASSIGN'
    LPAREN = 'LPAREN'
    RPAREN = 'RPAREN'
    COLON = 'COLON'
    NEWLINE = 'NEWLINE'
    EOF = 'EOF'

KEYWORDS = [
    'let', 'if', 'else', 'while', 'function', 'return', 'print', 'input'
]

class Token:
    def __init__(self, type_, value, line):
        self.type = type_
        self.value = value
        self.line = line

    def __repr__(self):
        return f"{self.type}:{self.value}"
