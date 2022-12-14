from PIL import Image
import random

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

    # the floor
    max_y += 2
    height = max_y - min_y
    print(f'height: {height}')
    min_x -= height + 1
    max_x += height + 1
    for xx in range(min_x, max_x + 1):
        m[(xx, max_y)] = '#'

    def generate_image(name, m, sand):
        min_x = min_y = max_x = max_y = None
        m[500, 0] = '.'
        for p in m.keys():
            x, y = p
            if max_x is None or x > max_x:
                max_x = x
            if max_y is None or y > max_y:
                max_y = y
            if min_x is None or x < min_x:
                min_x = x
            if min_y is None or y < min_y:
                min_y = y

        w = max_x - min_x + 1
        # for ffmpeg width must be divisible by 2
        if w % 2:
            w += 1
        h = max_y - min_y + 1
        img = Image.new('RGB', (w * 2, h * 2), "black")
        pixels = img.load()
        for p in m.keys():
            color = (0, 0, 0)
            x,y = p
            element = m.get((x, y), '.')
            if element == '#':
                color = (127, 127, 127)
            elif isinstance(element, tuple):
                pivot = sand - 1000
                element, index = element
                if index > pivot:
                    a = 196, 158, 118 #p1
                    b = 237, 201, 175 #p2
                    delta = (index - pivot) / max(1, (sand - pivot))
                else:
                    a = 186, 147, 104 #p0
                    b = 196, 158, 118 #p1

                    delta = (sand - index) /  max(1, pivot)
                # a = (255, 200, 0)
                # b = (255, 255, 0)
                # a = 186, 147, 104 #p0
                # b = 196, 158, 118 #p1
                # c = 237, 201, 175 #p2
                color = (
                    int(a[0] * delta + b[0] * (1 - delta)),
                    int(a[1] * delta + b[1] * (1 - delta)),
                    int(a[2] * delta + b[2] * (1 - delta)),
                )
            
            def put_pixel(x, y, color):
                pixels[x * 2, y * 2] = color
                pixels[x * 2, y * 2 + 1] = color
                pixels[x * 2 + 1, y * 2] = color
                pixels[x * 2 + 1, y * 2 + 1] = color
            put_pixel(p[0] - min_x, p[1] - min_y, color)
        img.save(name)
        print(f"save image {name}")

    # for y in range(min_y, max_y + 1):
    #     for x in range(min_x, max_x + 1):
    #         print(m.get((x, y), '.'), end='')
    #     print()

    sand = 0
    can_move_forever = False
    frame = 0
    while not can_move_forever:
        if sand % 250 == 0:
            generate_image(f'map_{frame:06d}.png', m, sand)
            frame += 1
        can_move = True
        sand += 1
        x, y = 500, 0
        if m.get((x, y), '.') != '.':
            break
        while can_move:

            # print(f"#{sand} {x} {y}")
            # move sand

            sign = random.choice([-1, 1])
            if m.get((x, y + 1), '.') == '.':
                y += 1
            elif m.get((x - sign * 1, y + 1), '.') == '.':
                y += 1
                x -= 1 * sign
            elif m.get((x + sign * 1, y + 1), '.') == '.':
                y += 1
                x += 1 * sign
            else:
                m[(x, y)] = ('O', sand)
                can_move = False

            if x < min_x or x > max_x or y > max_y:
                can_move_forever = True
                break

    # for y in range(min_y, max_y + 1):
    #     for x in range(min_x, max_x + 1):
    #         print(m.get((x, y), '.'), end='')
    #     print()

    # print(min_x, min_y, max_x, max_y)
    # print(f"sand: {sand-1}")
