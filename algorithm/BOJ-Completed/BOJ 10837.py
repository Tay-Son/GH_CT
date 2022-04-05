import sys

K_ = int(sys.stdin.readline())
sys.stdin.readline()
lst_ans = []
for input_ in sys.stdin.readlines():
    # M_, N_ = map(int, sys.stdin.readline().split())
    M_, N_ = map(int, input_.split())
    if M_ > N_:
        if (K_ - M_) + N_ + 2 < M_:
            lst_ans.append('0')
        else:
            lst_ans.append('1')
    elif M_ < N_:
        if (K_ - N_) + M_ + 1 < N_:
            lst_ans.append('0')
        else:
            lst_ans.append('1')
    else:
        lst_ans.append('1')
print('\n'.join(lst_ans))

exit()
