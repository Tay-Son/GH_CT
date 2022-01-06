def solution(lst_line):
    lst_ = []

    for line_ in lst_line:
        trs_, s_, r_ = line_.split()
        lst_s = s_.split(':')
        s_ = int(lst_s[0]) * 60 * 60 * 1000
        s_ += int(lst_s[1]) * 60 * 1000
        s_ += int(''.join(lst_s[2].split('.')))

        r_ = int(float(r_[:-1]) * 1000)

        lst_.append((s_, -1))
        lst_.append((s_ - r_ - 1000, 1))
        print(s_, r_)

    lst_.sort(key=lambda x: x[1])
    lst_.sort()

    max_ = 0
    curr_ = 0
    for trs_, val_ in lst_:
        curr_ += val_
        max_ = max(max_, curr_)

    print(lst_)

    return max_


print(solution(["2016-09-15 20:59:57.421 0.351s",
                "2016-09-15 20:59:58.233 1.181s",
                "2016-09-15 20:59:58.299 0.8s",
                "2016-09-15 20:59:58.688 1.041s",
                "2016-09-15 20:59:59.591 1.412s",
                "2016-09-15 21:00:00.464 1.466s",
                "2016-09-15 21:00:00.741 1.581s",
                "2016-09-15 21:00:00.748 2.31s",
                "2016-09-15 21:00:00.966 0.381s",
                "2016-09-15 21:00:02.066 2.62s"]))
