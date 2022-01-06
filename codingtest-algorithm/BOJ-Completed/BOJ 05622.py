lst_ = [3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 10, 10, 10, 10]

answer = 0
input_ = input()
for each_chr in input_:
    answer += lst_[ord(each_chr) - ord('A')]
print(answer)