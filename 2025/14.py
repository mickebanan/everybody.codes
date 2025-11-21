import itertools

def count_active(data):
    return sum(row.count('#') for row in data)

def work(data, rounds, pattern=None):
    def move(y, x):
        for dy, dx in ((-1, -1), (-1, 1), (1, -1), (1, 1)):
            if 0 <= y + dy < ymax and 0 <= x + dx < xmax:
                yield y + dy, x + dx

    def match(pattern):
        for y in range(len(pattern)):
            for x in range(len(pattern[0])):
                if pattern[y][x] != data[y + 13][x + 13]:
                    return False
        return True

    ymax, xmax = len(data), len(data[0])
    sums = {'p12': 0, 'p3': 0}
    part_3 = []
    i = 0
    diffs = []
    done = False
    while i < rounds:
        _data = []
        for y in range(ymax):
            row = ''
            for x in range(xmax):
                odd = count_active(data[yy][xx] for yy, xx in move(y, x)) % 2 != 0
                row += '#' if data[y][x] == '#' and odd or data[y][x] == '.' and not odd else '.'
            _data.append(row)
        data = _data
        sums['p12'] += count_active(_data)
        if pattern:
            matches = match(pattern)
            if matches:
                part_3.append(i)
                c = count_active(_data)
                sums['p3'] += c
                if len(part_3) >= 2:
                    diff = (part_3[-1] - part_3[-2], c)
                    if diff not in diffs:
                        diffs.append((part_3[-1] - part_3[-2], c))
                    else:
                        done = True
                if done:
                    diff_cycle = itertools.cycle(d[0] for d in diffs)
                    count_cycle = itertools.cycle(d[1] for d in diffs)
                    next(diff_cycle)  # We already counted the first one above
                    next(count_cycle)
                    while i < rounds:
                        i += next(diff_cycle)
                        if i < rounds:
                            sums['p3'] += next(count_cycle)
                    return sums
        i += 1
    return sums

data = open('inputs/14_1.txt').read().split('\n')
print('part 1:', work(data, 10)['p12'])

data = open('inputs/14_2.txt').read().split('\n')
print('part 2:', work(data, 2025)['p12'])

data = ['.' * 34] * 34
pattern = open('inputs/14_3.txt').read().split('\n')
print('part 3:', work(data, 1_000_000_000, pattern=pattern)['p3'])
