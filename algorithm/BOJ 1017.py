import sys

N_ = int(sys.stdin.readline())
lst_ = list(map(int, sys.stdin.readline().split()))

val_max = sum(sorted(lst_)[-2:]) + 1
lst_ip = [True for _ in range(val_max)]
lst_ip[0], lst_ip[1] = False, False
for val_ in range(2, val_max):
    if lst_ip[val_]:
        for val_sub in range(val_ + val_, val_max, val_):
            lst_ip[val_sub] = False

lst_e = [0]
lst_d = [0]
temp_ = lst_[0] % 2
for val_ in lst_:
    if temp_ == val_ % 2:
        lst_e.append(val_)
    else:
        lst_d.append(val_)

print(lst_e)
print(lst_d)
print()

if len(lst_e) != len(lst_d):
    print(-1)
else:
    grd_p = [[] for _ in range(len(lst_e))]

    for idx_e in range(1, len(lst_e)):
        for idx_d in range(1, len(lst_d)):
            val_ = lst_e[idx_e] + lst_d[idx_d]
            if lst_ip[val_]:
                grd_p[idx_e].append(idx_d)
    for each_ in grd_p:
        print(each_)
    print()


    def rec_(idx_, lst_iv, lst_p):
        if lst_iv[idx_]:
            return False
        else:
            lst_iv[idx_] = True
            for idx_t in grd_p[idx_]:
                if not lst_p[idx_t] or rec_(lst_p[idx_t], lst_iv, lst_p):
                    lst_p[idx_t] = idx_
                    return True
            else:
                return False


    lst_ans = []
    for idx_ in grd_p[1]:
        lst_p = [0 for _ in range(len(lst_d))]
        lst_p[idx_] = 1
        cnt_ = 1
        for idx_sub in range(1, len(lst_e)):
            lst_iv = [False for _ in range(len(lst_e))]
            lst_iv[1] = True
            cnt_ += 1 if rec_(idx_sub, lst_iv, lst_p) else 0
        if cnt_ == N_ // 2:
            lst_ans.append(lst_d[idx_])
        print(lst_d[idx_], cnt_)

    if len(lst_ans):
        print(' '.join(map(str, sorted(lst_ans))))
    else:
        print(-1)

exit()
