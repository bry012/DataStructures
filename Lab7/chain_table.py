# This class provides a basic implementation
# of the map ADT
from random import randrange
class HashTable:
    # Initial the class
    def __init__(self):
        # The size will be 11 items
        self.size = 11
        # Create lists to store the slots and the data
        self.slots = [[] for i in range(self.size)]
        self.data = [[] for i in range(self.size)]


    # Add an item to the hashtable by key/data
    def put(self,key,data):
        # Create the hashvalue
        hashvalue = self.hashfunction(key,len(self.slots))
        found = False
        for slot in self.slots[hashvalue]:
            if slot == key:
                self.data[hashvalue][self.slots[hashvalue].index(slot)] = data
                found = True
                break
        if not found:
           self.slots[hashvalue].append(key)
           self.data[hashvalue].append(data)

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
        data = None
        for value in self.slots[startslot]:
            if value == key:
                data = self.data[startslot][self.slots[startslot].index(value)]

        return data

    def remove(self,key):
        hashvalue = self.hashfunction(key,len(self.slots))
        slot = self.slots[hashvalue]
        for value in slot:
            if value == key:
                self.data[hashvalue].pop(slot.index(value))
                self.slots[hashvalue].remove(value)

    # Allows access by []
    def __getitem__(self,key):
        return self.get(key)

    # Allows access by []
    def __setitem__(self,key,data):
        self.put(key,data)

    def __delitem__(self,key):
        self.remove(key)

    def keys (self):
        return [key for slot in self.slots for key in slot]

def main():
    H=HashTable()
    while [] in H.slots:
        H[randrange(100)] = randrange(100)
    print("Filled HashTable")
    print("Slots:" + str(H.slots))
    print("Data:" + str(H.data))
    print("\nKey/Value Pairs:")
    for key in H.keys():
        print(str(key) + ":" + str(H.get(key)))
    print("")
    for key in H.keys():
        print("Deleting: " + str(key))
        del H[key]
    print("\nAfter Deleting:")
    print("Slots:" + str(H.slots))
    print("Data:" + str(H.data))


if __name__ == "__main__":
    main()
