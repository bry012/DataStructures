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

