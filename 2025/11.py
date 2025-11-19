def work(data, part=None):
    def phase1(data):
        rounds = 0
        while True:
            moving = False
            for i, (a, b) in enumerate(zip(data, data[1:])):
                if a > b:
                    data[i], data[i+1] = data[i] - 1, data[i+1] + 1
                    moving = True
            if not moving:
                break
            rounds += 1
        return rounds
    if part == 1:
        rounds = phase1(data)
        while True:
            moving = False
            for i, (a, b) in enumerate(zip(data, data[1:])):
                if a < b:
                    data[i + 1], data[i] = data[i + 1] - 1, data[i] + 1
                    moving = True
            if not moving:
                break
            rounds += 1
            if rounds == 10:
                return sum(i * n for i, n in enumerate(data, start=1))
    else:
        rounds = phase1(data)
        m = sum(data) // len(data)
        rounds += sum(a - m for a in data if a > m)
    return rounds

data = list(map(int, open('inputs/11_1.txt').read().strip().split('\n')))
print('part 1:', work(data, part=1))

data = list(map(int, open('inputs/11_2.txt').read().strip().split('\n')))
print('part 2:', work(data))

data = list(map(int, open('inputs/11_3.txt').read().strip().split('\n')))
print('part 3:', work(data))
