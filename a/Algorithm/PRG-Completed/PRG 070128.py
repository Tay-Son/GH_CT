def solution(lst_a, lst_b):
    return sum([val_a * val_b for val_a, val_b in zip(lst_a, lst_b)])
