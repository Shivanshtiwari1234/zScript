# lexer.py
from tokens import Token, TokenType, KEYWORDS

DIGITS = '0123456789'

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.current_char = None
        self.line = 1
        self.advance()

    def advance(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(self.text) else None

    def tokenize(self):
        tokens = []
        while self.current_char is not None:
            if self.current_char in ' \t':
                self.advance()
            elif self.current_char == '\n':
                tokens.append(Token(TokenType.NEWLINE, '\\n', self.line))
                self.line += 1
                self.advance()
            elif self.current_char in DIGITS:
                tokens.append(self.make_number())
            elif self.current_char.isalpha():
                tokens.append(self.make_identifier())
            elif self.current_char == '"':
                tokens.append(self.make_string())
            elif self.current_char == '=':
                tokens.append(Token(TokenType.ASSIGN, '=', self.line))
                self.advance()
            elif self.current_char in '+-*/^':
                tokens.append(Token(TokenType.OPERATOR, self.current_char, self.line))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Token(TokenType.LPAREN, '(', self.line))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(TokenType.RPAREN, ')', self.line))
                self.advance()
            elif self.current_char == ':':
                tokens.append(Token(TokenType.COLON, ':', self.line))
                self.advance()
            elif self.current_char == '/' and self.peek() == '/':
                self.skip_comment()
            else:
                raise Exception(f"Illegal character '{self.current_char}' at line {self.line}")
        tokens.append(Token(TokenType.EOF, None, self.line))
        return tokens

    def make_number(self):
        num_str = ''
        while self.current_char is not None and self.current_char in DIGITS:
            num_str += self.current_char
            self.advance()
        return Token(TokenType.NUMBER, int(num_str), self.line)

    def make_identifier(self):
        id_str = ''
        while self.current_char is not None and (self.current_char.isalnum() or self.current_char == '_'):
            id_str += self.current_char
            self.advance()
        if id_str in KEYWORDS:
            return Token(TokenType.KEYWORD, id_str, self.line)
        return Token(TokenType.IDENTIFIER, id_str, self.line)

    def make_string(self):
        self.advance()  # skip opening quote
        string_value = ''
        while self.current_char is not None and self.current_char != '"':
            string_value += self.current_char
            self.advance()
        self.advance()  # skip closing quote
        return Token(TokenType.STRING, string_value, self.line)

    def skip_comment(self):
        while self.current_char is not None and self.current_char != '\n':
            self.advance()

    def peek(self):
        peek_pos = self.pos + 1
        return self.text[peek_pos] if peek_pos < len(self.text) else None
