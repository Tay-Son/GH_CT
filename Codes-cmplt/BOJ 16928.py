import sys

N_ = int(sys.stdin.readline())

if N_ ** .5 == int(N_ ** .5):
    print(1)
else:
    lst_ = [num_ * num_ for num_ in range(1, int(N_ ** .5) + 1)]
    lst_sub = []
    for val_a in lst_:
        is_run = True
        for val_b in lst_:
            temp_ = val_a + val_b
            if temp_ < N_:
                lst_sub.append(temp_)
            elif temp_ == N_:
                print(2)
                is_run = False
                break
            else:
                break
        if not is_run:
            break
    else:
        for val_a in lst_sub:
            is_run = True
            for val_b in lst_:
                temp_ = val_a + val_b
                if temp_ < N_:
                    pass
                elif temp_ == N_:
                    print(3)
                    is_run = False
                    break
                else:
                    break
            if not is_run:
                break


        else:
            print(4)
exit()
