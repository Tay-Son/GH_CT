import sys

N_, M_ = map(int, sys.stdin.readline().split())
s_x, s_y = map(int, sys.stdin.readline().split())
e_x, e_y = map(int, sys.stdin.readline().split())

if N_ == 1 or M_ == 1:
    if s_x == e_x and s_y == e_y:
        print('YES')
    else:
        print('NO')
else:
    if (s_x + s_y) % 2 == (e_x + e_y) % 2:
        print('YES')
    else:
        print('NO')

exit()
