from priority_queue import PriorityQueue

def test_priority_queue():

    # Create a priority queue
    queue = PriorityQueue()

    # Check if the queue is empty
    assert queue.is_empty() == True

    # Enqueue some items
    queue.enqueue("A", 3)
    queue.enqueue("B", 2)
    queue.enqueue("C", 1)

    # Check if the queue is empty
    assert queue.is_empty() == False

    # Check the size of the queue
    assert queue.size() == 3

    # Peek at the first item
    assert queue.peek() == "C"

    # Dequeue an item
    assert queue.dequeue() == "C"

    # Check the size of the queue
    assert queue.size() == 2

    # Dequeue an item
    assert queue.dequeue() == "B"

    # Dequeue an item
    assert queue.dequeue() == "A"

    # Check if the queue is empty
    assert queue.is_empty() == True

    print("All priority queue tests pass")

test_priority_queue()