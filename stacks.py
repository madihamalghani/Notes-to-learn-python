#Stacks: LIFO =>last in first out
# Queues: FIFO=>First in first out

# =============Stacks operations in python==================#
# Creation of stack:
stack=[]
# Functions to push an element onto the stack:
def push(stack, element):
    stack.append(element)
    print(f'Pushed {element} onto the stack')

# Function to check if the stack is empty:
def is_empty(stack):
    return len(stack) == 0

# Function to pop an element from the stack:
def pop(stack):
    if not is_empty(stack):
        element = stack.pop()
        print(f'Popped {element} from the stack')
        return element
    else:
        print('Stack is empty')

# Function to peek at the top element of the stack:
def peak(stack):
    if not is_empty(stack):
        print(f'Peak element is {stack[-1]}')
        return stack[-1]
    else:
        print('Stack is empty')
def stack_length(stack):
    length=len(stack)
    print(f'Stack length is {length}')
    return length

# Example usage:
peak(stack)
push(stack, 1)
push(stack, 2)
peak(stack)
pop(stack)
pop(stack)
pop(stack)  # Trying to pop from an empty stack

stack_length(stack)