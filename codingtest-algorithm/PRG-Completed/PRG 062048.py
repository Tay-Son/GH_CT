def solution(W_, H_):
    def gcd_(val_a, val_b):
        val_a, val_b = max(val_a, val_b), min(val_a, val_b)
        if not val_b:
            return val_a
        else:
            return gcd_(val_b, val_a % val_b)

    return W_ * H_ - W_ - H_ - gcd_(W_, H_)


print(solution(8, 12))
