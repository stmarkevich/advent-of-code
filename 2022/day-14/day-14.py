
with open('input-14.txt') as f:

    m = {}
    min_x = max_x = 500
    min_y = max_y = 0
    for line in f.readlines():
        line = line.strip()

        points = line.split(' -> ')
        start = None
        for p in points:
            x, y = list(map(int, p.split(',')))

            if x > max_x:
                max_x = x
            if y > max_y:
                max_y = y
            if x < min_x:
                min_x = x
            if y < min_y:
                min_y = y

            if start:
                if x == start[0]:
                    for yy in range(min(start[1], y), max(start[1], y) + 1):
                        m[(x, yy)] = '#'
                else:
                    for xx in range(min(start[0], x), max(start[0], x) + 1):
                        m[(xx, y)] = '#'
                start = x, y
            else:
                start = x, y

def solve(m, min_x, min_y, max_x, max_y, part=1):
    m  = dict(m)
    if part == 2:
        # the "infinite" floor
        max_y += 2
        height = max_y - min_y
        min_x -= height + 1
        max_x += height + 1
        for xx in range(min_x, max_x + 1):
            m[(xx, max_y)] = '#'

    sand = 0
    can_move_forever = False
    while not can_move_forever:
        can_move = True
        sand += 1
        x, y = 500, 0
        if m.get((x, y), '.') != '.':
            break
        while can_move:
            if m.get((x, y + 1), '.') == '.':
                y += 1
            elif m.get((x - 1, y + 1), '.') == '.':
                y += 1
                x -= 1
            elif m.get((x + 1, y + 1), '.') == '.':
                y += 1
                x += 1
            else:
                m[(x, y)] = 'O'
                can_move = False

            if x < min_x or x > max_x or y > max_y:
                can_move_forever = True
                break

    # for y in range(min_y, max_y + 1):
    #     for x in range(min_x, max_x + 1):
    #         print(m.get((x, y), '.'), end='')
    #     print()

    return sand - 1

print(solve(m, min_x, min_y, max_x, max_y))
print(solve(m, min_x, min_y, max_x, max_y, part=2))