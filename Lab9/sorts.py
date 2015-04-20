def radix_sort(item_list, base=10):
    num_passes = max([num_digits(num) for num in item_list])
    a_list = item_list[:]
    for digit_num in range(num_passes):
        a_list = merge(split(a_list, base, digit_num))
    return a_list

def make_blanks(size):
    return [[] for num in range(size)]

def num_digits(num):
    return len(str(num))

def split(item_list, base, digit_num):
    buckets = make_blanks(base)
    for num in item_list:
        buckets[get_digit(num, base, digit_num)].append(num)
    return buckets

def merge(item_list):
    a_list = []
    for sublist in item_list:
        a_list.extend(sublist)
    return a_list

def get_digit(num, base, digit_num):
    return (num // base ** digit_num) % base


def bubbleSort(alist):
    # Loop for the total number of passes (n-1)
    # Each pass will generate a decreasing passnum for the next loop
    for passnum in range(len(alist)-1,0,-1):
        # Loop through the range of the pass
        for i in range(passnum):
            # If this item is greater than the next item
            if alist[i]>alist[i+1]:
                # Swap items (could have used shorter Python syntax)
                # alist[i], alist[i+1]=alist[i+1], alist[i]
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
    return alist


def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i<len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j<len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1

def insertionSort(alist):
    # Loop through the length of the list
    for index in range(1,len(alist)):
        # Get the current value of this index
        currentvalue = alist[index]
        # Store the position
        position = index

        # Loop while the position is greater than zero
        # and the item before the current position is greater than current value
        while position>0 and alist[position-1]>currentvalue:
            # Move the item in position one space over
            alist[position]=alist[position-1]
            # Move to the next position
            position = position-1

        # Copy the current value into its correct location
        alist[position]=currentvalue

def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper( alist,first,last):
    if first<last:

        splitpoint = partition(alist,first,last)

        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
    pivotvalue = alist[first]

    leftmark = first+1
    rightmark = last

    done = False
    while not done:

        while leftmark <= rightmark and \
                alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1

        while alist[rightmark] >= pivotvalue and \
                rightmark >= leftmark:
            rightmark = rightmark -1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp


    return rightmark


def selectionSort(alist):
    # Loop for the total number of passes (n-1)
    # Each pass will generate a decreasing passnum for the next loop
    for fillslot in range(len(alist)-1,0,-1):
        # Create variable to hold where the position is
        positionOfMax=0
        # Loop through the correct items for the pass
        for location in range(1,fillslot+1):
            # If this item is greater than the max for this pass
            if alist[location]>alist[positionOfMax]:
                # Store the position of this item
                positionOfMax = location

        # Swap the max item encountered to proper position
        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp
    return alist

def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist,startposition,sublistcount)

        sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):

        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap

        alist[position]=currentvalue

def python_sort(alist):
    alist.sort()
    return alist

if __name__ == "__main__":
    print(radix_sort([5,3,100,4,29,189,34],10))
