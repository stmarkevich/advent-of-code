
def move_head(head, direction):
    """Move the head according to the given direction."""
    if direction == 'R':
        head = head[0] + 1, head[1]
    elif direction == "L":
        head = head[0] - 1, head[1]
    elif direction == "U":
        head = head[0], head[1] + 1
    elif direction == "D":
        head = head[0], head[1] - 1
    return head

def move_tail(head, tail):
    """If necessary move the tail to the position where the tension is minimal."""

    def force(head, tail):
        f = head[0] - tail[0], head[1] - tail[1]
        return f[0] * f[0] + f[1] * f[1]

    f = force(head, tail)
    if f > 2:
        min_force = f
        min_position = tail

        for inc_x in [-1, 0, 1]:
            for inc_y in [-1, 0, 1]:
                if inc_x or inc_y:
                    new_tail = tail[0] + inc_x, tail[1] + inc_y
                    new_force = force(head, new_tail)
                    if new_force < min_force:
                        min_position = new_tail
                        min_force = new_force
        tail = min_position
    
    return tail

class Rope:
    def __init__(self, length):
        self._state = [(0, 0)] * length
        self._history = set()
        self._history.add(self._state[-1])

    def move_head(self, direction):
        length = len(self._state)
        self._state[0] = move_head(self._state[0], direction)
        for i in range(length - 1):
            self._state[i + 1] = move_tail(self._state[i], self._state[i + 1])
        self._history.add(self._state[-1])

    def tail_history(self):
        return self._history

with open('input-9.txt') as f:
    rope_2 = Rope(2)
    rope_10 = Rope(10)

    for line in f.readlines():
        direction, length = line.split()
        for _ in range(int(length)):
            rope_2.move_head(direction)
            rope_10.move_head(direction)

print(f"{len(rope_2.tail_history())}")
print(f"{len(rope_10.tail_history())}")
