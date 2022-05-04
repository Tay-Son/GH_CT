def solution(N_):
    lst_ = ['1', '2', '4']
    str_ans = ''

    while N_:
        N_, mod_ = divmod(N_ - 1, 3)
        str_ans = lst_[mod_] + str_ans

    return str_ans


for N_ in [1, 2, 3, 4]:
    print(solution(N_))

for N_ in range(100):
    print(N_, solution(N_))
