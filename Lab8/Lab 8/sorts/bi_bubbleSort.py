def bi_bubbleSort(alist):
    # Loop for the total number of passes (n-1)
    # Each pass will generate a decreasing passnum for the next loop
    for passnum in range(len(alist)-1,0,-1):
        # Loop through the range of the pass
        if passnum % 2 == 0:
            for i in range(passnum):
                # If this item is greater than the next item
                if alist[i]>alist[i+1]:
                    # Swap items (could have used shorter Python syntax)
                    # alist[i], alist[i+1]=alist[i+1], alist[i]
                    temp = alist[i]
                    alist[i] = alist[i+1]
                    alist[i+1] = temp
        else:
            for i in range(1,passnum+1):
                # If this item is greater than the next item
                if alist[-i]<alist[-i-1]:
                    # Swap items (could have used shorter Python syntax)
                    # alist[i], alist[i+1]=alist[i+1], alist[i]
                    temp = alist[-i]
                    alist[-i] = alist[-i-1]
                    alist[-i-1] = temp
    return alist



