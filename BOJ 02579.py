num_input = int(input())
lst_stair = []
for _ in range(num_input):
    lst_stair.append(int(input()))
lst_stair.reverse()

lst_answers = [lst_stair[0]]
if num_input > 1:
    lst_answers.append(lst_stair[0] + lst_stair[1])
if num_input > 2:
    lst_answers.append(lst_stair[0] + lst_stair[2])
if num_input > 3:
    for cnt_ in range(3, num_input):
        val_a = lst_stair[cnt_] + lst_stair[cnt_ - 1] + lst_answers[cnt_ - 3]
        val_b = lst_stair[cnt_] + lst_answers[cnt_ - 2]
        lst_answers.append(max(val_a, val_b))

if num_input > 1:
    print(max(lst_answers[-1], lst_answers[-2]))
else:
    print(lst_answers[0])