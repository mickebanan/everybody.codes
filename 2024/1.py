import collections
import itertools

cost = {'A': 0, 'B': 1, 'C': 3, 'D': 5, 'x': 0}
data = open('inputs/1_1.txt').read()
c = collections.Counter(data)
print('part 1:', sum(cost[k] * v for k, v in c.items()))

data = open('inputs/1_2.txt').read()
s = 0
for batch in itertools.batched(data, 2):
    c = collections.Counter(batch)
    s += sum(cost[k] * v for k, v in c.items()) + (2 if 'x' not in c else 0)
print('part 2:', s)

data = open('inputs/1_3.txt').read()
s = 0
for batch in itertools.batched(data, 3):
    c = collections.Counter(batch)
    s += sum(cost[k] * v for k, v in c.items()) + (6 if 'x' not in c else 2 if c['x'] == 1 else 0)
print('part 3:', s)
