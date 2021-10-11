import sys

num_input = int(sys.stdin.readline())
que_ = []
for _ in range(num_input):
    lst_input = sys.stdin.readline().split()

    if lst_input[0] == 'push':
        que_.append(lst_input[1])

    elif lst_input[0] == 'pop':
        if len(que_):
            print(que_.pop(0))
        else:
            print(-1)

    elif lst_input[0] == 'size':
        print(len(que_))

    elif lst_input[0] == 'empty':
        if not len(que_):
            print(1)
        else:
            print(0)
    elif lst_input[0] == 'front':
        if len(que_):
            print(que_[0])
        else:
            print(-1)

    elif lst_input[0] == 'back':
        if len(que_):
            print(que_[-1])
        else:
            print(-1)