class Bone:
    left = None
    right = None

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return ''.join((str(self.left or ''), str(self.value), str(self.right or '')))


def fishbone(data):
    bones = []
    for a in data:
        for bone in bones:
            if a < bone.value and not bone.left:
                bone.left = a
                break
            elif a > bone.value and not bone.right:
                bone.right = a
                break
        else:
            bones.append(Bone(a))
    return bones


data = open('inputs/5_1.txt').read()
data = map(int, data.split(':')[1].split(','))
print('part 1:', ''.join(str(bone.value) for bone in fishbone(data)))

data = open('inputs/5_2.txt').readlines()
values = []
for row in data:
    row = map(int, row.split(':')[1].split(','))
    values.append(int(''.join(str(bone.value) for bone in fishbone(row))))
print('part 2:', max(values) - min(values))

data = open('inputs/5_3.txt').readlines()
values = []
for row in data:
    id_, vals = row.split(':')
    values.append((id_, fishbone(map(int, vals.split(',')))))

def sort(value):
    id_, bone = value
    return (int(''.join(str(b.value) for b in bone)),) + tuple((int(''.join(str(b))),) for b in bone) + (int(id_),)
print('part 3:', sum(i * int(id_) for i, (id_, _) in enumerate(sorted(values, key=sort, reverse=True), start=1)))