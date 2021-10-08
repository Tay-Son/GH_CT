max_ = 0
curr_ = 0
for _ in range(4):
    a, b = map(int, input().split())
    curr_ -= a
    curr_ += b
    max_ = max(max_, curr_)
print(max_)
