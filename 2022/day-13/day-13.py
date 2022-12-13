import functools

with open('input-13.txt') as f:
    pairs = []

    left = None
    for line in f.readlines():
        line = line.strip()
        if not line:
            continue
        p = eval(line)
        if left is not None:
            pairs.append((left, p))
            left = None
        else:
            left = p

    def check_pair(a, b):
        if isinstance(a, list) and not isinstance(b, list):
            b = [b]
        if not isinstance(a, list) and isinstance(b, list):
            a = [a]
        
        if isinstance(a, list):
            for i in range(len(a)):
                if i >= len(b):
                    return 1
                test = check_pair(a[i], b[i])
                if test:
                    return test
            return len(a) - len(b)
        else:
            return a - b

    correct = []
    key_a = [[2]]
    key_b = [[6]]
    packets = [key_a, key_b]
    for i, (a,b) in enumerate(pairs):
        packets.append(a)
        packets.append(b)
        if check_pair(a,b) < 0:
            correct.append(i + 1)

    print(sum(correct))

    packets.sort(key=functools.cmp_to_key(check_pair))
    index_a = packets.index(key_a) + 1
    index_b = packets.index(key_b) + 1

    print(index_a * index_b)
