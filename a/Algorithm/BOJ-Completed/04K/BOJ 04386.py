import sys
import math
from itertools import combinations as cb

n_ = int(sys.stdin.readline())

lst_star = []
for _ in range(n_):
    x_, y_ = map(float, sys.stdin.readline().split())
    lst_star.append((x_, y_))

lst_edge = []
for idx_a, idx_b in cb(range(n_), 2):
    weight_ = (lst_star[idx_a][0] - lst_star[idx_b][0]) ** 2
    weight_ += (lst_star[idx_a][1] - lst_star[idx_b][1]) ** 2
    weight_ = math.sqrt(weight_)
    lst_edge.append((idx_a, idx_b, weight_))

lst_edge.sort(key=lambda x: x[2])
lst_p = [cnt_ for cnt_ in range(n_)]


def find(idx_):
    parent_ = lst_p[idx_]
    if parent_ != idx_:
        lst_p[idx_] = find(parent_)
    return lst_p[idx_]


def union(idx_a, idx_b):
    parent_a = find(idx_a)
    parent_b = find(idx_b)
    lst_p[parent_b] = parent_a


answer_ = 0.0
cnt_ = 0
for idx_a, idx_b, weight_ in lst_edge:
    if find(idx_a) != find(idx_b):
        union(idx_a, idx_b)
        answer_ += weight_
        cnt_ += 1
        if cnt_ == n_ - 1:
            break

print(answer_)