Code_dict = {
    'S001': 'Too long',
}

file_path = input()
with open(file_path, 'r') as file:
    data = file.read().split('\n')

warnings = []
for i in range(len(data)):
    if len(data[i]) > 79:
        warnings.append(f"Line {i + 1}: S001 {Code_dict['S001']}")

for info in warnings:
    print(info)