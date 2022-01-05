def solution(brown, yellow):
    brown //= 2
    brown -= 2

    for cnt_v in range(1, brown // 2 + 1):
        cnt_h = brown - cnt_v
        if cnt_h * cnt_v == yellow:
            return [cnt_h + 2, cnt_v + 2]
    return
