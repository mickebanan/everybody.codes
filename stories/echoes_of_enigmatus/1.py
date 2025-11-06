data = """
A=3657 B=3583 C=9716 X=903056852 Y=9283895500 Z=85920867478 M=188
A=6061 B=4425 C=5082 X=731145782 Y=1550090416 Z=87586428967 M=107
A=7818 B=5395 C=9975 X=122388873 Y=4093041057 Z=58606045432 M=102
A=7681 B=9603 C=5681 X=716116871 Y=6421884967 Z=66298999264 M=196
A=7334 B=9016 C=8524 X=297284338 Y=1565962337 Z=86750102612 M=145
""".strip().splitlines()

def eni(n, exp, mod, part=1):
    result = []
    if part == 1:
        for i in range(1, exp + 1):
            result.append(str(pow(n, i, mod)))
        result = reversed(result)
    else:
        for i in range(5):
            result.append(str(pow(n, exp - i, mod)))
    return int(''.join(result))

data = open('inputs/1_1.txt').readlines()
p1 = 0
for row in data:
    a, b, c, x, y, z, m = [int(a.split('=')[-1]) for a in row.split()]
    value = eni(a, x, m) + eni(b, y, m) + eni(c, z, m)
    p1 = max(p1, value)
print('part 1:', p1)

data = open('inputs/1_2.txt').readlines()
p2 = 0
for row in data:
    a, b, c, x, y, z, m = [int(a.split('=')[-1]) for a in row.split()]
    value = eni(a, x, m, part=2) + eni(b, y, m, part=2) + eni(c, z, m, part=2)
    p2 = max(p2, value)
print('part 2:', p2)
