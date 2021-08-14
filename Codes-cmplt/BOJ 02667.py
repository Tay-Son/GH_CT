import sys

val_N = int(sys.stdin.readline())
grd_ = [[] for _ in range(val_N)]
for idx_y in reversed(range(val_N)):
    grd_[idx_y] = list(map(int, list(sys.stdin.readline()[:-1])))


def search(idx_x, idx_y):
    grd_[idx_y][idx_x] = 0

    tot_ = 1
    if idx_x < val_N-1 and grd_[idx_y][idx_x + 1] == 1:
        tot_ += search(idx_x + 1, idx_y)
    if idx_y < val_N-1 and grd_[idx_y + 1][idx_x] == 1:
        tot_ += search(idx_x, idx_y + 1)
    if idx_x > 0 and grd_[idx_y][idx_x - 1] == 1:
        tot_ += search(idx_x - 1, idx_y)
    if idx_y > 0 and grd_[idx_y - 1][idx_x] == 1:
        tot_ += search(idx_x, idx_y - 1)
    return tot_


lst_answer = []
for idx_y in range(val_N):
    for idx_x in range(val_N):
        if grd_[idx_y][idx_x] == 1:
            lst_answer.append(search(idx_x, idx_y))
lst_answer.sort()

print(len(lst_answer))
for each_ in lst_answer:
    print(each_)
exit()