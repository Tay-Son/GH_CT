def solution(lst_money):
    lst_dp = [lst_money[0], max(lst_money[0], lst_money[1])]
    for idx_ in range(2, len(lst_money) - 1):
        lst_dp.append(max(lst_dp[-1], lst_dp[-2] + lst_money[idx_]))
    max_ = max(lst_dp)

    lst_dp = [0, lst_money[1]]
    for idx_ in range(2, len(lst_money)):
        lst_dp.append(max(lst_dp[-1], lst_dp[-2] + lst_money[idx_]))
    max_ = max(max_, max(lst_dp))

    return max_

print(solution([1, 2, 3, 1]))