import sys

L_ = int(sys.stdin.readline())
str_ = sys.stdin.readline().rstrip()

lst_pi = [0 for _ in range(L_)]

ptr_b = 0
for ptr_a in range(1, L_):
    while ptr_b > 0 and str_[ptr_a] != str_[ptr_b]:
        ptr_b = lst_pi[ptr_b - 1]
    if str_[ptr_a] == str_[ptr_b]:
        ptr_b += 1
        lst_pi[ptr_a] = ptr_b

print(L_ - lst_pi[L_ - 1])

exit()
