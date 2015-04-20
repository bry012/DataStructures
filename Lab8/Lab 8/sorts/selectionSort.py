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

