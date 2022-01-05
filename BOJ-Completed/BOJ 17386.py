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


lst_line = []
for _ in range(2):
    lst_line.append(list(map(int, sys.stdin.readline().split())))

if intersect(lst_line[0], lst_line[1]):
    print(1)
else:
    print(0)

exit()