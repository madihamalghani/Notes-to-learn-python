# Nested Loop:
for i in range(3):
# This loop will iterate over the range produced by range(3), which generates the sequence [0, 1, 2].
# The loop will assign each value from the range to the variable i in each iteration.
    for j in range(2):
        # Inside the outer loop, there is another for loop that iterates over
        #  the range produced by range(2), which generates the sequence [0, 1].
        print(f'i = {i}, j = {j}')
# In this sequence:
# Outer loop (i = 0):
# Inner loop (j = 0): print(f'i = 0, j = 0')
# Inner loop (j = 1): print(f'i = 0, j = 1')
        #  6 total iterations (3 outer loop iterations × 2 inner loop iterations).
def main():
    print('Welcome to the world of python')
if __name__=='__main__':
    main()
# main works only when you are running the script directly
def add(a, b):
    return a + b

if __name__ == '__main__':
    result = add(2, 3)
    print('The sum is:', result)
# it ensures that the function only runs when you execute the script directly.
