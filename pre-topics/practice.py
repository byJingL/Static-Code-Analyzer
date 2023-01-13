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