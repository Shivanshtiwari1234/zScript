ZScript++ – A Scalable Programming Language

ZScript++ is a modular, beginner-friendly programming language implemented in Python with a Lexer → Parser → AST → Interpreter architecture, designed for scalability and easy contribution.

Features

✅ Python-like syntax (easy for beginners)
✅ Modular architecture – Lexer, Parser, AST, Interpreter in separate files
✅ Core language constructs:

Variables: let x = 10

Print & Input:

print("Hello")
name = input("Enter your name: ")


Arithmetic & Boolean ops: + - * / ^, and or not

Conditionals:

if x > 5:
    print("Big")
else:
    print("Small")


Loops:

while x < 10:
    x = x + 1


Functions:

function greet(name):
    print("Hello " + name)
greet("ZScript")


✅ Error Handling with descriptive messages & line numbers
✅ REPL & File Execution modes
✅ Easily extendable for future features (lists, dictionaries, classes, modules)

Architecture
zscript/
│
├── main.py           # Entry point (CLI / REPL)
├── lexer.py          # Tokenizer
├── parser.py         # AST Builder
├── interpreter.py    # Executes the AST
├── tokens.py         # Token definitions
├── nodes.py          # AST Node classes
├── errors.py         # Error handling
└── README.md         # Documentation

Installation

Requires Python 3.8+
Clone the repo:

git clone https://github.com/yourusername/zscript.git
cd zscript


Install dependencies:

pip install -r requirements.txt


(Currently uses Colorama for colored output.)

How to Run

Run a script:

python main.py examples/hello.zs


Start REPL:

python main.py

Example Program
// This is a comment
let x = 5
let y = 10

if x < y:
    print("x is smaller")

function add(a, b):
    return a + b

print(add(x, y))

while x < 10:
    x = x + 1
    print(x)

Error System

ZScript++ reports errors with type, message, and line number:

[Error: SyntaxError] Unexpected token 'end' at line 4

Roadmap

✅ v1: Core syntax, loops, conditionals, functions

🔜 v2: Strings, lists, dictionaries, built-in functions

🔜 v3: Comments, file I/O, modules, REPL enhancements

🔜 Future: JIT compilation, multi-threading support

Contributing

Fork the repo

Create a new branch:

git checkout -b feature-new


Commit changes and push:

git push origin feature-new


Open a Pull Request

License

Licensed under Apache 2.0. See LICENSE
 for details.

✅ TL;DR:

ZScript++ = Simple syntax + Scalable architecture + Future-ready language.