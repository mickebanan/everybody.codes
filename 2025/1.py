def part1(names, moves):
    loc = 0
    for move in moves:
        distance = int(move[1:])
        if move[0] == 'L':
            loc = max(0, loc - distance)
        else:
            loc = min(loc + distance, len(names) - 1)
    return names[loc]

def part2(names, moves):
    loc = 0
    for move in moves:
        distance = int(move[1:])
        if move[0] == 'L':
            loc = loc - distance if loc >= distance else len(names) + (loc - distance)
        else:
            loc = (loc + distance) % len(names)
    return names[loc]

def part3(names, moves):
    for move in moves:
        distance = int(move[1:])
        if move[0] == 'L':
            names[0], names[len(names) - distance] = names[len(names) - distance], names[0]
        else:
            names[0], names[distance % len(names)] = names[distance % len(names)], names[0]
    return names[0]

for part, func in ('1', part1), ('2', part2), ('3', part3):
    names, moves = [line.split(',') for line in
                    [line for line in open(f'inputs/1_{part}.txt').read().splitlines() if line]]
    print(f'part {part}: {func(names, moves)}')
