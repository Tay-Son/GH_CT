import sys

lst_tri = list(map(str, range(ord('a'), ord('z') + 1)))
tri_t = [0] + [-1 for _ in range(len(lst_tri))]


def idx(chr_):
    return ord(chr_) - ord('a') + 1


def add(tri_, str_):
    idx_curr = 0
    for each_ in str_:
        idx_temp = idx(each_)
        if tri_[idx_curr][idx_temp] == -1:
            tri_[idx_curr][idx_temp] = len(tri_)
            tri_.append(tri_t.copy())
            tri_[idx_curr][0] += 1
        idx_curr = tri_[idx_curr][idx_temp]
    tri_[idx_curr][0] += 1


def find(tri_, str_):
    cnt_ = 1
    idx_curr = tri_[0][idx(str_[0])]
    for each_ in str_[1:]:
        if tri_[idx_curr][0] != 1:
            cnt_ += 1
        idx_temp = idx(each_)
        idx_curr = tri_[idx_curr][idx_temp]
    return cnt_


input_ = sys.stdin.readline()
while input_:
    N_ = int(input_)
    lst_ = []
    tri_ = [tri_t.copy()]
    for _ in range(N_):
        str_input = sys.stdin.readline().rstrip()
        lst_.append(str_input)
        add(tri_, str_input)
    cnt_ = 0
    for each_ in lst_:
        cnt_ += find(tri_, each_)
    print(format(cnt_ / N_, '.2f'))

    input_ = sys.stdin.readline()

exit()
