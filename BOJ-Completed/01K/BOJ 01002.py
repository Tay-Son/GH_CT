import sys

num_tc = int(sys.stdin.readline())
for _ in range(num_tc):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())

    if x1 == x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    else:
        r1_sq = r1 ** 2
        r2_sq = r2 ** 2

        d_sq = (x1 - x2) ** 2 + (y1 - y2) ** 2
        r_sq = (r1 + r2) ** 2

        if max(r1_sq, r2_sq) > d_sq:
            if abs(r1 - r2) ** 2 == d_sq:
                print(1)
            elif abs(r1 - r2) ** 2 < d_sq:
                print(2)
            elif abs(r1 - r2) ** 2 > d_sq:
                print(0)

        else:
            if d_sq == r_sq:
                print(1)
            elif d_sq > r_sq:
                print(0)
            elif d_sq < r_sq:
                print(2)
