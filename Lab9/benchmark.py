import sorts,csv,random
from timeit import Timer
class benchmark(object):
    def __init__(self):

        self.function_list = [sorts.bubbleSort, sorts.insertionSort, sorts.mergeSort,\
              sorts.quickSort, sorts.radix_sort, sorts.selectionSort, sorts.shellSort,\
              sorts.python_sort]

    def create_benchmark(self,  numlist):
        benchmark_list = []
        for funct in self.function_list:
            t = Timer(stmt="sorts." + funct.__name__ + "(" + str(numlist) + ")", setup="import sorts")
            benchmark_list.append(t.timeit(10))
        return benchmark_list

B = benchmark()
benchmark_list = [["Bubble", "Insertion", "Merge", "Quick", "Radix", "Selection", "Shell", "python"]]
for i in range(1,501):
    benchmark_list.append(B.create_benchmark([int(i*random.random()) for i in range(i)]))
with open("runtimes.csv","w", newline='\n') as csvfile:
    for lists in benchmark_list:
        aWriter = csv.writer(csvfile, delimiter=',')
        aWriter.writerow(lists)
