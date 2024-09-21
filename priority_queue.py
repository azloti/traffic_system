class PriorityQueue:

    def __init__(self):
        self.heap = []

    # Helper methods
    def parent(self, index):
        return (index - 1) // 2

    # Enqueue an item with a priority (O(log n))
    def enqueue(self, item, priority):
        # Add the new element at the end
        self.heap.append((priority, item))
        # Move it up to maintain the heap property
        self._heapify_up(len(self.heap) - 1)

    # Dequeue the item with the highest priority (smallest priority value) (O(log n))
    def dequeue(self):
        if self.is_empty():
            return None
        # Swap the root with the last item
        self._swap(0, len(self.heap) - 1)
        # Remove the last item (the smallest element)
        min_item = self.heap.pop()
        # Restore the heap property by moving the new root down
        self._heapify_down(0)
        # Return the item (not the priority)
        return min_item[1]

    # Peek at the item with the highest priority without removing it (O(1))
    def peek(self):
        if self.is_empty():
            return None
        return self.heap[0][1]

    # Check if the queue is empty (O(1))
    def is_empty(self):
        return len(self.heap) == 0

    # Get the size of the queue (O(1))
    def size(self):
        return len(self.heap)

    # Heapify up (bubble up the new element to maintain heap property)
    def _heapify_up(self, index):
        while index > 0 and self.heap[self.parent(index)][0] > self.heap[index][0]:
            # Swap if the parent is larger than the current element
            self._swap(index, self.parent(index))
            index = self.parent(index)

    # Heapify down (bubble down the root to maintain heap property after dequeue)
    def _heapify_down(self, index):
        smallest = index
        left = 2 * index + 1
        right = 2 * index + 2

        # Check if left child exists and is smaller than the current smallest
        if left < len(self.heap) and self.heap[left][0] < self.heap[smallest][0]:
            smallest = left

        # Check if right child exists and is smaller than the current smallest
        if right < len(self.heap) and self.heap[right][0] < self.heap[smallest][0]:
            smallest = right

        # If the smallest element is not the current element, swap and continue heapifying
        if smallest != index:
            self._swap(index, smallest)
            self._heapify_down(smallest)

    # Swap two elements in the heap
    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
