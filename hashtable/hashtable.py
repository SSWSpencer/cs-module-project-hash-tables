class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity):
        # Your code here
        self.array = [None] * capacity
        self.capacity = capacity


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return len(self.array)

    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """

        # Your code here


    def djb2(self, key):
        """
        DJB2 hash, 32-bit

        Implement this, and/or FNV-1.
        """
        # Your code here
        hash = 5381
        for x in key:
            hash = (( hash << 5) + hash) + ord(x)
        return hash & 0xFFFFFFFF



    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        #return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        #Your code here
        entry = HashTableEntry(key, value)
        if self.array[self.hash_index(key)] is None:
            self.array[self.hash_index(key)] = entry
        else:
            current = self.array[self.hash_index(key)]
            if current.key == key:
                current.value = entry.value
            inserted = False
            while current.next is not None:
                if current.key == key:
                    current.value = entry.value
                current = current.next
                
            current.next = entry

            




    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        if self.array[self.hash_index(key)] is not None:
            if self.array[self.hash_index(key)].key == key:
                self.array[self.hash_index(key)] = self.array[self.hash_index(key)].next
            elif self.array[self.hash_index(key)].next is not None:
                if self.array[self.hash_index(key)].next.next is None:
                    self.array[self.hash_index(key)].next = None




    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        if self.array[self.hash_index(key)]:
            if self.array[self.hash_index(key)].next is None and self.array[self.hash_index(key)] == key:
                return self.array[self.hash_index(key)].value
            else:
                current = self.array[self.hash_index(key)]
                while current is not None:
                    if(current.key == key):
                        return current.value
                    else:
                        current = current.next
        else:
            return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
        oldArr = self.array
        self.array = [None] * new_capacity
        for x in range(0, len(oldArr)):
            current = oldArr[x]
            self.put(current.key, current.value)
            while current.next is not None:
                current = current.next
                self.put(current.key, current.value)



if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("key-0", "val-0")
    ht.put("key-1", "val-1")
    ht.put("key-2", "val-2")
    ht.put("key-3", "val-3")
    ht.put("key-4", "val-4")
    ht.put("key-5", "val-5")
    ht.put("key-6", "val-6")
    ht.put("key-7", "val-7")
    ht.put("key-8", "val-8")
    ht.put("key-9", "val-9")

    ht.put("key-0", "new-val-0")
    ht.put("key-1", "new-val-1")
    ht.put("key-2", "new-val-2")
    ht.put("key-3", "new-val-3")
    ht.put("key-4", "new-val-4")
    ht.put("key-5", "new-val-5")
    ht.put("key-6", "new-val-6")
    ht.put("key-7", "new-val-7")
    ht.put("key-8", "new-val-8")
    ht.put("key-9", "new-val-9")

    print("")

    # Test storing beyond capacity
    for i in range(1, 11):
        print(ht.get(f"key-{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"key-{i}"))

    print("")
