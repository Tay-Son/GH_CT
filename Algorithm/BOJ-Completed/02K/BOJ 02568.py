import sys

lst_ = []
set_ = set()
for _ in range(int(sys.stdin.readline())):
    s_, e_ = map(int, sys.stdin.readline().split())
    lst_.append((s_, e_))
    set_.add(s_)

lst_.sort(key=lambda x: x[1])

lst_sub = [-1]
dct_sub = {}

for s_, trs_ in lst_:
    ptr_s = 0
    ptr_e = len(lst_sub)
    while ptr_s < ptr_e:
        ptr_c = (ptr_s + ptr_e) // 2
        if s_ < lst_sub[ptr_c]:
            ptr_e = ptr_c
        else:
            ptr_s = ptr_c + 1

    if ptr_e == len(lst_sub):
        lst_sub.append(s_)
    else:
        lst_sub[ptr_e] = s_

    dct_sub[s_] = lst_sub[ptr_e - 1]

curr_ = lst_sub[-1]
while curr_ != -1:
    set_.remove(curr_)
    curr_ = dct_sub[curr_]

print(len(set_))
for each_ in sorted(set_):
    print(each_)
exit()
