num_input = int(input())
lst_answer = [0, 1, 1, 1, 2]
for _ in range(num_input):
    input_ = int(input())

    while len(lst_answer) < input_ + 1:
        lst_answer.append(lst_answer[-1] + lst_answer[-5])
    print(lst_answer[input_])
