def solution(lst_grd):
    lst_aux = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    grd_ = None
    grd_iv = None

    def rec_(idx_r, idx_c, depth_):
        if depth_ > 2:
            return False
        elif depth_ > 0 and grd_[idx_r][idx_c] == 1:
            return True
        else:
            grd_iv[idx_r][idx_c] = True
            depth_ += 1
            for offset_r, offset_c in lst_aux:
                target_r = idx_r + offset_r
                target_c = idx_c + offset_c
                if 0 <= target_r < 5 and \
                        0 <= target_c < 5 and \
                        grd_[target_r][target_c] != -1 and \
                        not grd_iv[target_r][target_c]:
                    if rec_(target_r, target_c, depth_):
                        return True

    lst_answer = []
    for each_ in lst_grd:
        grd_ = []
        lst_t = []
        for str_, cnt_r in zip(each_, range(5)):
            lst_ = []
            for chr_, cnt_c in zip(str_, range(5)):
                if chr_ == 'P':
                    lst_.append(1)
                    lst_t.append((cnt_r, cnt_c))
                elif chr_ == 'O':
                    lst_.append(0)
                else:
                    lst_.append(-1)
            grd_.append(lst_)

        is_ = True
        for idx_s_r, idx_s_c in lst_t:
            grd_iv = [[False for _ in range(5)] for _ in range(5)]
            if rec_(idx_s_r, idx_s_c, 0):
                is_ = False
                break

        lst_answer.append(int(is_))

    return lst_answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
