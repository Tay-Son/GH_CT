import sys

N_ = int(sys.stdin.readline())
lst_a = list(map(int, sys.stdin.readline().split()))
lst_b = list(map(int, sys.stdin.readline().split()))

if 1 < N_:
    ptr_ = 0
    while lst_b[ptr_] != lst_a[0]:
        ptr_ += 1

    if lst_b[(ptr_ + 1) % N_] == lst_a[1]:
        for num_ in range(2, N_):
            if not lst_b[(ptr_ + num_) % N_] == lst_a[num_]:
                print("bad puzzle")
                break
        else:
            print("good puzzle")
    elif lst_b[(ptr_ - 1) % N_] == lst_a[1]:
        for num_ in range(2, N_):
            if not lst_b[(ptr_ - num_) % N_] == lst_a[num_]:
                print("bad puzzle")
                break
        else:
            print("good puzzle")
    else:
        print("bad puzzle")
else:
    print("good puzzle")

exit()
