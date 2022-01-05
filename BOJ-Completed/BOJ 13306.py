import sys

sys.setrecursionlimit(10 ** 6)

N_, Q_ = map(int, sys.stdin.readline().split())
lst_ = [cnt_ for cnt_ in range(N_ + 1)]
lst_p = [0, 1]
for idx_ in range(2, N_ + 1):
    lst_p.append(int(sys.stdin.readline()))


def find(idx_):
    temp_ = lst_[idx_]
    if temp_ != idx_:
        temp_ = find(temp_)
        lst_[idx_] = temp_
    return temp_


lst_is = [True for _ in range(N_ + 1)]
stk_com = []
for _ in range(N_ + Q_ - 1):
    stk_com.append(tuple(map(int, sys.stdin.readline().split())))
    if stk_com[-1][0] == 0:
        lst_is[stk_com[-1][1]] = False

for idx_ in range(2, N_ + 1):
    if lst_is[idx_]:
        lst_[idx_] = find(lst_p[idx_])
stk_ans = []
while stk_com:
    lst_com = stk_com.pop()
    if lst_com[0] == 0:
        lst_is[lst_com[1]] = True
        lst_[lst_com[1]] = find(lst_p[lst_com[1]])
    elif lst_com[0] == 1:
        if find(lst_com[1]) == find(lst_com[2]):
            stk_ans.append(True)
        else:
            stk_ans.append(False)
while stk_ans:
    ans_ = stk_ans.pop()
    if ans_:
        print('YES')
    else:
        print('NO')

exit()
