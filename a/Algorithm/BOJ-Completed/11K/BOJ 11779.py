import sys
import heapq as hq

INF_ = 10 ** 9

N_ = int(sys.stdin.readline())
M_ = int(sys.stdin.readline())

grp_ = [[] for _ in range(N_ + 1)]
lst_distance = [INF_ for _ in range(N_ + 1)]
lst_p = [-1 for _ in range(N_ + 1)]
lst_is_visited = [False for _ in range(N_ + 1)]

for _ in range(M_):
    idx_s, idx_e, weight_ = map(int, sys.stdin.readline().split())
    grp_[idx_s].append((idx_e, weight_))

S_, E_ = map(int, sys.stdin.readline().split())

hqu_ = [(0, S_)]
lst_distance[S_] = 0

while hqu_:
    distance_, idx_s = hq.heappop(hqu_)

    if not lst_is_visited[idx_s]:
        lst_is_visited[idx_s] = True
        for idx_e, weight_ in grp_[idx_s]:
            temp_ = distance_ + weight_
            if temp_ < lst_distance[idx_e]:
                lst_distance[idx_e] = temp_
                hq.heappush(hqu_, (temp_, idx_e))
                lst_p[idx_e] = idx_s

lst_answer = [E_]
idx_curr = E_
while lst_p[idx_curr] != -1:
    p_ = lst_p[idx_curr]
    lst_answer.append(p_)
    idx_curr = p_
lst_answer.reverse()

print(lst_distance[E_])
print(len(lst_answer))
print(' '.join(map(str, lst_answer)))

exit()
