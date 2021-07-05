import sys

str_a = sys.stdin.readline().rstrip() + 'a'
str_b = sys.stdin.readline().rstrip() + 'a'

offset_max = min(len(str_a), len(str_b)) - 1

lst_a = [0 for _ in range(26)]

ptr_a = 0
ptr_b = 0
offset_ = 1
lst_a[ord(str_a[0]) - ord('a')] = 1

while ptr_a + offset_ < len(str_a) - 1 and offset_ < offset_max:
    is_ = False

    lst_b = [0 for _ in range(26)]
    for ptr_b in range(len(str_b) - offset_):
        for idx_ in range(ptr_b, ptr_b + offset_):
            lst_b[ord(str_b[idx_]) - ord('a')] += 1

        is_hit = True
        for idx_ in range(26):
            if lst_a[idx_] != lst_b[idx_]:
                is_hit = False
                break
        if is_hit:
            is_ = True
            break
        lst_b[ord(str_b[ptr_b]) - ord('a')] -= 1
        lst_b[ord(str_b[ptr_b + offset_-1]) - ord('a')] += 1

    if is_:
        offset_ += 1
        chr_target = str_a[ptr_a+offset_]
        idx_target = ord(chr_target) - ord('a')
        lst_a[idx_target] += 1
    else:
        chr_target = str_a[ptr_a]
        idx_target = ord(chr_target) - ord('a')
        lst_a[idx_target] -= 1

        ptr_a += 1

        chr_target = str_a[ptr_a + offset_-1]
        idx_target = ord(chr_target) - ord('a')
        lst_a[idx_target] += 1

print(offset_ - 1)

exit()
