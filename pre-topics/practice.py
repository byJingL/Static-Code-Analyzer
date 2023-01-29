# ------------------ String order --------------- #
print('a' > 'b')
print('Ab' < 'a') # True

# ------------------ List sorting --------------- #
# Toby Marinet Chubby Kitty -> ['Toby', 'Kitty', 'Chubby', 'Marinet']
s = 'Toby Marinet Chubby Kitty'
toys = s.split()
# whitch sort is first
toys.sort()
toys.sort(key=len)
print(toys)

a = '1234567\n'
print(a[:-1])

# ------------------ Copy of an object --------------- #
l = [2, 4, 5]
l_copy = l
l.append(9)
print(l_copy) # [2, 4, 5, 9]

import copy

old = [3, 7, 9]
old_2 = copy.copy(old)
old.append(12)
print(old_2)

menu = {
   'breakfast': ['porridge'],
   'lunch': ['soup', 'main course', 'compote'],
   'dinner': ['main course', 'dessert', 'tea'],
}
copy_menu = menu.copy()
# a new container is created:
print(id(menu), id(copy_menu)) # 4353003592 4353042040
# but the stored values are the same
print(id(menu['lunch']), id(copy_menu['lunch']))

lst = [[5], [2,3,9]]
new_lst = lst.copy()
lst[1][0] = 10
print(new_lst)

lst = [[5], [2, 3, 9]]
new_lst = copy.deepcopy(lst)
lst[0].append(5)
print(lst)
print(new_lst)


classmates = ['Marco', 'James', 'Jane', 'Dan']
cinema = classmates
swimming = copy.copy(classmates)
cinema.append('Bob')
swimming.append('Kate')
# classmates = ['Marco', 'James', 'Jane', 'Dan', 'Bob']
# cinema = ['Marco', 'James', 'Jane', 'Dan', 'Bob']
# swimming = ['Marco', 'James', 'Jane', 'Dan', 'Kate']
print(classmates)
print(cinema)
print(swimming)

# ------------------ Regex, re module --------------- #
import re

print('======== Regex part ========')


regexp = r'hello'
result = re.match(regexp, 'hello, Jane')
print(result) # <re.Match object; span=(0, 5), match='hello'>
print(result is None) # False
print(bool(result)) # True

print(re.match(regexp, 'a hello, Jane')) # None

print(bool(re.match('Where.?.?.? my mind.', "Where's my mind?"))) # True
print(bool(re.match(r'Where.?.?.? my mind.', "Where's my mind?"))) # True

print(r'\n')

string = 'Backslash?'
string = re.escape(string)

# ------------------ Regex, Shorthands --------------- #
print(re.match('\w', 'X'))
print(re.match('\\w', 'X'))
print(re.match(r'\w', 'X'))

print(r'\\w', r'\w')
print(re.match(r'\\w', r'\w'))

print('ha\bppy') # hppy
print(r'\b') # \b

# boundary shorthand
print(re.match(r'hair\b', 'hair')) # match
print(re.match(r'hair\b', 'hair style')) # match
print(re.match(r'hair\b', 'haircut')) # None, no match
print(re.match(r'hair\b', 'hair\n')) # match
print(re.match(r'hair\b', 'hair \n')) # match

print(re.match(r'hair\B', 'hair')) # None, no match
print(re.match(r'hair\B', 'hair style')) # None, no match
print(re.match(r'hair\B', 'haircut')) # match
print(re.match(r'hair\B', 'hair\n')) # None, no match
print(re.match(r'hair\B', 'hair \n')) # None, no match

print(re.match('\Ahair', 'haircut')) # match
print(re.match('\Ahair', 'hair style')) # match
print(re.match('\Ahair', 'long hair')) # not match
print(re.match('\Ahair', 'brownhair')) # not match

print(re.match('hair\Z', 'hair')) # match
print(re.match('hair\Z', 'hair style')) #not match
print(re.match('hair\Z', 'haircut')) #not match
print(re.match('hair\Z', 'long hair')) #not match

print(re.match("^Bring cash", "Bring cash$")) # match
print(re.match("^Bring cash", "^Bring cash$")) # not match
print(re.match("^Bring cash", "A Bring cash$")) # not match
print(re.match("Bring cash", "Bring cash$")) # match the start by default

print(re.match("h?ello", 'yello'))

# ------------------ ast module --------------- #
print('===========ast=============')
# parse and dump
import ast
expression = '1 + 2'
tree = ast.parse(expression)
print(ast.dump(tree))
"""
Module(
	body=[
		Expr(
			value=BinOp(
				left=Constant(value=1), 
				op=Add(), 
				right=Constant(value=2)
        	),
        ),
    ], 
   type_ignores=[],
)
"""
# walk
nodes = ast.walk(tree)
for node in nodes:
   print(node)
# <ast.Module object at 0x1006584c0>
# <ast.Expr object at 0x100658550>
# <ast.BinOp object at 0x100658b20>
# <ast.Constant object at 0x10065b3a0>
# <ast.Add object at 0x100728c40>
# <ast.Constant object at 0x10065b6a0>

# node_visitor
class BinOpLister(ast.NodeVisitor):
	def visit_BinOp(self, node):
		print(node.left)
		print(node.op)
		print(node.right)
		self.generic_visit(node)
BinOpLister().visit(tree)

# literal evaluate
user_input = '15'
print(type(user_input))  # <class 'str'>
check_user_input = ast.literal_eval(user_input)
print(type(check_user_input))  # <class 'int'>


# lineno and end_lineno
with open('pre-topics/calculation.py') as file:
	data = file.read()
	print(type(data))
	tree = ast.parse(data)

for n in tree.body:
	print(n, n.lineno, n.end_lineno)

# <ast.Assign object at 0x104f03fa0> 1 1
# <ast.Assign object at 0x104f03f40> 2 2
# <ast.Assign object at 0x104f404c0> 3 3
# <ast.Expr object at 0x104f403d0> 4 4