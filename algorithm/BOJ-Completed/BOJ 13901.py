import sys

R_, C_ = map(int, sys.stdin.readline().split())
grd_movable = [[True for _ in range(C_)] for _ in range(R_)]

for _ in range(int(sys.stdin.readline())):
    temp_r, temp_c = map(int, sys.stdin.readline().split())
    grd_movable[temp_r][temp_c] = False

curr_r, curr_c = map(int, sys.stdin.readline().split())
lst_order = [(-1, 0), (1, 0), (0, -1), (0, 1)]
lst_seq = list(map(lambda x: int(x) - 1, sys.stdin.readline().split()))

cnt_seq = 0
is_ = True
while is_:
    grd_movable[curr_r][curr_c] = False
    is_ = False
    for _ in range(4):
        ord_r, ord_c = lst_order[lst_seq[cnt_seq % 4]]
        dest_r, dest_c = curr_r + ord_r, curr_c + ord_c
        if 0 <= dest_r < R_ and 0 <= dest_c < C_ and grd_movable[dest_r][dest_c]:
            curr_r, curr_c = dest_r, dest_c
            is_ = True
            break
        cnt_seq += 1

print(curr_r, curr_c)
exit()
