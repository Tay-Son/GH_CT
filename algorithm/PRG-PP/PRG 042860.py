def solution(name):
    ptr_r = -1
    ptr_l = 1

    for idx_ in range(1, len(name)):
        if name[idx_] != 'A':
            ptr_r = idx_

    while ptr_r >

    while ptr_l < len(name) and name[ptr_l] == 'A':
        ptr_l += 1
    if ptr_l == len(name):
        ptr_l = 0

    print(ptr_r, ptr_l)

    return min(ptr_r, len(name) - ptr_l) + sum([min(ord(chr_) - ord('A'), ord('Z') - ord(chr_) + 1) for chr_ in name])


print(solution("JAAAAA"))
