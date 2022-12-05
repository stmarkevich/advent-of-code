
def contain_fully(a, b):
    a_l, a_r = map(int, a.split('-'))
    b_l, b_r = map(int, b.split('-'))
    if b_l <= a_l <= b_r and b_l <= a_r <= b_r:
        return True
    if a_l <= b_l <= a_r and a_l <= b_r <= a_r:
        return True
    return False 

def overlap(a, b):
    a_l, a_r = map(int, a.split('-'))
    b_l, b_r = map(int, b.split('-'))
    if b_l <= a_l <= b_r or b_l <= a_r <= b_r:
        return True
    if a_l <= b_l <= a_r or a_l <= b_r <= a_r:
        return True
    return False

s = 0
s2 = 0
with open('input-4.txt') as f:
    for line in f.readlines():
        left, right = line.strip().split(',')
        if contain_fully(left, right):
            s += 1
        if overlap(left, right):
            s2 += 1

print(s)
print(s2)
