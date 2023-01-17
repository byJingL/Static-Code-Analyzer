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
