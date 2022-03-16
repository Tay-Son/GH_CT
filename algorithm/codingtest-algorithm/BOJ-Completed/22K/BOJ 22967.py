import sys

N_ = int(sys.stdin.readline())

grp_ = [[] for _ in range(N_+1)]
for _ in range(N_-1):
    idx_a, idx_b = map(int,sys.stdin.readline().split())
    grp_[idx_a].append(idx_b)
    grp_[idx_b].append(idx_a)

def dfs_(lst_iv,idx_s,depth_):
    lst_iv[idx_s] = depth_
    depth_ += 1
    for idx_e in grp_[idx_s]:
        if not lst_iv[idx_e]:
            dfs_(lst_iv,idx_e,depth_)

lst_iv = [0 for _ in range(N_)]
dfs_(lst_iv,0,0)



exit()