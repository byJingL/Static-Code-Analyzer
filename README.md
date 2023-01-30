# Static-Code-Analyzer
This program can check code format of Python files meets the standards and recommendations according to PEP8.
## Main Skill
re module, ast module, regexp, AST, argparse module, docstrings  
## Theory
All python code format issues included below are checked by two methods:  
1. Read the file line by line as list of strings, check them one by one using regular expression (regex) and re module.
2. Parse the file as a Abstract Syntax Tree, check it node by node using ast module.  

Code issues covered:  
- S001: Too long
- S002: Indentation is not a multiple of four 
- S003: Unnecessary semicolon after a statement
- S004: Less than two spaces before inline comments
- S005: TODO found
- S006: More than two blank lines preceding a code line
- S007: Too many spaces after construction_name (def or class)
- S008: Class name class_name should be written in CamelCase
- S009: Function name function_name should be written in snake_case
- S010: Argument name arg_name should be written in snake_case
- S011: Variable var_name should be written in snake_case
- S012: The default argument value is mutable.

## How to use
- Download [code_analyzer.py](/code_analyzer.py)
- Run [code_analyzer.py](/code_analyzer.py) with argument of which folder or file you want to check. e.g. 
  ```
  python3 code_analyzer.py root_folder
  ```
  ```
  python3 code_analyzer.py folder/main.py
  ```
- All the code format issues in the given folder or the given file will be listed.
- Attention: only `.py` file will be checked.

## Example
Example python file:
```
class  Person:
    pass

class user:

    def __init__(self, login: str, password: str):
        self.login = login
        self.password = password

    @staticmethod
    def _print1():
        print('q')

    @staticmethod
    def Print2():
        print('q')

CONSTANT = 10
names = ['John', 'Lora', 'Paul']


def fun1(S=5, test=[]):  # default argument value is mutable
    VARIABLE = 10
    string = 'string'
    print(VARIABLE)
```
Expected output:
```
/path/to/file/script.py: Line 1: S007 Too many spaces after 'class'
/path/to/file/script.py: Line 4: S008 Class name 'user' should use CamelCase
/path/to/file/script.py: Line 15: S009 Function name 'Print2' should use snake_case
/path/to/file/script.py: Line 19: S010 Argument name 'S' should be snake_case
/path/to/file/script.py: Line 19: S012 Default argument value is mutable
/path/to/file/script.py: Line 20: S011 Variable 'VARIABLE' in function should be snake_case
```

## Disclaimer
The original learning materials and project ideas are from [JetBrains Academy](https://www.jetbrains.com/academy/). All codes were written by myself.