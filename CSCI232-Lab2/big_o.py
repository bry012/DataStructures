__author__ = 'bryan'
from timeit import Timer

def constant(lists):
    return len(lists)

def logarithmic(lists):
    if len(lists) == 1:
        return lists[0]
    else:
        return logarithmic(lists[:len(lists)//2])


def linearSum(lists):
    sums = 0
    for x in lists:
        sums += x
    return sums

def square(lists):
    squares = []
    for num in lists:
        sums = 0
        for nums in range(num):
            sums += num
        squares.append(sums)
    return squares



def cubic(lists):
    squares = []
    for num in lists:
        sums = 0
        for nums in range(num):
            for nums in range(num):
                sums += num
        squares.append(sums)
    return squares



t1 = Timer(stmt="constant(range(100))", setup="from __main__ import constant")
t2 = Timer(stmt="logarithmic(range(100))", setup="from __main__ import logarithmic")
t3 = Timer(stmt="linearSum(range(100))", setup="from __main__ import linearSum")
t4 = Timer(stmt="square(range(100))", setup="from __main__ import square")
t5 = Timer(stmt="cubic(range(100))", setup="from __main__ import cubic")

print("Printing time for 'constant(range(100))'\n" + str(t1.timeit(1000)))
print("Printing time for 'logarithmic(range(100))'\n" + str(t2.timeit(1000)))
print("Printing time for 'linearSum(range(100))'\n" + str(t3.timeit(1000)))
print("Printing time for 'square(range(100))'\n" + str(t4.timeit(1000)))
print("Printing time for 'cubic(range(100))'\n" + str(t5.timeit(1000)))