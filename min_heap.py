# Course: CS261 - Data Structures
# Assignment: 5
# Student: Bobby Craft  
# Description: Min Heap Implementation

# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    """
    pass


class MinHeap:

    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        """
        self.heap = DynamicArray()
        # populate MH with initial values (if provided)
        # before using this feature, implement add() method
        if start_heap:
            for node in start_heap:
                self.add(node)

    def __str__(self) -> str:
        """
        Return MH content in human-readable form
        """
        return 'HEAP ' + str(self.heap)

    def is_empty(self) -> bool:
        """
        Return True if no elements in the heap, False otherwise
        """
        return self.heap.length() == 0
    
    def add(self, node: object) -> None:
        """
        Adds new object to Heap;
        Maintains Heap properties
        """
        self.heap.append(node)

        if self.heap.length() == 1:
            return

        inserted_child = self.heap.length() - 1
        while inserted_child > 0:
            par_index = (inserted_child - 1) // 2
            if self.heap[inserted_child] >= self.heap[par_index]:
                break
            self.heap[inserted_child], self.heap[par_index] = \
                self.heap[par_index], self.heap[inserted_child]
            inserted_child = par_index

    def get_min(self) -> object:
        """
        Returns min value in Heap without removal
        """
        if self.is_empty():
            raise MinHeapException

        return self.heap[0]

    def remove_min(self) -> object:
        """
        Removes minimum element in heap;
        Returns removed value
        """
        if self.is_empty():
            raise MinHeapException

        first_element = self.heap[0]

        # Replace the value of the first element in the array with the value 
        # of the last element.
        self.heap[0] = self.heap.pop()

        # Call helper function to heapify/shift down larger values
        self.shift_down(0)

        return first_element
    
    def build_heap(self, da: DynamicArray) -> None:
        """
        Receives dynamic array with objects in any order;
        Builds proper MinHeap from them
        """

        # Assign array to heap
        self.heap = da

        # Determine start index
        i = da.length() // 2 - 1

        while i >= 0:
            self.shift_down(i)
            i -= 1

    def shift_down(self, i):
        """
        Helper function that percolates nodes down the tree
        Takes index
        """
        while (i * 2) < self.heap.length():
            mc = self.min_child(i)
            if self.heap[i] > self.heap[mc]:
                self.heap[i], self.heap[mc] = self.heap[mc], self.heap[i]
            i = mc

    def min_child(self, i):
        """
        Helper function to determine minimum child;
        Takes index
        """
        left_child = i * 2 + 1
        right_child = i * 2 + 2
        if right_child >= self.heap.length():
            return left_child
        return left_child if self.heap[left_child] <= \
            self.heap[right_child] else right_child


# BASIC TESTING
if __name__ == '__main__':
    print("\nPDF - add example 1")
    print("-------------------")
    h = MinHeap()
    print(h, h.is_empty())
    for value in range(300, 200, -15):
        h.add(value)
        print(h)
    print("\nPDF - add example 2")
    print("-------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    for value in ['monkey', 'zebra', 'elephant', 'horse', 'bear']:
        h.add(value)
        print(h)
    print("\nPDF - get_min example 1")
    print("-----------------------")
    h = MinHeap(['fish', 'bird'])
    print(h)
    print(h.get_min(), h.get_min())
    print("\nPDF - remove_min example 1")
    print("--------------------------")
    h = MinHeap([1, 10, 2, 9, 3, 8, 4, 7, 5, 6])
    while not h.is_empty():
        print(h, end=' ')
        print(h.remove_min())
    print("\nPDF - build_heap example 1")
    print("--------------------------")
    da = DynamicArray([100, 20, 6, 200, 90, 150, 300])
    h = MinHeap(['zebra', 'apple'])
    print(h)
    h.build_heap(da)
    print(h)
    da.set_at_index(0, 500)
    print(da)
    print(h)
