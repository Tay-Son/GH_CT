import sys

lst_p = [500, 100, 50, 10, 5, 1]

A_ = int(sys.stdin.readline())
R_ = 1000 - A_
cnt_ = 0
for p_ in lst_p:
    div_, R_ = divmod(R_, p_)
    cnt_ += div_
print(cnt_)
exit()
