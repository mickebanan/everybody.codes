import itertools

def check_similarity(row1, row2):
    return sum(1 for i, c in enumerate(row1) if c == row2[i])

def get_relationships(data):
    def is_compatible(c, p1, p2):
        for i, x in enumerate(c):
            if x != p1[i] and x != p2[i]:
                return False
        return True

    relationships = {}
    for id1, row in data.items():
        rest = {id_: dna for id_, dna in data.items() if id_ != id1}
        for (id2, row2), (id3, row3) in itertools.combinations(rest.items(), 2):
            if is_compatible(row, row2, row3):
                relationships[id1] = (id2, id3)
    return list(relationships.items())

data = dict(row.split(':') for row in open('inputs/9_1.txt').read().split('\n'))
c, (p1, p2) = get_relationships(data)[0]
print('part 1:', check_similarity(data[c], data[p1]) * check_similarity(data[c], data[p2]))

data = dict(row.split(':') for row in open('inputs/9_2.txt').read().split('\n'))
s = sum(check_similarity(data[c], data[p1]) * check_similarity(data[c], data[p2])
        for c, (p1, p2) in get_relationships(data))
print('part 2:', s)

data = dict(row.split(':') for row in open('inputs/9_3.txt').read().split('\n'))
relationships = get_relationships(data)
graph = {id_: set() for id_ in data}
for c, (p1, p2) in relationships:
    graph[c] |= {p1, p2}
    graph[p1].add(c)
    graph[p2].add(c)
visited = set()
families = []
for id1 in data:
    if id1 not in visited:
        family = set()
        q = [id1]
        while q:
            x = q.pop(0)
            if x in visited:
                continue
            visited.add(x)
            family.add(x)
            q.extend(graph[x])
        families.append(family)
print('part 3:', sum(int(a) for a in sorted(families, key=len, reverse=True)[0]))
