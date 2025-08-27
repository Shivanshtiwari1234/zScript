# nodes.py

class NumberNode:
    def __init__(self, value):
        self.value = value

class StringNode:
    def __init__(self, value):
        self.value = value

class VarAccessNode:
    def __init__(self, var_name):
        self.var_name = var_name

class VarAssignNode:
    def __init__(self, var_name, value_node):
        self.var_name = var_name
        self.value_node = value_node

class BinOpNode:
    def __init__(self, left, op, right):
        self.left = left
        self.op = op
        self.right = right

class PrintNode:
    def __init__(self, expr):
        self.expr = expr

class IfNode:
    def __init__(self, condition, body, else_body=None):
        self.condition = condition
        self.body = body
        self.else_body = else_body

class WhileNode:
    def __init__(self, condition, body):
        self.condition = condition
        self.body = body

class FuncDefNode:
    def __init__(self, name, params, body):
        self.name = name
        self.params = params
        self.body = body

class FuncCallNode:
    def __init__(self, name, args):
        self.name = name
        self.args = args
