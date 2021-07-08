import sys
import gc

N_ = int(sys.stdin.readline())
mat_ = []
for _ in range(N_):
    mat_.append(list(map(int, sys.stdin.readline().split())))

lst_offset = [(0, -1), (0, 1), (-1, 0), (1, 0)]


def func_(thr_):
    mat_visited = [[False for _ in range(N_)] for _ in range(N_)]
    que_ = [(0, 0)]
    idx_que = 0
    while idx_que < len(que_):
        idx_c_m, idx_c_n = que_[idx_que]
        curr_height = mat_[idx_c_m][idx_c_n]
        mat_visited[idx_c_m][idx_c_n] = True
        for offset_m, offset_n in lst_offset:
            idx_t_m = idx_c_m + offset_m
            idx_t_n = idx_c_n + offset_n
            if 0 <= idx_t_m < N_ and 0 <= idx_t_n < N_:
                target_height = mat_[idx_t_m][idx_t_n]
                if not mat_visited[idx_t_m][idx_t_n] and abs(target_height - curr_height) <= thr_:
                    que_.append((idx_t_m, idx_t_n))
        idx_que += 1
    gc.collect()
    return mat_visited[N_ - 1][N_ - 1]


ptr_s = 0
ptr_e = 1000000000
while ptr_s < ptr_e:
    ptr_c = (ptr_s + ptr_e) // 2

    if not func_(ptr_c):
        ptr_s = ptr_c + 1
    else:
        ptr_e = ptr_c

print(ptr_s)

exit()
