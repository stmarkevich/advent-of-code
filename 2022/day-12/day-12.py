

with open('input-12.txt') as f:
    m = []
    for line in f.readlines():
        m.append(line.strip())

    N = len(m)
    M = len(m[0])

def solve(part=1):
    visited = set()
    path = []

    start_points = 'S' if part == 1 else 'Sa'
    for j in range(N):
        for i in range(M):
            if m[j][i] in start_points:
                start = i, j
                visited.add(start)
                path.append([start])
            if m[j][i] == 'E':
                end = i, j

    def height(place):
        if place == 'S':
            place = 'a'
        if place == 'E':
            place = 'z'
        return ord(place)

    while path:
        path_to_check = path
        path = []
        for p in path_to_check:
            if p[-1] == end:
                return len(p)-1
            i, j = p[-1]
            if i > 0 and height(m[j][i-1]) - height(m[j][i]) <= 1 and not (i-1,j) in visited:
                path.append(p + [(i-1, j)])
                visited.add((i-1,j))
            if i < M-1 and height(m[j][i+1]) - height(m[j][i]) <= 1 and not (i+1,j) in visited:
                path.append(p + [(i+1, j)])
                visited.add((i+1,j))
            if j > 0 and height(m[j-1][i]) - height(m[j][i]) <= 1 and not (i,j-1) in visited:
                path.append(p + [(i, j-1)])
                visited.add((i,j-1))
            if j < N-1 and height(m[j+1][i]) - height(m[j][i]) <= 1 and not (i,j+1) in visited:
                path.append(p + [(i, j+1)])
                visited.add((i,j+1))

print(solve())
print(solve(part=2))