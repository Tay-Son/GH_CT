def solution(str_target):
    N_ = len(str_target)
    answer = 0
    min_move = N_ - 1

    for idx_, char in enumerate(str_target):
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)
        target_ = idx_ + 1
        while target_ < N_ and str_target[target_] == 'A':
            target_ += 1
        min_move = min(min_move, 2 * idx_ + N_ - target_, idx_ + 2 * (N_ - target_))
    answer += min_move
    return answer
