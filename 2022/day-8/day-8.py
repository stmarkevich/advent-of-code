
with open('input-8.txt') as f:
    m = []
    for line in f.readlines():
        m.append(list(map(int, line.strip())))

    N = len(m)
    M = len(m[0])
    visible_trees = 2 * M + 2 * N - 4
    visibility = [[0] * M for j in range(N)]

    def is_visible(x, y):
        print(f'is_visible({x}, {y})')
        import time
        time.sleep(1)
        if x == 0 or x == M - 1 or y == 0 or y == N - 1:
            return 1
        if visibility[y][x] is not None:
            return visibility[y][x]
        visible = 0
        # visible from left
        if is_visible(x - 1, y) and m[y][x - 1] < m[y][x]:
            visible = 1
        elif is_visible(x + 1, y) and m[y][x + 1] < m[y][x]:
            visible = 1
        elif is_visible(x, y - 1) and m[y - 1][x] < m[y][x]:
            visible = 1
        elif is_visible(x, y + 1) and m[y + 1][x] < m[y][x]:
            visible = 1
            
        visibility[y][x] = visible
        return visible
        
    def update_scores(scores, current_tree):
        for i in range(len(scores)):
            if i <= current_tree:
                scores[i] = 0
            else:
                scores[i] += 1

    # visible from the left
    left_scores = [[0] * M for j in range(N)]
    for j in range(N):
        visibility[j][0] = 1
        highest = m[j][0]
        scores = [0] * 10
        left_scores[j][0] = 0
        for i in range(1, M):
            left_scores[j][i] = scores[m[j][i]] + 1
            update_scores(scores, m[j][i])
            if m[j][i] > highest:
                visibility[j][i] = 1
                highest = m[j][i]

    # visible from the right
    right_scores = [[0] * M for j in range(N)]
    for j in range(N):
        visibility[j][M-1] = 1
        highest = m[j][M-1]
        scores = [0] * 10
        for i in range(M-2, -1, -1):
            right_scores[j][i] = scores[m[j][i]] + 1
            update_scores(scores, m[j][i])
            if m[j][i] > highest:
                visibility[j][i] = 1
                highest = m[j][i]
    
    # visible from the top
    top_scores = [[0] * M for j in range(N)]
    for i in range(M):
        visibility[0][i] = 1
        highest = m[0][i]
        scores = [0] * 10
        for j in range(N):
            top_scores[j][i] = scores[m[j][i]] + 1
            update_scores(scores, m[j][i])
            if m[j][i] > highest:
                visibility[j][i] = 1
                highest = m[j][i]

    # visible from the bottom
    bottom_scores = [[0] * M for j in range(N)]
    for i in range(M):
        visibility[N-1][i] = 1
        highest = m[N-1][i]
        scores = [0] * 10
        for j in range(N-2, -1, -1):
            bottom_scores[j][i] = scores[m[j][i]] + 1
            update_scores(scores, m[j][i])
            if m[j][i] > highest:
                visibility[j][i] = 1
                highest = m[j][i]

    count_visible = 0
    for row in visibility:
        for tree in row:
            if tree:
                count_visible += 1

    highest_score = 0
    
    for j in range(N):
        for i in range(M):
            score = left_scores[j][i] * right_scores[j][i] * top_scores[j][i] * bottom_scores[j][i]
            if score > highest_score:
                highest_score = score

print(count_visible)
print(f"{highest_score}")