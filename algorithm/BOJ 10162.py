import sys

lst_aux = [300, 60, 10]

T_ = int(sys.stdin.readline())
lst_ans = []
for aux_ in lst_aux:
    div_, T_ = divmod(T_, aux_)
    lst_ans.append(div_)
if T_:
    print(-1)
else:
    print(' '.join(map(str, lst_ans)))

exit()
