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

