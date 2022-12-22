# Course: CS261 - Data Structures
# Assignment: 5
# Student: Bobby Craft
# Description: Hash-map implementation


# Import pre-written DynamicArray and LinkedList classes
from a5_include import *

def hash_function_1(key: str) -> int:
    """
    Sample Hash function #1 to be used with A5 HashMap implementation
    DO NOT CHANGE THIS FUNCTION IN ANY WAY
    """
    hash = 0
    for letter in key:
        hash += ord(letter)
    return hash

def hash_function_2(key: str) -> int:
    """
    Sample Hash function #2 to be used with A5 HashMap implementation
    DO NOT CHANGE THIS FUNCTION IN ANY WAY
    """
    hash, index = 0, 0
    index = 0
    for letter in key:
        hash += (index + 1) * ord(letter)
        index += 1
    return hash

    
class HashMap:

    def __init__(self, capacity: int, function) -> None:
        """
        Init new HashMap based on DA with SLL for collision resolution
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.buckets = DynamicArray()
        for _ in range(capacity):
            self.buckets.append(LinkedList())
        self.capacity = capacity
        self.hash_function = function
        self.size = 0

    def __str__(self) -> str:
        """
        Return content of hash map t in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = ''
        for i in range(self.buckets.length()):
            list = self.buckets.get_at_index(i)
            out += str(i) + ': ' + str(list) + '\n'
        return out
        
    def clear(self) -> None:
        """
        Clears Hash Table without changing underlying capacity
        """
        for i in range(self.buckets.length()):
            if self.buckets.data[i].size != 0:
                self.buckets.data[i].head = None
                self.buckets.data[i].size = 0
        self.size = 0
        
    def get(self, key: str) -> object:
        """
        Returns value associated with given key;
        Returns None if key isn't in Hash Map
        """
        # Compute the elements bucket
        hash = self.hash_function(key)
        index = hash % self.capacity

        ll = self.buckets.data[index]

        for node in ll:
            if node.key == key:
                return node.value
        return None

    def put(self, key: str, value: object) -> None:
        """
        Updates the key / value pair in the hash map.
        If a given key already exists in the hash map,
        its associated value should be replaced with the
        new value. If a given key is not in the hash map,
        a key / value pair is be added
        """

        hash = self.hash_function(key)
        pos = hash % self.buckets.length()

        bucket = self.buckets[pos]

        if bucket.head is None:
            bucket.insert(key, value)
            self.size += 1
            return

        elif bucket.contains(key) is not None:
            target = bucket.contains(key)
            target.value = value

        else:
            bucket.insert(key, value)
            self.size += 1
        
    def remove(self, key: str) -> None:
        """
        Removes given key and associated value;
        Does nothing if key isn't found
        """
        # Compute the elements bucket
        hash = self.hash_function(key)
        index = hash % self.buckets.length()

        list = self.buckets.get_at_index(index)

        if list.head is None:
            return None

        prev, cur = None, list.head

        while cur is not None:
            if cur.key == key:
                if prev:
                    prev.next = cur.next
                else:
                    list.head = cur.next
                self.size -= 1
            prev, cur = cur, cur.next

    def contains_key(self, key: str) -> bool:
        """
        Returns True if the given key is in the hash map,
        otherwise it returns False. An empty hash map does
        not contain any keys
        """
        # Compute the elements bucket
        hash = self.hash_function(key)
        index = hash % self.capacity

        linked_list = self.buckets.data[index] 

        for node in linked_list:
            if node.key == key:
                return True
        return False

    def empty_buckets(self) -> int:
        """
        Returns no. of empty buckets in Hash Table
        """

        count = 0

        for i in range(self.buckets.length()):

            list = self.buckets.get_at_index(i)

            if list.head is None:
                count += 1

        return count

    def table_load(self) -> float:
        """
        Returns current load factor
        """
        return float(self.size/(self.capacity))
    
    def resize_table(self, new_capacity: int) -> None:
        """
        Changes capacity he internal hash table.
        If new_capacity is less than 1, this method does nothing.
        """
        if new_capacity < 1:
            return

        # Create new larger table
        n_map = HashMap(new_capacity, hash_function_1)

        # Transfer data from old map to new map
        for i in range(self.buckets.length()):

            list = self.buckets.get_at_index(i)
            cur = list.head

            while cur is not None:
                hash = self.hash_function(cur.key)
                pos = hash % n_map.buckets.length()
                transfer = n_map.buckets[pos]
                transfer.insert(cur.key, cur.value)
                cur = cur.next

        self.capacity = n_map.capacity
        self.buckets = n_map.buckets

    def get_keys(self) -> DynamicArray:
        """
        Returns Dynamic Array that contains
        all of stored keys in the Hash Map
        """
        # create empty DA
        da_keys = DynamicArray()

        # Starting at beginning of DA, Traverse buckets
        for i in range(self.buckets.length()):

            # If bucket has linked list, traverse LL for keys - 
            # starting at head until end of linked list

            da_ll = self.buckets.get_at_index(i)
            da_ll_head = da_ll.head

            while da_ll_head is not None:
                da_keys.append(da_ll_head.key)
                da_ll_head = da_ll_head.next

        # When end of old array reached, return new DA
        return da_keys



