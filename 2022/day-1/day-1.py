

elfs = []
s = 0
with open('input-1.txt') as f:
    for line in f.readlines():
        line = line.strip()
        if line:
            s += int(line)
        else:
            elfs.append(s)
            s = 0
elfs.append(s)

print(max(elfs))

elfs = sorted(elfs)[-3:]
print(sum(elfs))
