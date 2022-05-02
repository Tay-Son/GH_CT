def solution(lst_size):
    min_w, min_h = 0, 0
    for w_, h_ in lst_size:
        if min(w_, h_) <= min_w and max(w_, h_) <= min_h:
            pass
        else:
            l_a = max(min_w, w_) * max(min_h, h_)
            l_b = max(min_w, h_) * max(min_h, w_)
            if l_a <= l_b:
                min_w = max(min_w, w_)
                min_h = max(min_h, h_)
            else:
                min_w = max(min_w, h_)
                min_h = max(min_h, w_)

            if min_w > min_h:
                min_w, min_h = min_h, min_w

    return min_h * min_w
