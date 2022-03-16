import sys


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


def intersectPB(pnt_, AABB_):
    if pnt_[0] < min(AABB_[0], AABB_[2]) or max(AABB_[0], AABB_[2]) < pnt_[0]:
        return False
    if pnt_[1] < min(AABB_[1], AABB_[3]) or max(AABB_[1], AABB_[3]) < pnt_[1]:
        return False
    return True


def intersectLB(lst_input):
    line_ = lst_input[:4]

    pnt_lb = [min(lst_input[4], lst_input[6]), min(lst_input[5], lst_input[7])]
    pnt_rb = [max(lst_input[4], lst_input[6]), min(lst_input[5], lst_input[7])]
    pnt_lt = [min(lst_input[4], lst_input[6]), max(lst_input[5], lst_input[7])]
    pnt_rt = [max(lst_input[4], lst_input[6]), max(lst_input[5], lst_input[7])]

    if intersect(line_, pnt_lb + pnt_lt):
        return True
    if intersect(line_, pnt_rb + pnt_rt):
        return True
    if intersect(line_, pnt_lb + pnt_rb):
        return True
    if intersect(line_, pnt_lt + pnt_rt):
        return True

    if intersectPB(line_[:2], pnt_lb + pnt_rt) and intersectPB(line_[2:], pnt_lb + pnt_rt):
        return True
    return False


T_ = int(sys.stdin.readline())

for _ in range(T_):
    lst_input = list(map(int, sys.stdin.readline().split()))
    if intersectLB(lst_input):
        print('T')
    else:
        print('F')

exit()