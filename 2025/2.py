import itertools
import re


class Complex:
    value = None

    def __init__(self, real, imag):
        self.value = (real, imag)

    def __add__(self, other):
        return Complex(self.value[0] + other[0], self.value[1] + other[1])

    def __mul__(self, other):
        real = self.value[0] * other[0] - self.value[1] * other[1]
        imag = self.value[0] * other[1] + self.value[1] * other[0]
        return Complex(real, imag)

    def __truediv__(self, other):
        real = int(self.value[0] / other[0])
        imag = int(self.value[1] / other[1])
        return Complex(real, imag)

    def __getitem__(self, item):
        return self.value[item]

    def __str__(self):
        return f'Complex({self.value[0]}, {self.value[1]})'

part1 = open('inputs/2_1.txt').read()
m = re.search(r'([0-9-]+),([0-9-]+)', part1)
for name, a in ('test', Complex(25, 9)), ('1', Complex(int(m.group(1)), int(m.group(2)))):
    r = Complex(0, 0)
    for _ in range(3):
        r *= r
        r /= Complex(10, 10)
        r += a
    print(f'part {name}: [{r[0]},{r[1]}]')

part2 = open('inputs/2_2.txt').read()
m = re.search(r'([0-9-]+),([0-9-]+)', part2)
start = Complex(int(m.group(1)), int(m.group(2)))

def work(pos):
    r = Complex(0, 0)
    for i in range(100):
        r *= r
        r /= Complex(100_000, 100_000)
        r += pos
        if abs(r[0]) > 1_000_000 or abs(r[1]) > 1_000_000:
            return False
    return r

for name, d, length in (('part 2', 10, 101), ('part 3', 1, 1001)):
    c = 0
    for row, col in itertools.product(range(length), range(length)):
        pos = start + Complex(col * d, row * d)
        if work(pos):
            c += 1
    print('%s %s' % (name, c))