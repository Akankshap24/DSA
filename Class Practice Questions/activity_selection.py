def activity_selection_greedy(activities):
    activities.sort(key=lambda x: x[1])
    end = 0
    count = 0
    for start, finish in activities:
        if start >= end:
            count += 1
            end = finish
    return count