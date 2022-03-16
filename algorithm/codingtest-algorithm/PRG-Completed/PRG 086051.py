def solution(numbers):
    tot_ = 0
    for num_ in range(1, 10):
        if num_ not in numbers:
            tot_ += num_

    return tot_
