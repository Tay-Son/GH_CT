import sys

R_, C_ = map(int, sys.stdin.readline().split())
str_ans = ''
if not R_ % 2 and not C_ % 2:
    min_ = 1000
    min_r = 0
    min_c = 0
    for idx_r in range(R_):
        for idx_c, val_ in enumerate(map(int, sys.stdin.readline().split())):
            if (idx_r + idx_c) % 2 and val_ < min_:
                min_ = val_
                min_r = idx_r
                min_c = idx_c

    for idx_r in range(0, min_r // 2 * 2, 2):
        str_ans += 'R' * (C_ - 1) + 'D' + 'L' * (C_ - 1) + 'D'
    cnt_ = 0
    for idx_c in range(C_):
        if idx_c != min_c:
            str_ans += 'U' if cnt_ % 2 else 'D'
            cnt_ += 1
        if idx_c != C_ - 1:
            str_ans += 'R'
    for idx_r in range((min_r // 2 + 1) * 2, R_, 2):
        str_ans += 'D' + 'L' * (C_ - 1) + 'D' + 'R' * (C_ - 1)
elif R_ % 2:
    for _ in range(R_ // 2):
        str_ans += 'R' * (C_ - 1) + 'D' + 'L' * (C_ - 1) + 'D'
    str_ans += 'R' * (C_ - 1)
else:
    for _ in range(C_ // 2):
        str_ans += 'D' * (R_ - 1) + 'R' + 'U' * (R_ - 1) + 'R'
    str_ans += 'D' * (R_ - 1)

print(str_ans)
exit()
