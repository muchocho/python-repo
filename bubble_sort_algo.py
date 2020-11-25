def bub(list):
    in_len = len(list) - 1
    sort = False

    while not sort:
        sort = True
        for i in range(0, in_len):
            if list[i] > list[i+1]:
                sort = False
                list[i], list[i+1] = list[i + 1], list[i]

    return list

print(bub([2,8,9,7,3,1,6,5,4]))
