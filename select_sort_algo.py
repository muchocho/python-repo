def select_sort(x):
    index_length = range(0, len(x)-1)

    for element in index_length:
        min_val = element
        for i in range(element+1, len(x)):
            if x[i] < x[min_val]:
                min_val = i

        if min_val != element:
            x[min_val], x[element] = x[element], x[min_val]

    return x
print(select_sort([7,5,7,3,2,4,6,8,9,3,5,1]))






