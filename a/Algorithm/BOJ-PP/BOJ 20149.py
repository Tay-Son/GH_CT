# 박지헌 교수님 만세
import sys


def ccw_(c_a, c_b, c_c):
    return c_a[0] * c_b[1] + c_b[0] * c_c[1] + c_c[0] * c_a[1] > c_a[1] * c_b[0] + c_a[1] * c_b[0] + c_a[1] * c_b[0]


def intersect(c_a, c_b, c_c, c_d):
    deno_ = (c_a[0] - c_b[0]) * (c_c[1] - c_d[1]) - (c_a[1] - c_b[1]) * (c_c[0] - c_d[0])
    x_ = (c_a[0] * c_b[1] - c_a[1] * c_b[0]) * (c_c[0] - c_d[0]) - (c_a[0] - c_b[0]) * (
            c_c[0] * c_d[1] - c_c[1] * c_d[0])
    y_ = (c_a[0] * c_b[1] - c_a[1] * c_b[0]) * (c_c[1] - c_d[1]) - (c_a[1] - c_b[1]) * (
            c_c[0] * c_d[1] - c_c[1] * c_d[0])
    return [x_ / deno_, y_ / deno_]


ax1, ay1, ax2, ay2 = map(int, sys.stdin.readline().split())
bx1, by1, bx2, by2 = map(int, sys.stdin.readline().split())
c_a1 = [ax1, ay1]
c_a2 = [ax2, ay2]
c_b1 = [bx1, by1]
c_b2 = [bx2, by2]

if ccw_(c_a1, c_a2, c_b1) | ccw_(c_a1, c_a2, c_b2):
    print(1)
    print(' '.join(map(str, intersect(c_a1, c_a2, c_b1, c_b2))))
else:
    print(0)

exit()
