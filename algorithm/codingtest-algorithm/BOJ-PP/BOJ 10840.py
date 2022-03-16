import sys

str_a = sys.stdin.readline().rstrip()
str_b = sys.stdin.readline().rstrip()

ptr_a_s = 0

lst_c_a = [0 for _ in range(26)]
lst_c_a[ord(str_a[0]) - ord('a')] += 1

for ptr_a_e in range(len(str_a)):
    print(ptr_a_s, ptr_a_e, lst_c_a)
    lst_c_b = [0 for _ in range(26)]

    ptr_b_s = 0
    ptr_b_e = ptr_a_e - ptr_a_s + 1

    for idx_b in range(ptr_b_e):
        lst_c_b[ord(str_b[idx_b]) - ord('a')] += 1

    is_ = False
    for _ in range(len(str_b) - (ptr_a_e - ptr_a_s + 1)):
        print(ptr_b_s, ptr_b_e, lst_c_b)
        is_sub = True

        for idx_c in range(26):
            if lst_c_a[idx_c] == lst_c_b[idx_c]:
                pass
            else:
                is_sub = False
                break
        if is_sub:
            is_ = True
            break
        else:
            lst_c_b[ord(str_b[ptr_b_s]) - ord('a')] -= 1
            ptr_b_s += 1
            if ptr_b_e < len(str_b):
                lst_c_b[ord(str_b[ptr_b_e]) - ord('a')] += 1
            ptr_b_e += 1

    print()
    ptr_a_e += 1
    if ptr_a_e < len(str_a):
        lst_c_a[ord(str_a[ptr_a_e]) - ord('a')] += 1
    if not is_:
        lst_c_a[ord(str_a[ptr_a_s]) - ord('a')] -= 1
        ptr_a_s += 1
    elif ptr_a_e - ptr_a_s + 1 > len(str_b):
        break

print(ptr_a_e - ptr_a_s)

exit()
