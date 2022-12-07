from collections import deque

tree = []
current_dir = tree
upper_dir = deque()
with open('input-7.txt') as f:
    for line in f.readlines():
        line = line.strip()
        if line.startswith('$ cd '):

            cwd = line[5:]
            if cwd == '/':
                current_dir = tree
                upper_dir = deque()
            elif cwd == '..':
                if upper_dir:
                    current_dir = upper_dir.pop()
            else:
                upper_dir.append(current_dir)
                for item in current_dir:
                    if item[0] == cwd:
                        current_dir = item[1]

        # if line.startswith
        if line.startswith('dir '):
            dir = line[4:]
            current_dir.append((dir, []))
        if '0' <= line[0] <= '9':
            size, name = line.split(' ')
            size = int(size)
            current_dir.append((name, size))


answer_1 = 0
cache = {}
def dir_size(tree):
    global answer_1
    if id(tree) in cache:
        return cache[id(tree)]
    size = 0
    for item in tree:
        _, value = item
        if isinstance(value, list):
            size += dir_size(value)
        else:
            size += value
    cache[id(tree)] = size
    if size < 100000:
        answer_1 += size
    return size

root_size = dir_size(tree)
total_disk = 70000000
need_to_have = 30000000
need_to_delete = 30000000 - (70000000 - root_size)
print(answer_1)


for size in sorted(cache.values()):
    if size >= need_to_delete:
        answer_2 = size
        break

print(answer_2)
        