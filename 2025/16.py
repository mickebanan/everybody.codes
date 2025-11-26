from math import prod

def get_blocks(data, length):
    return sum(length // n for n in data)

def get_factors(data):
    factors = []
    step = 1
    while sum(data) > 0:
        is_factor = True
        indexes = []
        for i in range(step - 1, len(data), step):
            indexes.append(i)
            if not data[i]:
                is_factor = False
                break
        if is_factor:
            factors.append(step)
            for i in indexes:
                data[i] -= 1 if data[i] else 0
        step += 1
    return factors

data = map(int, open('inputs/16_1.txt').read().split(','))
print('part 1:', get_blocks(data, 90))

data = list(map(int, open('inputs/16_2.txt').read().split(',')))
print('part 2:', prod(get_factors(data)))

data = list(map(int, open('inputs/16_3.txt').read().split(',')))
factors = get_factors(data)
lo, hi = 0, 2
target = 202520252025000
while True:  # Determine ceiling
    v = get_blocks(factors, hi)
    if v < target:
        hi = hi ** 2
    else:
        break
prev = None
while True:  # Binary search to find the highest result < target
    mid = (lo + hi) // 2
    v = get_blocks(factors, mid)
    if prev and v == prev:
        print('part 3:', mid)
        break
    if v > target:
        hi = mid - 1
    elif v < target:
        lo = mid + 1
    prev = v