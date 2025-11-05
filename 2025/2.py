import itertools
import re


class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.imag * other.imag,
                       self.real * other.imag + self.imag * other.real)

    def __truediv__(self, other):
        return Complex(int(self.real / other.real),
                       int(self.imag / other.imag))

    def check(self, n, div):
        r = Complex(0, 0)
        for _ in range(n):
            r *= r
            r /= Complex(div, div)
            r += self
            if abs(r.real) > 1_000_000 or abs(r.imag) > 1_000_000:
                return False
        return r


part1 = open('inputs/2_1.txt').read()
m = re.search(r'([0-9-]+),([0-9-]+)', part1)
for name, a in (('test', Complex(25, 9)),
                ('1', Complex(int(m.group(1)), int(m.group(2))))):
    a = a.check(3, 10)
    print(f'part {name}: [{a.real},{a.imag}]')

part2 = open('inputs/2_2.txt').read()
m = re.search(r'([0-9-]+),([0-9-]+)', part2)
start = Complex(int(m.group(1)), int(m.group(2)))
for name, d, length in (('part 2', 10, 101),
                        ('part 3', 1, 1001)):
    c = 0
    for row, col in itertools.product(range(length), range(length)):
        pos = start + Complex(col * d, row * d)
        if pos.check(100, 100_000):
            c += 1
    print('%s: %s' % (name, c))