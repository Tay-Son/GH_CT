import sys

N_, K_, Q_ = map(int, sys.stdin.readline().split())
lst_ = []
for _ in range(K_):
    a_, b_ = sys.stdin.readline().split()
    lst_.append((a_, b_))

if lst_[Q_ - 1][0] == '0':
    print(-1)
else:
    set_ = set([chr(idx_) for idx_ in range(ord('B'), ord('A') + N_)])
    for idx_K in range(Q_ - 1, K_):
        a_, b_ = lst_[idx_K]
        if b_ in set_:
            set_.remove(b_)
    ptr_ = Q_ - 1
    c_ = lst_[ptr_][0]
    while 0 < ptr_ and lst_[ptr_ - 1][0] == c_:
        ptr_ -= 1
        b_ = lst_[ptr_][1]
        if b_ in set_:
            set_.remove(b_)
    print(' '.join(map(str, sorted(list(set_)))))

exit()
