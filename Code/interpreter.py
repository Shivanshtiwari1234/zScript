# interpreter.py
from nodes import *

class Interpreter:
    def __init__(self):
        self.variables = {}

    def interpret(self, statements):
        for stmt in statements:
            self.execute(stmt)

    def execute(self, node):
        if isinstance(node, VarAssignNode):
            value = self.eval(node.value_node)
            self.variables[node.var_name] = value
        elif isinstance(node, VarAccessNode):
            return self.variables.get(node.var_name, None)
        elif isinstance(node, PrintNode):
            print(self.eval(node.expr))
        elif isinstance(node, BinOpNode):
            return self.eval(node)
        elif isinstance(node, NumberNode):
            return node.value
        elif isinstance(node, StringNode):
            return node.value
        elif isinstance(node, IfNode):
            if self.eval(node.condition):
                for stmt in node.body:
                    self.execute(stmt)
            elif node.else_body:
                for stmt in node.else_body:
                    self.execute(stmt)
        elif isinstance(node, WhileNode):
            while self.eval(node.condition):
                for stmt in node.body:
                    self.execute(stmt)

    def eval(self, node):
        if isinstance(node, BinOpNode):
            left = self.eval(node.left)
            right = self.eval(node.right)
            if node.op == '+': return left + right
            if node.op == '-': return left - right
            if node.op == '*': return left * right
            if node.op == '/': return left / right
            if node.op == '^': return left ** right
        elif isinstance(node, NumberNode):
            return node.value
        elif isinstance(node, StringNode):
            return node.value
        elif isinstance(node, VarAccessNode):
            return self.variables.get(node.var_name, None)
        return None
