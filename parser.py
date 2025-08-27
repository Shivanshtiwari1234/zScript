# parser.py
from tokens import TokenType
from nodes import *

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0
        self.current_token = self.tokens[self.pos]

    def advance(self):
        self.pos += 1
        if self.pos < len(self.tokens):
            self.current_token = self.tokens[self.pos]

    def parse(self):
        statements = []
        while self.current_token.type != TokenType.EOF:
            if self.current_token.type == TokenType.NEWLINE:
                self.advance()
                continue
            statements.append(self.statement())
        return statements

    def statement(self):
        if self.current_token.type == TokenType.KEYWORD:
            if self.current_token.value == 'let':
                return self.var_assign()
            elif self.current_token.value == 'print':
                return self.print_statement()
            elif self.current_token.value == 'if':
                return self.if_statement()
            elif self.current_token.value == 'while':
                return self.while_statement()
            elif self.current_token.value == 'function':
                return self.func_def()
        return self.expr()

    def var_assign(self):
        self.advance()  # skip 'let'
        var_name = self.current_token.value
        self.advance()
        if self.current_token.type == TokenType.ASSIGN:
            self.advance()
            expr = self.expr()
            return VarAssignNode(var_name, expr)
        raise Exception("Expected '=' after variable name")

    def print_statement(self):
        self.advance()
        expr = self.expr()
        return PrintNode(expr)

    def if_statement(self):
        self.advance()
        condition = self.expr()
        if self.current_token.type != TokenType.COLON:
            raise Exception("Expected ':' after if condition")
        self.advance()
        body = []
        while self.current_token.type != TokenType.KEYWORD and self.current_token.type != TokenType.EOF:
            body.append(self.statement())
        else_body = None
        if self.current_token.type == TokenType.KEYWORD and self.current_token.value == 'else':
            self.advance()
            if self.current_token.type != TokenType.COLON:
                raise Exception("Expected ':' after else")
            self.advance()
            else_body = []
            while self.current_token.type != TokenType.EOF:
                else_body.append(self.statement())
        return IfNode(condition, body, else_body)

    def while_statement(self):
        self.advance()
        condition = self.expr()
        if self.current_token.type != TokenType.COLON:
            raise Exception("Expected ':' after while condition")
        self.advance()
        body = []
        while self.current_token.type != TokenType.EOF:
            body.append(self.statement())
        return WhileNode(condition, body)

    def func_def(self):
        self.advance()
        func_name = self.current_token.value
        self.advance()
        if self.current_token.type != TokenType.LPAREN:
            raise Exception("Expected '(' after function name")
        self.advance()
        params = []
        while self.current_token.type != TokenType.RPAREN:
            params.append(self.current_token.value)
            self.advance()
        self.advance()  # skip ')'
        if self.current_token.type != TokenType.COLON:
            raise Exception("Expected ':' after function header")
        self.advance()
        body = []
        while self.current_token.type != TokenType.EOF:
            body.append(self.statement())
        return FuncDefNode(func_name, params, body)

    def expr(self):
        left = self.term()
        while self.current_token.type == TokenType.OPERATOR and self.current_token.value in ['+', '-']:
            op = self.current_token.value
            self.advance()
            right = self.term()
            left = BinOpNode(left, op, right)
        return left

    def term(self):
        left = self.factor()
        while self.current_token.type == TokenType.OPERATOR and self.current_token.value in ['*', '/', '^']:
            op = self.current_token.value
            self.advance()
            right = self.factor()
            left = BinOpNode(left, op, right)
        return left

    def factor(self):
        token = self.current_token
        if token.type == TokenType.NUMBER:
            self.advance()
            return NumberNode(token.value)
        elif token.type == TokenType.STRING:
            self.advance()
            return StringNode(token.value)
        elif token.type == TokenType.IDENTIFIER:
            self.advance()
            return VarAccessNode(token.value)
        elif token.type == TokenType.LPAREN:
            self.advance()
            expr = self.expr()
            if self.current_token.type == TokenType.RPAREN:
                self.advance()
                return expr
            raise Exception("Expected ')'")
        raise Exception(f"Unexpected token {token}")
