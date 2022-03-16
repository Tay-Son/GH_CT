import sys

num_tc = int(sys.stdin.readline())
for _ in range(num_tc):
    n_ = int(sys.stdin.readline())
    lst_ = [0] + list(map(int, sys.stdin.readline().split()))
    lst_cycle = [-1 for _ in range(n_ + 1)]

    cnt_ = 0
    for idx_ in range(1, n_ + 1):
        if lst_cycle[idx_] == -1:
            curr_ = idx_
            lst_temp = []
            while lst_cycle[curr_] == -1:
                lst_cycle[curr_] = 0
                lst_temp.append(curr_)
                curr_ = lst_[curr_]
            ptr_ = curr_
            for each_ in lst_temp:
                if each_ == ptr_:
                    break
                else:
                    lst_cycle[each_] = 1
        cnt_ += lst_cycle[idx_]
    print(cnt_)