# BASIC TESTING
if __name__ == "__main__":
    print("\nPDF - empty_buckets example 1")
    print("-----------------------------")
    m = HashMap(100, hash_function_1)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key1', 10)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key2', 20)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key1', 30)
    print(m.empty_buckets(), m.size, m.capacity)
    m.put('key4', 40)
    print(m.empty_buckets(), m.size, m.capacity)
    print("\nPDF - empty_buckets example 2")
    print("-----------------------------")
    m = HashMap(50, hash_function_1)
    for i in range(150):
        m.put('key' + str(i), i * 100)
        if i % 30 == 0:
            print(m.empty_buckets(), m.size, m.capacity)
    print("\nPDF - table_load example 1")
    print("--------------------------")
    m = HashMap(100, hash_function_1)
    print(m.table_load())
    m.put('key1', 10)
    print(m.table_load())
    m.put('key2', 20)
    print(m.table_load())
    m.put('key1', 30)
    print(m.table_load())
    print("\nPDF - table_load example 2")
    print("--------------------------")
    m = HashMap(50, hash_function_1)
    for i in range(50):
        m.put('key' + str(i), i * 100)
        if i % 10 == 0:
            print(m.table_load(), m.size, m.capacity)
    print("\nPDF - clear example 1")
    print("---------------------")
    m = HashMap(100, hash_function_1)
    print(m.size, m.capacity)
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key1', 30)
    print(m.size, m.capacity)
    m.clear()
    print(m.size, m.capacity)
    print("\nPDF - clear example 2")
    print("---------------------")
    m = HashMap(50, hash_function_1)
    print(m.size, m.capacity)
    m.put('key1', 10)
    print(m.size, m.capacity)
    m.put('key2', 20)
    print(m.size, m.capacity)
    m.resize_table(100)
    print(m.size, m.capacity)
    m.clear()
    print(m.size, m.capacity)
    print("\nPDF - put example 1")
    print("-------------------")
    m = HashMap(50, hash_function_1)
    for i in range(150):
        m.put('str' + str(i), i * 100)
        if i % 25 == 24:
            print(m.empty_buckets(), m.table_load(), m.size, m.capacity)
    print("\nPDF - put example 2")
    print("-------------------")
    m = HashMap(40, hash_function_2)
    for i in range(50):
        m.put('str' + str(i // 3), i * 100)
        if i % 10 == 9:
            print(m.empty_buckets(), m.table_load(), m.size, m.capacity)
    print("\nPDF - contains_key example 1")
    print("----------------------------")
    m = HashMap(10, hash_function_1)
    print(m.contains_key('key1'))
    m.put('key1', 10)
    m.put('key2', 20)
    m.put('key3', 30)
    print(m.contains_key('key1'))
    print(m.contains_key('key4'))
    print(m.contains_key('key2'))
    print(m.contains_key('key3'))
    m.remove('key3')
    print(m.contains_key('key3'))
    print("\nPDF - contains_key example 2")
    print("----------------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 20)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.size, m.capacity)
    result = True
    for key in keys:
        # all inserted keys must be present
        result &= m.contains_key(str(key))
        # NOT inserted keys must be absent
        result &= not m.contains_key(str(key + 1))
    print(result)
    print("\nPDF - get example 1")
    print("-------------------")
    m = HashMap(30, hash_function_1)
    print(m.get('key'))
    m.put('key1', 10)
    print(m.get('key1'))
    print("\nPDF - get example 2")
    print("-------------------")
    m = HashMap(150, hash_function_2)
    for i in range(200, 300, 7):
        m.put(str(i), i * 10)
    print(m.size, m.capacity)
    for i in range(200, 300, 21):
        print(i, m.get(str(i)), m.get(str(i)) == i * 10)
        print(i + 1, m.get(str(i + 1)), m.get(str(i + 1)) == (i + 1) * 10)
    print("\nPDF - remove example 1")
    print("----------------------")
    m = HashMap(50, hash_function_1)
    print(m.get('key1'))
    m.put('key1', 10)
    print(m.get('key1'))
    m.remove('key1')
    print(m.get('key1'))
    m.remove('key4')
    print("\nPDF - resize example 1")
    print("----------------------")
    m = HashMap(20, hash_function_1)
    m.put('key1', 10)
    print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))
    m.resize_table(30)
    print(m.size, m.capacity, m.get('key1'), m.contains_key('key1'))
    print("\nPDF - resize example 2")
    print("----------------------")
    m = HashMap(75, hash_function_2)
    keys = [i for i in range(1, 1000, 13)]
    for key in keys:
        m.put(str(key), key * 42)
    print(m.size, m.capacity)
    for capacity in range(111, 1000, 117):
        m.resize_table(capacity)
        m.put('some key', 'some value')
        result = m.contains_key('some key')
        m.remove('some key')
        for key in keys:
            result &= m.contains_key(str(key))
            result &= not m.contains_key(str(key + 1))
        print(capacity, result, m.size, m.capacity, round(m.table_load(), 2))
    print("\nPDF - get_keys example 1")
    print("------------------------")
    m = HashMap(10, hash_function_2)
    for i in range(100, 200, 10):
        m.put(str(i), str(i * 10))
    print(m.get_keys())
    m.resize_table(1)
    print(m.get_keys())
    m.put('200', '2000')
    m.remove('100')
    m.resize_table(2)
    print(m.get_keys())