import colorama
colorama.init()
print(colorama.Fore.RED)

class ZScriptError(Exception):
    """Base class for all zScript errors."""
    pass

class SyntaxErrorZ(ZScriptError):
    """Raised when a syntax error occurs in zScript."""
    def __init__(self, message, line_num=None, code_line=None):
        self.message = message
        self.line_num = line_num
        self.code_line = code_line
        super().__init__(self.message)

class RuntimeErrorZ(ZScriptError):
    """Raised when a runtime error occurs in zScript."""
    def __init__(self, message, line_num=None, code_line=None):
        self.message = message
        self.line_num = line_num
        self.code_line = code_line
        super().__init__(self.message)

class NameErrorZ(ZScriptError):
    """Raised when an undefined variable is accessed."""
    def __init__(self, var_name, line_num=None, code_line=None):
        self.var_name = var_name
        self.message = f"Undefined variable: '{var_name}'"
        self.line_num = line_num
        self.code_line = code_line
        super().__init__(self.message)

class FunctionErrorZ(ZScriptError):
    """Raised when there is an issue with function definition or call."""
    def __init__(self, message, line_num=None, code_line=None):
        self.message = message
        self.line_num = line_num
        self.code_line = code_line
        super().__init__(self.message)
