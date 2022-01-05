num_input = input()
lst_input = map(int, input().split())
answer = 0
for each_input in lst_input:
    if each_input == 1:
        is_ = False
    else:
        is_ = True
        for cnt_ in range(2, each_input):
            if not each_input % cnt_:
                is_ = False
                break
    if is_:
        answer += 1
print(answer)
