import sys
from itertools import combinations as cb

N_ = int(sys.stdin.readline())
lst_p = [[i_, 1] for i_ in range(N_)]


def intersect(line_a, line_b):
    if max(line_a[0], line_a[2]) < min(line_b[0], line_b[2]):
        return False
    if min(line_a[0], line_a[2]) > max(line_b[0], line_b[2]):
        return False
    if max(line_a[1], line_a[3]) < min(line_b[1], line_b[3]):
        return False
    if min(line_a[1], line_a[3]) > max(line_b[1], line_b[3]):
        return False

    is_a = (line_a[2] - line_a[0]) * (line_b[1] - line_a[1]) - (line_b[0] - line_a[0]) * (line_a[3] - line_a[1])
    is_b = (line_a[2] - line_a[0]) * (line_b[3] - line_a[1]) - (line_b[2] - line_a[0]) * (line_a[3] - line_a[1])
    is_c = (line_b[2] - line_b[0]) * (line_a[1] - line_b[1]) - (line_a[0] - line_b[0]) * (line_b[3] - line_b[1])
    is_d = (line_b[2] - line_b[0]) * (line_a[3] - line_b[1]) - (line_a[2] - line_b[0]) * (line_b[3] - line_b[1])

    if is_a == 0 and is_b == 0 and is_c == 0 and is_d == 0:
        return True

    return is_a * is_b <= 0 and is_c * is_d <= 0


def find(idx_):
    temp_ = lst_p[idx_]
    if temp_[0] != idx_:
        temp_ = find(temp_[0])
        lst_p[idx_] = temp_
    return temp_


def union(idx_a, idx_b):
    p_a = find(idx_a)
    p_b = find(idx_b)

    if p_a[0] > p_b[0]:
        lst_p[p_a[0]][1] = p_a[1] + p_b[1]
        lst_p[p_b[0]] = lst_p[p_a[0]]

    elif p_a[0] < p_b[0]:
        lst_p[p_b[0]][1] = p_a[1] + p_b[1]
        lst_p[p_a[0]] = lst_p[p_b[0]]


lst_line = []
for _ in range(N_):
    lst_line.append(list(map(int, sys.stdin.readline().split())))

for cb_ in cb(range(N_), 2):
    if intersect(lst_line[cb_[0]], lst_line[cb_[1]]):
        union(cb_[0], cb_[1])

cnt_ = 0
max_ = 0

for idx_ in range(N_):
    temp_ = find(idx_)
    if temp_[0] == idx_:
        cnt_ += 1
    if temp_[1] > max_:
        max_ = temp_[1]

print(cnt_)
print(max_)

exit()
