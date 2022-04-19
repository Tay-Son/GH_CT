import sys

N_, M_ = map(int, sys.stdin.readline().split())
grd_ = []
for _ in range(N_):
    grd_.append(sys.stdin.readline().rstrip())

for idx_n in range(N_):
    for idx_m in range(M_):
        if grd_[idx_n][idx_m] == '#':
            break
    else:
        continue
    break

offset_ = 2
while (idx_n + offset_ + 2 < N_ and grd_[idx_n + offset_ + 2][idx_m] == '#') \
        or (idx_m + offset_ + 2 < M_ and grd_[idx_n][idx_m + offset_ + 2] == '#'):
    offset_ += 2

offset_ //= 2

if grd_[idx_n + offset_][idx_m] == '.':
    print('LEFT')
elif grd_[idx_n][idx_m + offset_] == '.':
    print('UP')
elif grd_[idx_n + 2 * offset_][idx_m + offset_] == '.':
    print('DOWN')
else:
    print('RIGHT')

exit()
