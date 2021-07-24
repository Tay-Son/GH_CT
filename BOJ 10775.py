import sys
sys.setrecursionlimit(10**5)

G_ = int(sys.stdin.readline())
P_ = int(sys.stdin.readline())

lst_ = [i_ for i_ in range(G_ + 1)]


def find(idx_):
    temp_ = lst_[idx_]
    if temp_ != idx_:
        lst_[idx_] = find(temp_)
    return lst_[idx_]


tot_ = 0
for _ in range(P_):
    V_ = int(sys.stdin.readline())
    temp_ = find(V_)
    if temp_:
        lst_[temp_] -= 1
        tot_ += 1
    else:
        break
print(tot_)

exit()
