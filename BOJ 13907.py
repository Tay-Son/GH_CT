import sys
import heapq as hq

INF_ = 1000000007

N_, M_, K_ = map(int, sys.stdin.readline().split())
S_, D_ = map(lambda x: int(x) - 1, sys.stdin.readline().split())

grp_ = [[] for _ in range(N_)]
for _ in range(M_):
    a_, b_, dist_ = map(int, sys.stdin.readline().split())
    a_, b_ = a_ - 1, b_ - 1
    grp_[a_].append((b_, dist_))
    grp_[b_].append((a_, dist_))

grd_dist = [[INF_ for _ in range(N_)] for _ in range(N_)]
grd_dist[S_][0] = 0
hqu_ = [(0, 0, S_)]

while hqu_:
    tot_dist, tot_mov, idx_s = hq.heappop(hqu_)
    if idx_s != D_:
        for mov_ in range(tot_mov):
            if grd_dist[idx_s][mov_] < tot_dist:
                break
        else:
            tot_mov += 1
            if tot_mov < N_:
                for idx_e, dist_ in grp_[idx_s]:
                    temp_ = tot_dist + dist_
                    if temp_ < grd_dist[idx_e][tot_mov]:
                        grd_dist[idx_e][tot_mov] = temp_
                        hq.heappush(hqu_, (temp_, tot_mov, idx_e))

lst_ = []
for idx_, val_ in enumerate(grd_dist[D_]):
    if val_ != INF_:
        lst_.append((val_, idx_))

tot_ = 0
print(min([idx_ * tot_ + val_ for val_, idx_ in lst_]))
for _ in range(K_):
    tot_ += int(sys.stdin.readline())
    print(min([idx_ * tot_ + val_ for val_, idx_ in lst_]))

exit()


# dijsta : 2차원 배열 d를 갱신시키는 함수
def dijstra(v):
    global ans
    d[v][0] = 0
    min_q = []
    min_q.append((d[v][0], v, 0))
    while len(min_q) != 0:
        distance = min_q[0][0]
        current = min_q[0][1]
        visited = min_q[0][2]
        heapq.heappop(min_q)
        flag = False
        # 불필요한 경우 1:
        # 이미 최소 거리가 있다면 굳이 정점을 더 거쳐가지 않아도 되므로
        # flag를 True로 바꿔준다
        for i in range(visited):
            if d[current][i] < distance:
                flag = True
                break
        # 불필요한 경우 2:
        # 불필요한 경우 1에서 걸려진 경우거나, 똑같이 j번째 정점을 방문해도
        # 거리가 더 작은 쪽이 유지되어야 하므로
        # 현재 거리가 배열에 저장된 거리보다 크다면 굳이 갱신이 일어나지 않는다
        if flag or d[current][visited] < distance:
            continue
        # 불필요한 경우 3:
        # 애초에 현재 정점이 도착정점이라면 굳이 다른 정점을 탐색하지 않아도 된다
        if current == end - 1:
            ans = min(ans, d[current][visited])
            continue
        for i in range(len(adj[current])):
            next = adj[current][i][0]
            nextdistance = adj[current][i][1] + distance
            # 배열 d의 범위를 벗어나지 않고 거리가 더 작다면 갱신
            if visited + 1 < vertex and nextdistance < d[next][visited + 1]:
                d[next][visited + 1] = nextdistance
                heapq.heappush(min_q, (nextdistance, next, visited + 1))
