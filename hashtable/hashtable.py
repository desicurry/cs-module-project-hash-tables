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

MAX_LOAD_FACTOR = 0.7
MIN_LOAD_FACTOR = 0.2


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity=MIN_CAPACITY):
        self.capacity = capacity
        self.array = [None] * capacity
        self.number_of_items = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        # Your code here
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here
        return self.number_of_items / self.capacity


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
        return hash & 0xFFFFFFF


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
        # Your code here
        index = self.hash_index(key)
        entry = self.array[index]

        if entry is None:
            self.array[index] = HashTableEntry(key, value)
            self.number_of_items += 1
            self.resize_if_needed()
            return

        while entry.next != None and entry.key != key:
            entry = entry.next

        if entry.key == key:
            entry.value = value
        else:
            entry.next = HashTableEntry(key, value)
            self.number_of_items += 1
            self.resize_if_needed()

    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        entry = self.array[index]
        prev_entry = None

        if entry is not None:
            while entry.next != None and entry.key != key:
                prev_entry = entry
                entry = entry.next
            if entry.key == key:
                if prev_entry is None:
                    self.array[index] = entry.next
                else:
                    prev_entry.next = entry.next
                self.number_of_items -= 1
                self.resize_if_needed()
                return
        print(f"Warning: Tried to delete a value from HashTable but no value exists for key: '{key}'")

    def get(self, key):
        """
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Implement this.
        """
        # Your code here
        index = self.hash_index(key)
        entry = self.array[index]

        if entry is None:
            return None

        while entry.next != None and entry.key != key:
            entry = entry.next

        return entry.value if entry.key == key else None

        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        # Your code here
    def resize_if_needed(self):
            if self.get_load_factor() > MAX_LOAD_FACTOR:
                self.resize(self.capacity * 2)
            elif self.get_load_factor() <           MIN_LOAD_FACTOR and int(self.capacity / 2) >= MIN_CAPACITY:
                self.resize(int(self.capacity / 2))

    def resize(self, new_capacity):
        old_array = self.array
        self.array = [None] * new_capacity
        self.capacity = new_capacity

        for old_entry in old_array:
            while old_entry is not None:
                key = old_entry.key
                value = old_entry.value
                index = self.hash_index(key)
                entry = self.array[index]

                # insert old key/value into resized hash table
                if entry is None:
                    self.array[index] = HashTableEntry(key, value)
                else:
                    while entry.next != None:
                        entry = entry.next
                    entry.next = HashTableEntry(key, value)

                old_entry = old_entry.next

if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
