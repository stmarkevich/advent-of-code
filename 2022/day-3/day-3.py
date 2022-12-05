
def priority(item):
    if item >= 'a' and item <= 'z':
        return ord(item) - ord('a') + 1
    if item >= 'A' and item <= 'Z':
        return ord(item) - ord('A') + 27

def wrong_item(left, right):
    d = set(left).intersection(right)
    return next(iter(d))

s = 0
group = []
s2 = 0
with open('input-3.txt') as f:
    for line in f.readlines():
        data = line.strip()
        n = len(data) // 2
        left, right = data[:n], data[n:]
        c = wrong_item(left, right)
        s += priority(c)

        group.append(data)
        if len(group) == 3:
            common = set(group[0]).intersection(group[1])
            common = common.intersection(group[2])
            common = next(iter(common))
            s2 += priority(common)
            group = []


print(s)
print(s2)

