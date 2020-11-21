def sort(sequence):
    length = len(sequence)
    if length <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    items_greater = []
    items_lower = []

    for item in sequence:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return sort(items_lower) + [pivot] + sort(items_greater)

print(sort([3,5,7,3,4,1,2,3,7]))





