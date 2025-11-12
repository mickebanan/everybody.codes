def get_input(fn):
    names, rules = open(f'inputs/{fn}.txt').read().split('\n\n')
    return names.split(','), get_rules(rules)

def get_rules(prod_rules):
    rules = {}
    for p in prod_rules.split('\n'):
        a, b = p.split(' > ')
        rules[a] = b.split(',')
    return rules

def get_valid_names(names, rules):
    valid, s = [], 0
    for i, name in enumerate(names, start=1):
        exists = True
        for c0, c1 in zip(name, name[1:]):
            if not exists:
                break
            if c0 not in rules or c1 not in rules[c0]:
                exists = False
        if exists:
            valid.append(name)
            s += i
    return {'valid': valid, 'sum': s}

def generate_names(name, rules):
    if name[-1] in rules:
        for letter in rules[name[-1]]:
            if 7 <= len(name + letter) <= 11:
                yield name + letter
            if len(name + letter) < 11:
                yield from generate_names(name + letter, rules)


names, rules = get_input('7_1')
print('part 1:', get_valid_names(names, rules)['valid'][0])

names, rules = get_input('7_2')
print('part 2:', get_valid_names(names, rules)['sum'])

names, rules = get_input('7_3')
print('part 3:', len({n for name in get_valid_names(names, rules)['valid'] for n in generate_names(name, rules)}))