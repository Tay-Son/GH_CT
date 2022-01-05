def solution(N_, lst_a, lst_b):
    lst_answer = []
    for val_a, val_b in zip(lst_a, lst_b):
        str_bin = bin(val_a | val_b)[2:]
        str_bin = '0' * (N_ - len(str_bin)) + str_bin
        lst_answer.append(''.join(['#' if each_ == '1' else ' ' for each_ in str_bin]))
    return lst_answer
