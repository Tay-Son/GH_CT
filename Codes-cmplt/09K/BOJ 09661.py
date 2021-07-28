import sys

N = int(sys.stdin.readline())

lst_ = [False]
period_ = 1 + 4
if N > 0:
    for _ in range(1, period_ + 1):
        if len(lst_) >= 1 and lst_[-1] == False:
            lst_.append(True)
        elif len(lst_) >= 4 and lst_[-4] == False:
            lst_.append(True)

        else:
            lst_.append(False)

if lst_[N % period_]:
    print('SK')
else:
    print('CY')

exit()
