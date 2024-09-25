# FIFO => First in First out
# import deque:
from collections import deque

# Initialize the queue
queue = deque([1, 2, 3])
print('Queue created: ', queue)

# Function to enqueue an element to the queue
def enqueue(queue, element):
    queue.append(element)
    print(f'Enqueued {element} to the queue')

# Function to check if the queue is empty
def is_empty(queue):
    return len(queue) == 0

# Function to dequeue an element from the queue
def dequeue(queue):
    if not is_empty(queue):
        element = queue.popleft()
        print(f'Dequeued {element} from queue')
        return element
    else:
        print('Queue is empty')
def peak(queue):
    if not is_empty(queue):
        print(f'Front Element is {queue[0]}')
        return queue[0] 
# Example usage:
enqueue(queue, 4)
dequeue(queue)
dequeue(queue)
dequeue(queue)
dequeue(queue)  # This will trigger the "Queue is empty" condition
# initialize a deque:
dq=deque([1,2,3,4,5])
print('Queue 2 is created: ',dq)
# rotate dq three steps left negative rotation:
dq.rotate(-3)
# Reverse the queue:
print('Rotate the dq queue: ',dq)
# Rotate 2 steps to right:
dq.rotate(2)
print('Rotate two steps right: ',dq)
# Reverse the deque:
dq.reverse()
print('After reversing dq:',dq)
# Remove first occurance of value 3
dq.remove(3)
print('After removing 3 from dq: ',dq)
# insert value 10 at index 2:
dq.insert(2,10)
print('After printing 10 at index 2: ',dq)

