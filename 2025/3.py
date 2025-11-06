data = [int(a) for a in open('inputs/3_1.txt').read().split(',')]
print('part 1:', sum(set(data)))

data = [int(a) for a in open('inputs/3_2.txt').read().split(',')]
print('part 2:', sum(sorted(set(data))[:20]))

data = [int(a) for a in open('inputs/3_3.txt').read().split(',')]
bins = []
for a in sorted(data, reverse=True):
    for b in bins:
        if a < b[-1]:
            b.append(a)
            break
    else:
        bins.append([a])
print('part 3:', len(bins))
