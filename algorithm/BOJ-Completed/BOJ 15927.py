import sys

str_ = sys.stdin.readline().rstrip()
len_ = len(str_)

is_p = True
is_a = True
ptr_s = 0
ptr_e = len_ - 1

while ptr_s < ptr_e:
    if str_[ptr_s] != str_[0]:
        is_a = False
    if str_[ptr_s] != str_[ptr_e]:
        is_p = False
        break
    ptr_s += 1
    ptr_e -= 1
if str_[ptr_s] != str_[0]:
    is_a = False

if not is_p:
    print(len_)
else:
    if not is_a:
        print(len_ - 1)
    else:
        print(-1)
exit()

c_s = 0
c_e = len_
while c_s < c_e:
    c_c = (c_s + c_e) // 2
    print(c_s, c_e, c_c, end=' ')
    ptr_s = c_c
    ptr_e = len_ - 1
    is_p = True

    while ptr_s < ptr_e:
        if str_[ptr_s] != str_[ptr_e]:
            is_p = False
            break

        ptr_s += 1
        ptr_e -= 1

    if is_p:
        print('is_p')
        c_s = c_c + 1
    else:
        print('is_not_p')
        c_e = c_c

print(len_ - c_s if len_ != c_s else -1)
exit()

for idx_s in range(len_ - 1):
    ptr_s = idx_s
    ptr_e = len_ - 1
    is_p = True
    while ptr_s < ptr_e:
        if str_[ptr_s] != str_[ptr_e]:
            is_p = False
            break

        ptr_s += 1
        ptr_e -= 1
    if not is_p:
        print(len_ - idx_s)
        break
else:
    print(-1)
exit()
