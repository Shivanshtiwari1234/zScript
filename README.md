# zScript Interpreter

A simple beginner-friendly programming language called **zScript** implemented in Python.

## Features
- Python-like syntax (beginner-friendly)
- Commands:
  - `print("Hello")` – prints text or evaluated expressions
  - `input("Enter:")` – takes user input
  - `global x = 10` – declare a global variable
  - `local y = 5` – declare a local variable
- Arithmetic operations: `+`, `-`, `*`, `/`, `^` (for exponentiation)
- Comments: `// comment`
- Functions:
  ```
  function greet():
      print("Hello")
  ```
- Infinite loop:
  ```
  forever:
      print("Running")
  ```
- Error handling with colored output (uses Colorama):
  - Red error messages with line number and error type

## Requirements
- Python 3.8+
- Install Colorama:
```
pip install colorama
```

## How to Run
1. Save the interpreter as `zscript.py`.
2. Create a `.zs` file (example: `test.zs`) with your zScript code.
3. Run:
```
python zscript.py test.zs
```

## Example Program (`test.zs`)
```
// This is a comment
global x = 10
local y = 5
print(x + y)

function greet():
    print("Welcome to zScript!")

greet()

forever:
    print("Looping...")
```

## Error System
- If an invalid line is found, zScript shows:
```
Error in line X: <code> (ErrorType)
```

## License
Licensed under the **Apache License 2.0**. See [LICENSE](LICENSE) for details.

## Future Improvements
- Add conditionals (`if`, `else`)
- Add `return` in functions
- Add file I/O
- Add REPL mode

---
Enjoy coding with **zScript**!
