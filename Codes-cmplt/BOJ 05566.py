import sys

N_, M_ = map(int, sys.stdin.readline().split())
lst_order = [0]
for _ in range(N_):
    lst_order.append(int(sys.stdin.readline()))

curr_ = 1
for cnt_ in range(1, M_ + 1):
    curr_ += int(sys.stdin.readline())
    if curr_ < N_:
        curr_ += lst_order[curr_]
        if not curr_ < N_:
            break
    else:
        break
print(cnt_)

exit()