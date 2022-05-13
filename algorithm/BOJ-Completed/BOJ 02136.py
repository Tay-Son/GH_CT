# import sys
#
# N_, L_ = map(int, sys.stdin.readline().split())
#
# lst_d_l = []
# lst_d_r = []
# lst_u = []
# cnt_l = 0
#
# for id_ in range(1, N_ + 1):
#     val_ = int(sys.stdin.readline())
#     lst_u.append([id_, val_])
# lst_u.sort(key=lambda x: abs(x[1]))
#
# cnt_l = 0
# for idx_ in range(N_):
#     id_, val_ = lst_u[idx_]
#     lst_u[idx_].append(cnt_l)
#     if val_ < 0:
#         lst_d_l.append(abs(val_))
#     else:
#         lst_d_r.append(L_ - val_)
#         cnt_l += 1
#
# cnt_r = 0
# for idx_ in range(N_ - 1, -1, -1):
#     id_, val_, cnt_l = lst_u[idx_]
#     lst_u[idx_].append(cnt_r)
#     if val_ < 0:
#         cnt_r += 1
#
# lst_d_l.sort(reverse=True)
# lst_d_r.sort(reverse=True)
#
# max_t = 0
# max_id = 0
# for idx_ in range(N_):
#     id_, val_, cnt_l, cnt_r = lst_u[idx_]
#     if 0 < val_:
#         if cnt_l >= cnt_r:
#             t_ = lst_d_r.pop()
#         else:
#             t_ = lst_d_l.pop()
#     else:
#         if cnt_l <= cnt_r:
#             t_ = lst_d_l.pop()
#         else:
#             t_ = lst_d_r.pop()
#     if t_ > max_t:
#         max_t = t_
#         max_id = id_
# print(max_id, max_t)
# exit()

import sys

N_, L_ = map(int, sys.stdin.readline().split())

lst_d_l = []
lst_d_r = []
lst_u = []
cnt_l = 0

for id_ in range(1, N_ + 1):
    val_ = int(sys.stdin.readline())
    lst_u.append([id_, val_])
lst_u.sort(key=lambda x: abs(x[1]))
print(lst_u)

cnt_l = 0
for idx_ in range(N_):
    id_, val_ = lst_u[idx_]
    lst_u[idx_].append(cnt_l)
    if val_ < 0:
        lst_d_l.append(abs(val_))
        # cnt_l = max(0, cnt_l - 1)
        # cnt_l -= 1
    else:
        lst_d_r.append(L_ - val_)
        cnt_l += 1
print(lst_u)

cnt_r = 0
for idx_ in range(N_ - 1, -1, -1):
    id_, val_, cnt_l = lst_u[idx_]
    lst_u[idx_].append(cnt_r)
    if val_ < 0:
        cnt_r += 1
    else:
        # cnt_r = max(0, cnt_r - 1)
        # cnt_r -= 1
        pass
print(lst_u)

lst_d_l.sort(reverse=True)
lst_d_r.sort()
print(lst_d_l)
print(lst_d_r)

max_t = 0
max_id = 0
for idx_ in range(N_):
    id_, val_, cnt_l, cnt_r = lst_u[idx_]
    if 0 < val_:
        if cnt_l >= cnt_r:
            t_ = lst_d_r.pop()
        else:
            t_ = lst_d_l.pop()
    else:
        if cnt_l <= cnt_r:
            t_ = lst_d_l.pop()
        else:
            t_ = lst_d_r.pop()
    if t_ > max_t:
        max_t = t_
        max_id = id_
    print(id_, val_, cnt_l, cnt_r, t_)
print(max_id, max_t)
exit()

import sys

N_, L_ = map(int, sys.stdin.readline().split())
lst_ = []
cnt_ = 0

lst_d_l = []
lst_d_r = []

for _ in range(N_):
    pos_, id_ = map(int, sys.stdin.readline().split())
    lst_.append([id_])
    lst_[-1].append(cnt_)
    if 0 < id_:
        lst_d_l.append(L_ - pos_ + 1)
        cnt_ += 1
    else:
        lst_d_r.append(pos_ + 1)
lst_d_l.sort()
lst_d_r.sort(reverse=True)

cnt_c = 0
for idx_ in range(N_ - 1, -1, -1):
    lst_[idx_].append(cnt_c)
    if lst_[idx_][0] < 0:
        cnt_c += 1

for idx_ in range(N_):
    id_, cnt_, cnt_c = lst_[idx_]
    if 0 < id_:
        if cnt_ >= cnt_c:
            lst_[idx_].append(lst_d_l.pop())
        else:
            lst_[idx_].append(lst_d_r.pop())

    else:
        if cnt_ > cnt_c:
            lst_[idx_].append(lst_d_l.pop())
        else:
            lst_[idx_].append(lst_d_r.pop())

lst_.sort(key=lambda x: x[0])
lst_.sort(key=lambda x: x[-1])
print(lst_[K_ - 1][0])

exit()
