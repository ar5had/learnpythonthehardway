def median(nos):
    nos = sorted(nos)
    mid = len(nos) / 2
    print nos, mid
    if len(nos) % 2 == 1:
        return nos[mid]
    else:
        print nos[mid], nos[mid - 1]
        return (nos[mid] + nos[mid - 1]) / 2

print median([4, 5, 5, 4])
