import sys

N_ = int(sys.stdin.readline())
lst_ori = list(map(int, list(sys.stdin.readline().rstrip())))
lst_cnt = list(map(lambda x: x ^ 1, lst_ori))

lst_o = []
ptr_ = 0

print(''.join(map(str, lst_ori)))
print(''.join(map(str, lst_cnt)))
for idx_a in range(0, N_ - 1):
    lst_ori[idx_a] ^= 1
    lst_cnt[idx_a] ^= 1
    print(''.join(map(str, lst_ori)))
    print(''.join(map(str, lst_cnt)))

    lst_o.append(idx_a)
    for _ in range(1, 2 ** idx_a):
        idx_target = lst_o[ptr_]
        lst_ori[idx_target] ^= 1
        lst_cnt[idx_target] ^= 1
        print(''.join(map(str, lst_ori)))
        print(''.join(map(str, lst_cnt)))
        lst_o.append(idx_target)
        ptr_ += 1
    ptr_ = 0

exit()
