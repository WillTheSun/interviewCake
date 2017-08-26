# Sort by start time
# for...
#   if t.start <= prev.end
#       update prev
#   else
#       result += prev
#       t = prev


def merge_ranges(times):
    times = sorted(times, key=lambda t: t[0])
    mergedTimes = []
    prev = times[0]

    for t in times[1:]:
        if t[0] <= prev[1]:
              prev = (prev[0],max(prev[1], t[1]))
        else:
            mergedTimes.append(prev)
            prev = t
    mergedTimes.append(prev)

    return mergedTimes

times =         [(1, 10), (2, 6), (3, 5), (7, 9)]
# ->   [(0, 1), (3, 8), (9, 12)]
merged = merge_ranges(times)
print(merged)
