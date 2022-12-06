
def solve(part=1):
    with open("input-6.txt") as f:
        data = f.read()
        packet = ''
        for i, c in enumerate(data):
            packet += c
            length = 14 if part == 2 else 4
            if len(packet) > length:
                packet = packet[-length:]
            if len(packet) == length and len(set(packet)) == length:
                return i + 1
                break

print(solve())
print(solve(part=2))