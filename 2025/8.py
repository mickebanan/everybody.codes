import collections
import itertools

data = list(map(int, open('inputs/8_1.txt').read().split(',')))
s = 0
for n0, n1 in itertools.pairwise(data):
    if max(n0, n1) - min(n0, n1) == max(data) / 2:
        s += 1
print('part 1:', s)


def get_pairs_and_intersections(data):
    pairs = []
    s = 0
    for a, b in sorted(tuple(sorted(p)) for p in itertools.pairwise(data)):
        s += sum(1 for p0, p1 in pairs if p0 < a < p1 < b)
        pairs.append((a, b))
    return {'pairs': pairs, 'intersections': s}
data = list(map(int, open('inputs/8_2.txt').read().split(',')))
print('part 2:', get_pairs_and_intersections(data)['intersections'])

data = list(map(int, open('inputs/8_3.txt').read().split(',')))
nails = 256
pairs = get_pairs_and_intersections(data)['pairs']
counts = collections.Counter()
for c0, c1 in list(sorted(itertools.combinations(range(1, nails + 1), 2))):
    for p0, p1 in pairs:
        if p0 < c0 < p1 < c1 or c0 < p0 < c1 < p1 or (p0, p1) == (c0, c1):
            counts[(c0, c1)] += 1
print('part 3:', counts.most_common(1)[0][-1])