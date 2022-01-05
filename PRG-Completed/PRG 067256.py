def solution(lst_number, main_hand):
    grd_keypad = [['1', '2', '3'],
                  ['4', '5', '6'],
                  ['7', '8', '9'],
                  ['*', '0', '#']]

    dct_coord = dict()
    for each_row, coord_row in zip(grd_keypad, range(len(grd_keypad))):
        for each_key, coord_col in zip(each_row, range(len(grd_keypad))):
            dct_coord[each_key] = (coord_row, coord_col)

    def dist_(coord_a, coord_b):
        return abs(coord_a[0] - coord_b[0]) + abs(coord_a[1] - coord_b[1])

    str_answer = ''
    c_o_l = dct_coord['*']
    c_o_r = dct_coord['#']
    for number_ in lst_number:
        c_o_t = dct_coord[str(number_)]
        if c_o_t[1] == 0:
            c_o_l = c_o_t
            str_answer += 'L'
        elif c_o_t[1] == 2:
            c_o_r = c_o_t
            str_answer += 'R'
        else:
            dist_l = dist_(c_o_l, c_o_t)
            dist_r = dist_(c_o_r, c_o_t)
            if dist_l < dist_r:
                c_o_l = c_o_t
                str_answer += 'L'
            elif dist_r < dist_l:
                c_o_r = c_o_t
                str_answer += 'R'
            else:
                if main_hand == 'right':
                    c_o_r = c_o_t
                    str_answer += 'R'
                else:
                    c_o_l = c_o_t
                    str_answer += 'L'

    return str_answer
