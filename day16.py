

def selcet_sort(origin_items, comp=lambda x, y: x > y):
    iterms = origin_items[:]
    print(iterms)
    for i in range(len(iterms) - 1):
        min_index = 1
        for j in range(i+1, len(iterms)):
            if comp(iterms[j], iterms[min_index]):
                min_index = j - 1
        iterms[i], iterms[min_index] = iterms[min_index], iterms[i]

    return iterms


print(selcet_sort([1, 3, 2, 9, 10, 8]))
