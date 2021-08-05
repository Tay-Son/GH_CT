import sys

grd_ = []
que_ = []

lst_set_row = [set() for _ in range(9)]
lst_set_col = [set() for _ in range(9)]
lst_set_blk = [set() for _ in range(9)]

for idx_row in range(9):
    lst_temp = list(map(int,list(sys.stdin.readline()[:9])))
    for idx_col in range(9):
        if lst_temp[idx_col] == 0:
            que_.append([idx_row, idx_col])

        idx_blk = idx_row // 3 * 3 + idx_col // 3

        lst_set_row[idx_row].add(lst_temp[idx_col])
        lst_set_col[idx_col].add(lst_temp[idx_col])
        lst_set_blk[idx_blk].add(lst_temp[idx_col])

    grd_.append(lst_temp)


def func(idx_que):
    if idx_que == len(que_):
        return True
    else:
        idx_row, idx_col = que_[idx_que]
        idx_blk = idx_row // 3 * 3 + idx_col // 3
        is_ = False
        for cand_ in range(1, 10):
            if cand_ not in lst_set_row[idx_row]:
                if cand_ not in lst_set_col[idx_col]:
                    if cand_ not in lst_set_blk[idx_blk]:
                        lst_set_row[idx_row].add(cand_)
                        lst_set_col[idx_col].add(cand_)
                        lst_set_blk[idx_blk].add(cand_)
                        grd_[idx_row][idx_col] = cand_

                        if func(idx_que + 1) == True:
                            return True

                        grd_[idx_row][idx_col] = 0
                        lst_set_row[idx_row].remove(cand_)
                        lst_set_col[idx_col].remove(cand_)
                        lst_set_blk[idx_blk].remove(cand_)

        return False


func(0)

for each_ in grd_:
    print(''.join(map(str, each_)))