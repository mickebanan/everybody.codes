def get_moves(y, x, ymax, xmax):
    for dy, dx in {(-1, 0), (1, 0), (0, -1), (0, 1)}:
        if 0 <= y + dy < ymax and 0 <= x + dx < xmax:
            yield y + dy, x + dx

def dfs(start, ymax, xmax, skip):
    visited = set()
    q = start
    while q:
        y, x = q.pop()
        visited.add((y, x))
        for yy, xx in get_moves(y, x, ymax, xmax):
            if (yy, xx) not in visited and int(data[yy][xx]) <= int(data[y][x]) and (yy, xx) not in skip:
                q.append((yy, xx))
    return visited

data = open('inputs/12_1.txt').read().split('\n')
print('part 1:', len(dfs([(0, 0)], len(data), len(data[0]), set())))

data = open('inputs/12_2.txt').read().split('\n')
ymax, xmax = len(data), len(data[0])
print('part 2:', len(dfs([(0, 0), (ymax - 1, xmax - 1)], ymax, xmax, set())))

data = open('inputs/12_3.txt').read().split('\n')
ymax, xmax = len(data), len(data[0])
skip = set()
barrels = 0
for _ in range(3):
    results = {}
    for y in range(ymax):
        for x in range(xmax):
            results[(y, x)] = list(dfs([(y, x)], ymax, xmax, skip))
    k, v = sorted(results.items(), key=lambda x: len(x[1]))[-1]
    barrels += len(v)
    skip |= set(v)
print('part 3:', barrels)