import sys

str_t = sys.stdin.readline().rstrip()
str_p = sys.stdin.readline().rstrip()

lst_pi = [0 for _ in range(len(str_p))]

ptr_b = 0
for ptr_a in range(1, len(str_p)):
    while ptr_b > 0 and str_p[ptr_a] != str_p[ptr_b]:
        ptr_b = lst_pi[ptr_b - 1]
    if str_p[ptr_a] == str_p[ptr_b]:
        ptr_b += 1
        lst_pi[ptr_a] = ptr_b

lst_ans = []
idx_p = 0
for idx_t in range(len(str_t)):
    while idx_p > 0 and str_t[idx_t] != str_p[idx_p]:
        idx_p = lst_pi[idx_p - 1]
    if str_t[idx_t] == str_p[idx_p]:
        if idx_p == len(str_p) - 1:
            lst_ans.append(idx_t - len(str_p) + 2)
            idx_p = lst_pi[idx_p]
        else:
            idx_p += 1

print(len(lst_ans))
print(' '.join(map(str, lst_ans)))
exit()
