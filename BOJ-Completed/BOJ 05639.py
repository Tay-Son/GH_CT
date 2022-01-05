import sys

sys.setrecursionlimit(10 ** 5)

dct_ = dict()
root_ = int(sys.stdin.readline())
dct_[root_] = ['.', '.']

while True:
    try:
        input_ = int(sys.stdin.readline())
        temp_ = root_

        while temp_ != '.':
            curr_ = temp_
            if input_ < curr_:
                idx_sub = 0
            elif curr_ < input_:
                idx_sub = 1
            temp_ = dct_[curr_][idx_sub]

        dct_[curr_][idx_sub] = input_
        dct_[input_] = ['.', '.']

    except:
        break


def func(s_):
    if s_ != '.':
        l_, r_ = dct_[s_]
        func(l_)
        func(r_)
        print(s_)


func(root_)
