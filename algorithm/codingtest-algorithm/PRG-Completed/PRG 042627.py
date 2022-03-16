def solution(lst_job):
    import heapq as hq

    lst_job.sort()
    ptr_job = 0
    hqu_ = []
    time_total = 0
    time_current = 0

    while ptr_job < len(lst_job) or hqu_:
        while ptr_job < len(lst_job) and lst_job[ptr_job][0] <= time_current:
            hq.heappush(hqu_, (lst_job[ptr_job][1], lst_job[ptr_job][0]))
            ptr_job += 1

        if not hqu_:
            time_start, time_elapsed = lst_job[ptr_job]
            time_current = time_start + time_elapsed
            time_total += time_elapsed
            ptr_job += 1

        else:
            time_elapsed, time_start = hq.heappop(hqu_)
            time_current += time_elapsed
            time_total += time_current - time_start

    return time_total // len(lst_job)