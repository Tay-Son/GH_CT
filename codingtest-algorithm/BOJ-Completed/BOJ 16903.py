import sys

MAX_DEPTH = 30

tri_t = [-1, -1, 0]
tri_ = [[cnt_, -1, 1] for cnt_ in range(1, MAX_DEPTH + 1)]
tri_.append([-1, -1, 1])

for _ in range(int(sys.stdin.readline())):
    com_, var_ = map(int, sys.stdin.readline().split())

    if com_ == 1:
        idx_tri = 0
        tri_[idx_tri][2] += 1
        for cnt_ in range(MAX_DEPTH - 1, -1, -1):
            idx_sub, var_ = divmod(var_, 1 << cnt_)
            if tri_[idx_tri][idx_sub] == -1:
                tri_[idx_tri][idx_sub] = len(tri_)
                tri_.append(tri_t.copy())
            idx_tri = tri_[idx_tri][idx_sub]
            tri_[idx_tri][2] += 1

    elif com_ == 2:
        idx_tri = 0
        tri_[idx_tri][2] -= 1
        for cnt_ in range(MAX_DEPTH - 1, -1, -1):
            idx_sub, var_ = divmod(var_, 1 << cnt_)
            idx_tri = tri_[idx_tri][idx_sub]
            tri_[idx_tri][2] -= 1

    elif com_ == 3:
        tot_ = 0
        idx_tri = 0
        for cnt_ in range(MAX_DEPTH - 1, -1, -1):
            temp_a = 1 << cnt_
            idx_sub, var_ = divmod(var_, 1 << cnt_)
            temp_b = tri_[idx_tri][not idx_sub]
            if temp_b != -1 and tri_[temp_b][2]:
                tot_ += temp_a
                idx_tri = temp_b
            else:
                idx_tri = tri_[idx_tri][idx_sub]
        print(tot_)

exit()
