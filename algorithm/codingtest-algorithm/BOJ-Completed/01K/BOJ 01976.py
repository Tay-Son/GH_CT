import sys

N_ = int(sys.stdin.readline())
trs_ = sys.stdin.readline()
lst_p = [idx_ for idx_ in range(N_)]


def find_(idx_):
    temp_ = lst_p[idx_]
    if temp_ != idx_:
        temp_ = find_(temp_)
        lst_p[idx_] = temp_
    return lst_p[idx_]


def union_(idx_a, idx_b):
    p_a = find_(idx_a)
    p_b = find_(idx_b)
    lst_p[p_a] = p_b


mat_ = []
for idx_a in range(N_):
    idx_b = 0
    for is_ in map(int, sys.stdin.readline().split()):
        if is_:
            union_(idx_a, idx_b)
        idx_b += 1

lst_temp = list(map(lambda x: int(x) - 1, sys.stdin.readline().split()))
is_ = True
for each_ in lst_temp[1:]:
    if find_(each_) != find_(lst_temp[0]):
        is_ = False
        break
if is_:
    print('YES')
else:
    print('NO')

exit()
