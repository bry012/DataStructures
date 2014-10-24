# This class provides a basic implementation
# of the map ADT
class HashTable:
    # Initial the class
    def __init__(self):
        # The size will be 11 items
        self.size = 11
        # Create lists to store the slots and the data
        self.slots = [None] * self.size
        self.data = [None] * self.size
        self.load_factor = self.size * (1/4.0)

    def has_reached_load_factor(self):
        num_nones = len([slot for slot in self.slots if slot == None])
        if num_nones <= self.load_factor:
            return True
        else:
            return False

    def increase_hash_table(self):
        growth_factor = 0.75
        num_to_increase = int(self.size * growth_factor)
        self.slots += [None] * num_to_increase
        self.data += [None] * num_to_increase

    # Add an item to the hashtable by key/data
    def put(self,key,data):
        if self.has_reached_load_factor():
            self.increase_hash_table()

        # Create the hashvalue
        hashvalue = self.hashfunction(key,len(self.slots))

        # If slot is empty
        if self.slots[hashvalue] == None:
            # Store the key/data
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            # If the slot contains this key
            if self.slots[hashvalue] == key:
                # Replace the data
                self.data[hashvalue] = data
            else:
                # Get the slot after the current slot
                nextslot = self.rehash(hashvalue,len(self.slots))
                # Loop until an empty slot is found
                while self.slots[nextslot] != None and \
                      self.slots[nextslot] != key:

                    # Get the next slot
                    nextslot = self.rehash(nextslot,len(self.slots))

                    # Check if the next slot is empty
                    if self.slots[nextslot] == None:
                        # Store the key/data
                        self.slots[nextslot]=key
                        self.data[nextslot]=data
                    else:
                        # Replace the data
                        self.data[nextslot] = data

    # Returns the hashvalue based on a given key and size of table
    def hashfunction(self,key,size):
        # Create the hashvalue using the remainder method
        return key%size

    # Rehash, creating a new hashvalue
    def rehash(self,oldhash,size):
        return (oldhash+1)%size

    # Returns an item with the given key
    def get(self,key):
        # Find the starting slot
        startslot = self.hashfunction(key,len(self.slots))

        # Create variables for looping
        data = None
        stop = False
        found = False
        position = startslot

        # While the slot is not equal to None
        # and we haven't found the item and the stop flag is not true
        while self.slots[position] != None and  \
                         not found and not stop:
            # If this slot matches the key
            if self.slots[position] == key:
               found = True
               # Get the data from the slot
               data = self.data[position]
            else:
                # Get the next position by rehashing
                position=self.rehash(position,len(self.slots))
            # If the algorithm has looped back to its starting slot
            if position == startslot:
                # Stop looping, the item wasn't found
                stop = True
        return data

    # Allows access by []
    def __getitem__(self,key):
        return self.get(key)

    # Allows access by []
    def __setitem__(self,key,data):
        self.put(key,data)

H=HashTable()
H[54]="cat"
H[26]="dog"
H[93]="lion"
H[17]="tiger"
H[77]="bird"
H[31]="cow"
H[44]="goat"
H[55]="pig"
H[20]="chicken"
print(H.slots)
print(H.data)
print(len(H.slots),len(H.data))
H[10]="lemar"
H[80]="fox"
H[45]="sheep"
H[32] = "deer"
print(H.slots)
print(H.data)
print(len(H.slots),len(H.data))
