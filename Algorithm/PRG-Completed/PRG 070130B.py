def solution(lst_):
    from collections import Counter

    N_ = len(lst_)
    if N_ < 2:
        return 0
    else:
        answer_max = 0
        for target_, max_ in sorted(list(Counter(lst_).items()), key=lambda x: x[1], reverse=True):
            if max_ * 2 <= answer_max:
                break
            else:
                ptr_ = 0
                cnt_ = 0
                while ptr_ < N_ - 1:
                    if lst_[ptr_] != lst_[ptr_ + 1] and (lst_[ptr_] == target_ or lst_[ptr_+1] == target_):
                        cnt_ += 2
                        ptr_ += 2
                    else:
                        ptr_ += 1
                answer_max = max(answer_max, cnt_)

    return answer_max


print(solution([0, 3, 3, 0, 7, 2, 0, 2, 2, 0]))


def star(a, x):
    result = []
    i = 0
    while True:
        if (a[i] != a[i + 1]) and (a[i] == x or a[i + 1] == x):
            result.append(a[i])
            result.append(a[i + 1])
            i += 2
        else:
            i += 1
        if i >= len(a) - 1:
            break
    return len(result)


def solution(a):
    answer = -1
    maxs = findMax(a)
    if len(a) < 2:
        return 0
    for i in range(len(maxs)):
        if maxs[i] * 2 <= answer:
            continue
        answer = max(star(a, i), answer)
    return answer
