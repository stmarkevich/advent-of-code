
code = []
x_values = [1]
with open("input-10.txt") as f:
    for line in f.readlines():
        if line.startswith('noop'):
            x_values.append(x_values[-1])
        if line.startswith('add'):
            _, inc = line.split()
            inc = int(inc)
            x_values.append(x_values[-1])
            x_values.append(x_values[-1] + inc)

answer_1 = 0
for probe in [20, 60, 100, 140, 180, 220]:
    answer_1 += probe * x_values[probe-1]

print(f"{answer_1}")

# Answer 2 is given in a visual form.
line = ''
for i, x in enumerate(x_values):
    h = i % 40
    if h == 0:
        print('')
    if abs(h - x) <= 1:
        print('#', end='')
    else:
        print('.', end='')

