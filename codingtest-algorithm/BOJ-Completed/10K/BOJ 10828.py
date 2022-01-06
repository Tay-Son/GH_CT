import sys

num_input_line = int(sys.stdin.readline())

stk_ = []
for _ in range(num_input_line):
    lst_func = sys.stdin.readline().split()
    if lst_func[0] == 'push':
        stk_.append(int(lst_func[1]))

    elif lst_func[0] == 'pop':
        if len(stk_) > 0:
            print(stk_.pop(-1))
        else:
            print(-1)

    elif lst_func[0] == 'size':
        print(len(stk_))

    elif lst_func[0] == 'empty':
        if len(stk_) > 0:
            print(0)
        else:
            print(1)

    elif lst_func[0] == 'top':
        if len(stk_) > 0:
            print(stk_[-1])
        else:
            print(-1)