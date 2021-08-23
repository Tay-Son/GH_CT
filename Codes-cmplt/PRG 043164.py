def solution(lst_ticket):
    dct_ = dict()
    dct_ticket = dict()
    for str_s, str_e in lst_ticket:
        if (str_s, str_e) not in dct_ticket:
            dct_ticket[(str_s, str_e)] = 1
        else:
            dct_ticket[(str_s, str_e)] += 1

        if str_s not in dct_:
            dct_[str_s] = []
        dct_[str_s].append(str_e)
    for lst_ in dct_.values():
        lst_.sort()

    stk_ = ['ICN']

    def dfs_(str_s):
        if len(stk_) == len(lst_ticket) + 1:
            return True
        else:
            if str_s in dct_:
                for str_e in dct_[str_s]:
                    if dct_ticket[(str_s, str_e)]:
                        dct_ticket[(str_s, str_e)] -= 1
                        stk_.append(str_e)
                        if dfs_(str_e):
                            return True
                        stk_.pop()
                        dct_ticket[(str_s, str_e)] += 1
            return False

    dfs_('ICN')

    return stk_


print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
