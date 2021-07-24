import sys

lst_a = [-1 for _ in range(500001)]
lst_l = [-1 for _ in range(100001)]
lst_t = []

for idx_ in range(int(sys.stdin.readline())):
    a_, b_ = map(int, sys.stdin.readline().split())
    lst_a[a_] = idx_
    lst_t.append(b_)
lst_b = []
for b_ in lst_t:
    temp_ = lst_a[b_]
    if temp_ != -1:
        lst_b.append(temp_)
        lst_l[temp_] = b_

lst_dp = []
lst_sub = [(-1,-1)]

for each_ in lst_b:
    ptr_s = 0
    ptr_e = len(lst_sub)
    while ptr_s < ptr_e:
        ptr_c = (ptr_s + ptr_e) // 2
        if each_ < lst_sub[ptr_c][0]:
            ptr_e = ptr_c
        else:
            ptr_s = ptr_c + 1

    if ptr_e == len(lst_sub):
        lst_sub.append((each_,lst_sub[ptr_e-1][0]))
    else:
        lst_sub[ptr_e] = (each_,lst_sub[ptr_e-1][0])
    lst_dp.append(ptr_e)

lst_sub.append((-1, lst_sub[-1][0]))
ptr_sub = len(lst_sub) -1
for each_ in sorted(lst_b,reverse=True):
    print(each_,lst_sub[ptr_sub][1])
    if ptr_sub > 1 and each_ == lst_sub[ptr_sub][1]:
        ptr_sub -= 1
    else:
        print(lst_l[each_])

print(lst_sub)
print(lst_dp)
print(len(lst_b) - max(lst_dp))

exit()
