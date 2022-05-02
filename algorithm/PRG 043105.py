def solution(grd_):
    for idx_r in range(1, len(grd_)):
        for idx_c in range(idx_r + 1):
            grd_[idx_r][idx_c] += max(grd_[idx_r - 1][max(0, idx_c - 1):min(idx_r, idx_c + 1)])

    return max(grd_[-1])


for grd_ in [
    [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
]:
    print(solution(grd_))
