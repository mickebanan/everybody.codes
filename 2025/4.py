import math

data = open('inputs/4_1.txt').readlines()
a, b = int(data[0]), int(data[-1])
print('part 1:', math.floor(2025 * a / b))

data = open('inputs/4_2.txt').readlines()
a, b = int(data[0]), int(data[-1])
print('part 2:', math.ceil(10000000000000 / (a / b)))

data = open('inputs/4_3.txt').readlines()
a, data, b = int(data[0]), data[1:-1], int(data[-1])
for d in data:
    x, y = map(int, d.split('|'))
    a = a / x * y
print('part 3:', math.floor(a / b * 100))