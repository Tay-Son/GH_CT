import sys
import heapq as hq

N_ = int(sys.stdin.readline())
mat_height = []
for _ in range(N_):
    mat_height.append(list(map(int, sys.stdin.readline().split())))
mat_is_visited = [[False for _ in range(N_)] for _ in range(N_)]

lst_offset = [(0, 1), (0, -1), (1, 0), (-1, 0)]
max_diff = 0
hqu_ = [(0, 0, 0)]

while not mat_is_visited[N_ - 1][N_ - 1]:
    diff_height, idx_curr_n, idx_curr_m = hq.heappop(hqu_)
    max_diff = max(max_diff, diff_height)
    if not mat_is_visited[idx_curr_n][idx_curr_m]:
        mat_is_visited[idx_curr_n][idx_curr_m] = True

        for offset_m, offset_n in lst_offset:
            idx_target_n = idx_curr_n + offset_n
            idx_target_m = idx_curr_m + offset_m

            if 0 <= idx_target_n < N_ and 0 <= idx_target_m < N_ \
                    and not mat_is_visited[idx_target_n][idx_target_m]:
                diff_height = abs(mat_height[idx_curr_n][idx_curr_m] -
                                  mat_height[idx_target_n][idx_target_m])
                hq.heappush(hqu_, (diff_height, idx_target_n, idx_target_m))

print(max_diff)
