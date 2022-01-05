def solution(lst_dir):
    lst_set = [set(), set()]
    dct_offset = {'U': (1, 0, 0), 'D': (-1, 0, 0), 'R': (0, 1, 1), 'L': (0, -1, 1)}

    c_c = 0
    c_r = 0
    for dir_ in lst_dir:
        o_c, o_r, idx_set = dct_offset[dir_]
        t_c, t_r = c_c + o_c, c_r + o_r
        if abs(t_c) <= 5 and abs(t_r) <= 5:
            lst_set[idx_set].add((min(c_c, t_c), min(c_r, t_r)))
            c_c, c_r = t_c, t_r

    return sum(map(lambda x: len(x), lst_set))
