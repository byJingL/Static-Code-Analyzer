import ast

# ast nodes and exmple
with open('pre-topics/my_func.py') as file:
	data = file.read()
	tree = ast.parse(data)
# The structure of the tree can be seen in ast_exmple.JPG
print(ast.dump(tree))

print(tree.body)

for node in tree.body:
    if isinstance(node, ast.Import):
        for alias in node.names:
            print(alias.name)

for node in ast.walk(tree):
    if isinstance(node, ast.FunctionDef):
        for default in node.args.defaults:
            print(default)


fuction1 = tree.body[2]
fuction2 = tree.body[3]
print(fuction1)
print(fuction2.name)
args = [arg.arg for arg in fuction1.args.args]
print(args)
