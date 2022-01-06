import sys

for _ in range(int(sys.stdin.readline())):
    str_com = sys.stdin.readline().rstrip()
    N_ = int(sys.stdin.readline())
    if N_:
        lst_ = list(map(int, sys.stdin.readline().rstrip()[1:-1].split(",")))
    else:
        sys.stdin.readline()
        lst_ = []

    is_ = True
    ptr_a = 0
    ptr_b = N_

    for each_com in str_com:
        if each_com == 'R':
            is_ = not is_
        else:
            if is_:
                ptr_a += 1
            else:
                ptr_b -= 1

    if ptr_a <= ptr_b:
        if is_:
            print('[' + ','.join(map(str, lst_[ptr_a:ptr_b])) + ']')
        else:
            print('[' + ','.join(map(str, reversed(lst_[ptr_a:ptr_b]))) + ']')
    else:
        print('error')
exit()
