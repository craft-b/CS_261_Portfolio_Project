# Course: CS261 - Data Structures
# Assignment: 5
# Student: Bobby Craft  
# Description: Min Heap Implementation

# Import pre-written DynamicArray and LinkedList classes
from a5_include import *


class MinHeapException(Exception):
    """
    Custom exception to be used by MinHeap class
    DO NOT CHANGE THIS CLASS IN ANY WAY
    """
    pass


class MinHeap:

    def __init__(self, start_heap=None):
        """
        Initializes a new MinHeap
        DO NOT CHANGE THIS METHOD IN ANY WAY
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
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return 'HEAP ' + str(self.heap)

    def is_empty(self) -> bool:
        """
        Return True if no elements in the heap, False otherwise
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        return self.heap.length() == 0
    
    def add(self, node: object) -> None:
        """
        Adds new object to Heap;
        Maintains Heap properties
        """

        # Put new element at the end of the array.
        self.heap.append(node)

        if self.heap.length() == 1:
            return

        else:
            # Compute the inserted element’s parent index((i - 1) / 2).
            par_index = (((self.heap.length()-1)-1)//2)
            inserted_child = self.heap.length() - 1

            # Compare the value of the inserted element with the value of its parent.
            while self.heap[inserted_child] < self.heap[par_index]:
                self.heap[inserted_child], self.heap[par_index] = self.heap[par_index], self.heap[inserted_child]
                inserted_child = par_index
                if inserted_child == 0:
                    return
                par_index = ((inserted_child - 1)//2)
            return

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

        # Replace the value f the first element in the array with the value of the last element and
        self.heap[0] = self.heap[self.heap.length() - 1]

        # Remove the last element.
        self.heap.pop()

        # Starting index
        i = 0

        # If the array is not empty(i.e., it started with more than one element)
        if not self.is_empty():

            # Compute the indices of the children of the replacement element (2 * i + 1 and 2 * i + 2).
            left_child = (2 * i) + 1
            right_child = (2 * i) + 2

            if right_child >= self.heap.length() and left_child >= self.heap.length():
                return first_element

            # Call helper function to heapify/shift down
            # larger values
            self.shift_down(i)

            return first_element
        return first_element

    def build_heap(self, da: DynamicArray) -> None:
        """
        Receives dynamic array with objects in any order;
        Builds proper MinHeap from them
        """

        # Assign array to heap
        self.heap = da

        # Determine start index
        i = (da.length() // 2) - 1

        while (i > -1):
            self.shift_down(i)
            i = i - 1

    def shift_down(self, i):
        """
        Helper function that percolates nodes down the tree
        Takes index
        """
        while (i * 2) <= self.heap.length():

            mc = self.min_child(i)

            if i * 2 + 2 >= self.heap.length() and i * 2 + 1 >= self.heap.length():
                return

            if self.heap[i] > self.heap[mc]:
                tmp = self.heap[i]
                self.heap[i] = self.heap[mc]
                self.heap[mc] = tmp

            i = mc

    def min_child(self, i):
        """
        Helper function to determine minimum child;
        Takes index
        """

        # right child >= length, left child only leaf node
        if i * 2 + 2 >= self.heap.length() and i * 2 + 1 < self.heap.length():
            return i * 2 + 1

        # left child >= length, right child only leaf
        if i * 2 + 2 < self.heap.length() and i * 2 + 1 >= self.heap.length():
            return i * 2 + 2

        # both children are nodes
        if i * 2 + 2 < self.heap.length() and i * 2 + 1 < self.heap.length():

            if self.heap[i * 2 + 1] <= self.heap[i * 2 + 2]:
                return i * 2 + 1

            if self.heap[i * 2 + 2] <= self.heap[i * 2 + 1]:
                return i * 2 + 2

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