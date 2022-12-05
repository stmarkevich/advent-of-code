
from collections import deque, defaultdict
import re

def solve(part=1):
    stacks = defaultdict(deque)
    with open("input-5.txt") as f:
        for line in f.readlines():
            if not line.strip():
                continue
            if line.startswith('move'):
                m = re.match('move (\d+) from (\d+) to (\d+).*', line)
                if m:
                    n, src, dst = map(int, m.groups())
                    src = stacks[src]
                    dst = stacks[dst]
                    if part == 1:
                        # part 1
                        for i in range(n):
                            dst.append(src.pop())
                    else:
                        # part 2
                        items = deque()
                        for i in range(n):
                            items.append(src.pop())
                        while items:
                            dst.append(items.pop())

            elif line.startswith(' 1'):
                for s in stacks.values():
                    s.reverse()
                # for k in sorted(stacks.keys()):
                #     print(f"  {stacks[k]}")

                pass
            else:
                stack_number = None
                for i, c in enumerate(line):
                    if c == '[':
                        stack_number = i // 4 + 1
                    if 'A' <= c <= 'Z':
                        stacks[stack_number].append(c)
                        stack_number = None
    result = ''
    for k in sorted(stacks.keys()):
        result += stacks[k].pop()
    return result

print(solve())
print(solve(part=2))