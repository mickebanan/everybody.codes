def make_wheel(data):
    wheel = [1]
    left = []
    for i, (start, stop) in enumerate(data):
        if i % 2 == 0:
            wheel.extend(list(range(start, stop + 1)))
        else:
            left.extend(list(range(start, stop + 1)))
    return wheel + list(reversed(left))

data = list(map(int, open('inputs/13_1.txt').read().split('\n')))
wheel = [1]
for i, value in enumerate(data):
    if i % 2 == 0:
        wheel.append(value)
    else:
        wheel.insert(0, value)
print('part 1:', wheel[(wheel.index(1) + 2025) % len(wheel)])

data = [map(int, d.split('-')) for d in open('inputs/13_2.txt').read().split('\n')]
wheel = make_wheel(data)
print('part 2:', wheel[20252025 % len(wheel)])

data = [map(int, d.split('-')) for d in open('inputs/13_3.txt').read().split('\n')]
wheel = make_wheel(data)  # ~10s with pypy3
print('part 3:', wheel[202520252025 % len(wheel)])