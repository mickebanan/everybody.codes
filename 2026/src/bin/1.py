d = [int(v) for v in open(r'../../data/1-1.dat').readline().split(',')]
squares = [v * v for v in range(1, max(d))]
print('part 1:', sum(next(v - pc for v in squares if pc <= v) for pc in d))

d = [int(v) for v in open(r'../../data/1-2.dat').readline().split(',')]
squares = {v: v * v for v in range(1, max(d))}
frames = [v * v - squares[v-2] for v in range(3, max(d))]
print('part 2:', sum(next(v - pc for v in frames if pc <= v) for pc in d))

d = [int(v) for v in open(r'../../data/1-3.dat').readline().split(',')]
squares = {v: v * v for v in range(1, max(d))}
outposts = [v - 1 for k, v in squares.items() if k % 2 != 0]
print('part 3:', sum(next(v - pc for v in outposts if pc <= v) for pc in d))
