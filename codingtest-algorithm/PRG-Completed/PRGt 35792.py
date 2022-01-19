def solution(grd_):
    from collections import deque

    R_, C_ = len(grd_), len(grd_[0])
    grd_iv = [[-1 for _ in range(C_)] for _ in range(R_)]
    que_ = deque([(1, 0, 0)])

    while que_:
        d_, i_r, i_c = que_.popleft()
        print(i_r, i_c, d_, que_)
        if grd_iv[i_r][i_c] == -1:
            grd_iv[i_r][i_c] = d_
            d_ += 1
            for o_r, o_c in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                t_r, t_c = i_r + o_r, i_c + o_c
                if 0 <= t_r < R_ and 0 <= t_c < C_ and grd_[t_r][t_c]:
                    que_.append((d_, t_r, t_c))

    return grd_iv[-1][-1]


print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
