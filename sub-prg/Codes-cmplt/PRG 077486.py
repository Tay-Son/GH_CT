def solution(lst_enroll, lst_referral, lst_seller, lst_amount):
    dct_m = dict()
    dct_b = dict()

    for slave_, master_ in zip(lst_enroll, lst_referral):
        dct_m[slave_] = master_
        dct_b[slave_] = 0

    for slave_, cnt_sales in zip(lst_seller, lst_amount):
        benefit_ = 100 * cnt_sales
        curr_ = slave_

        while dct_m[curr_] != '-' and benefit_:
            temp_ = int(benefit_ * 0.1)
            dct_b[curr_] += benefit_ - temp_
            benefit_ = temp_
            curr_ = dct_m[curr_]
        temp_ = int(benefit_ * 0.1)
        dct_b[curr_] += benefit_ - temp_

    lst_answer = []
    for slave_ in lst_enroll:
        lst_answer.append(dct_b[slave_])

    return lst_answer


print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
               ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
               ["young", "john", "tod", "emily", "mary"],
               [12, 4, 2, 5, 10]))
