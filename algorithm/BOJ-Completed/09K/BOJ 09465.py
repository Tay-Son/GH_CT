import sys

num_tc = int(sys.stdin.readline())
for _ in range(num_tc):
    lst_ = []
    len_ = int(sys.stdin.readline())
    lst_.append(list(map(int, sys.stdin.readline().split())))
    lst_.append(list(map(int, sys.stdin.readline().split())))

    lst_answer = [[0, lst_[0][0]],[0, lst_[1][0]]]
    if len_ > 1:
        lst_answer[0].append(lst_[0][1] + lst_answer[1][1])
        lst_answer[1].append(lst_[1][1] + lst_answer[0][1])
    if len_ > 2:
        for cnt_ in range(2, len_):
            lst_answer[0].append(lst_[0][cnt_] + max(lst_answer[1][cnt_], lst_answer[1][cnt_ - 1]))
            lst_answer[1].append(lst_[1][cnt_] + max(lst_answer[0][cnt_], lst_answer[0][cnt_ - 1]))

    print(max(lst_answer[0][-1], lst_answer[1][-1]))