from timeit import Timer
import sorts.bubbleSort, sorts.insertionSort, sorts.mergeSort, sorts.quickSort, sorts.selectionSort, sorts.shellSort, sorts.bi_bubbleSort
import random
class benchmark(object):
    def __init__(self):
        pass

    def create_benchmark(self, function_list, numlist):
        for funct in function_list:
            t = Timer(stmt="sorts." + funct.__name__ + "." + funct.__name__ + "(" + str(numlist) + ")", setup="import sorts." + funct.__name__ + ", random")
            print("Printing time for '" + funct.__name__ + "(list)'\n" + str(t.timeit(10)))

B = benchmark()
B.create_benchmark([sorts.bubbleSort.bubbleSort, sorts.insertionSort.insertionSort,sorts.mergeSort.mergeSort, sorts.quickSort.quickSort, \
                    sorts.selectionSort.selectionSort,sorts.shellSort.shellSort, sorts.bi_bubbleSort.bi_bubbleSort], [int(500*random.random()) for i in range(500)])


