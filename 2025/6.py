letters = {'a': 'A', 'b': 'B', 'c': 'C'}
data = open('inputs/6_1.txt').read()
s = sum(data[:i].count('A') if c == 'a' else 0 for i, c in enumerate(data))
print('part 1:', s)

data = open('inputs/6_2.txt').read()
s = sum(data[:i].count(letters[c]) if c in letters else 0 for i, c in enumerate(data))
print('part 2:', s)

data = open('inputs/6_3.txt').read() * 1000
s = sum(data[max(0, i - 1000):min(len(data), i + 1000 + 1)].count(letters[c]) if c in letters else 0
        for i, c in enumerate(data))
print('part 3:', s)
