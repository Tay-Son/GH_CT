import sys
from collections import deque
num_com = int(sys.stdin.readline())

deq_ = deque()
for _ in range(num_com):
    lst_com = sys.stdin.readline().split()

    if lst_com[0] == 'push_front':
        deq_.appendleft(lst_com[1])
    elif lst_com[0] == 'push_back':
        deq_.append(lst_com[1])
    elif lst_com[0] == 'pop_front':
        if len(deq_) > 0:
            print(deq_.popleft())
        else:
            print(-1)
    elif lst_com[0] == 'pop_back':
        if len(deq_) > 0:
            print(deq_.pop())
        else:
            print(-1)
    elif lst_com[0] == 'size':
        print(len(deq_))
    elif lst_com[0] == 'empty':
        if len(deq_) == 0:
            print(1)
        else:
            print(0)
    elif lst_com[0] == 'front':
        if len(deq_) > 0:
            print(deq_[0])
        else:
            print(-1)
    elif lst_com[0] == 'back':
        if len(deq_) > 0:
            print(deq_[-1])
        else:
            print(-1)