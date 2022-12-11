import math
class Monkey:
    def __init__(self):
        self.items = []
        self.operation = None
        self.test = None
        self.on_false = None
        self.on_true = None
        self.count = 0

    def __str__(self):
        return f'Monkey({self.items}, {self.operation}, {self.test}, {self.on_true}, {self.on_false})'

def solve(part=1):
    monkeys = []
    with open('input-11.txt') as f:

        for line in f.readlines():
            line = line.strip()

            if line.startswith("Monkey"):
                m = Monkey()
            if line.startswith('Starting items:'):
                _, items = line.split(': ')
                m.items = list(map(int, items.split(', ')))

            if line.startswith("Operation:"):
                _, operation = line.split('Operation: ')
                _, m.operation = operation.split('new = ')
                # m.operation = compile(m.operation)

            if line.startswith("Test:"):
                _, test = line.split('divisible by ')
                m.test = int(test)

            if line.startswith("If true:"):
                _, on_true = line.split('throw to monkey ')
                m.on_true = int(on_true)

            if line.startswith("If false:"):
                _, on_false = line.split('throw to monkey ')
                m.on_false = int(on_false)

            if not line:
                monkeys.append(m)

    monkeys.append(m)


    N = math.lcm(*[m.test for m in monkeys])
    for round in range(20 if part == 1 else 10000):
        for i, m in enumerate(monkeys):
            m = monkeys[i]
            for item in m.items:
                worry = eval(m.operation, {'old': item})
                if part == 1:
                    worry //= 3
                if worry % m.test == 0:
                    monkeys[m.on_true].items.append(worry % N)
                else:
                    monkeys[m.on_false].items.append(worry % N)
            m.count += len(m.items)
            m.items = []

    counts = []
    for i, m in enumerate(monkeys):
        counts.append(m.count)

    counts = sorted(counts)
    # Monkey business.
    return counts[-1] * counts[-2]

print(solve())
print(solve(part=2))
