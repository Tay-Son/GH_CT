def solution(lst_lotto, lst_win_numbers):
    prize_min = 7
    prize_max = 1

    for each_lotto in lst_lotto:
        if each_lotto:
            if each_lotto in lst_win_numbers:
                prize_min -= 1
            else:
                prize_max += 1

    return [min(prize_max, 6), min(prize_min, 6)]


print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
