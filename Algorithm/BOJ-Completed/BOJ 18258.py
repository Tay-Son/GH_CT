import sys
from collections import deque

deq_ = deque()
lst_ans = []
for _ in range(int(sys.stdin.readline())):
    lst_input = sys.stdin.readline().split()
    if lst_input[0] == 'push':
        deq_.append(int(lst_input[1]))
    elif lst_input[0] == 'pop':
        if deq_:
            lst_ans.append(deq_.popleft())
        else:
            lst_ans.append(-1)
    elif lst_input[0] == 'size':
        lst_ans.append(len(deq_))
    elif lst_input[0] == 'empty':
        if not deq_:
            lst_ans.append(1)
        else:
            lst_ans.append(0)
    elif lst_input[0] == 'front':
        if deq_:
            lst_ans.append(deq_[0])
        else:
            lst_ans.append(-1)
    elif lst_input[0] == 'back':
        if deq_:
            lst_ans.append(deq_[-1])
        else:
            lst_ans.append(-1)

print('\n'.join(map(str, lst_ans)))

exit()