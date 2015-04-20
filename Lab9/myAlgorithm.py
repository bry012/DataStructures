import sorts,random
to_sort = [int(20*random.random()) for i in range(20)]
print("Unsorted List:" + str(to_sort))
sorted_list = sorts.radix_sort(to_sort)
print("Sorted List:" + str(sorted_list))
