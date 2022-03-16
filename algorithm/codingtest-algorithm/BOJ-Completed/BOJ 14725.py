import sys

tri_ = [dict()]


def dfs(idx_, depth_):
    for key_, value_ in sorted(tri_[idx_].items()):
        print('--' * depth_, end='')
        print(key_)
        dfs(value_, depth_ + 1)


for _ in range(int(sys.stdin.readline())):
    lst_input = sys.stdin.readline().split()
    idx_curr = 0
    for each_ in lst_input[1:]:
        if each_ not in tri_[idx_curr]:
            tri_[idx_curr][each_] = len(tri_)
            tri_.append(dict())
        idx_curr = tri_[idx_curr][each_]

dfs(0, 0)

exit()