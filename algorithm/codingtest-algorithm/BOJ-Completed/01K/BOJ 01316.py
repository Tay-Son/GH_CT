num_input = int(input())
answer = 0
for _ in range(num_input):
    str_input = input()
    is_ = True
    set_ = set()
    for each_chr in str_input:
        if each_chr not in set_:
            set_.add(each_chr)
            past_ = each_chr
        else:
            if not each_chr == past_:
                is_ = False
                break
    if is_:
        answer += 1
print(answer)