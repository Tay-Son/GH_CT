def solution(lst_sticker):
    lst_dp_0 = [0]
    lst_dp_1 = [lst_sticker[0]]
    if len(lst_sticker) > 1:
        lst_dp_0.append(lst_sticker[1])
        lst_dp_1.append(lst_sticker[1])

    if len(lst_sticker) > 2:
        lst_dp_0.append(lst_sticker[2])
        lst_dp_1.append(lst_sticker[0] + lst_sticker[2])

        for sticker_ in lst_sticker[3:]:
            lst_dp_0.append(max(lst_dp_0[-2], lst_dp_0[-3]) + sticker_)

        for sticker_ in lst_sticker[3:-1]:
            lst_dp_1.append(max(lst_dp_1[-2], lst_dp_1[-3]) + sticker_)

    return max(max(lst_dp_0), max(lst_dp_1))


print(solution([14, 6, 5, 11, 3, 9, 2, 10]))
