# In DSA importing array is necessary:
import array
# Creating an array:
my_array=array.array('i',[1,2,3,4,5])
print('Original array: ',my_array)
# Accessing elements:
print('First element: ',my_array[0])
print('Second Element: ',my_array[-1]) #-1 provide value of last index
# Adding elements:
my_array.append(6)
print('Array after appending 6: ',my_array)
# Inserting Elements:
my_array.insert(0,0)
print('Array after inserting 0 at index 0',my_array)
# Removing elements:
my_array.remove(3)
print('Array after removing 3',my_array)
# Popping elements:
popped_element=my_array.pop()
#pop=> remove last element
print(f'popped element is {popped_element}')
print('Array after popping the last element: ',my_array)
# Slicing Array:
sliced_array=my_array[1:4]
print('Sliced array 2 to 4 element: ',sliced_array)
# Array catenation:
another_array=array.array('i',[7,8,9])
concatenated_array=my_array + another_array
print('Concatenated array ',concatenated_array )
# Reversing array:
my_array.reverse()
print('Array after reversing: ',my_array)
# Length of array:
print('Length of array: ',len(my_array))
# Iterating over the array:
print('Iterating over the array: ')
for element in my_array:
    print(element,end='')
print()
# Demonstrating_type constrain:
try:
    my_array.append('a')
except   TypeError as e:
    print('Error: arrays have type constrains can not add ')
# Using array module's method:
# print('Buffer info address and size: ',my_array.buffer_info)
print('Count of element 2 in array: ',my_array.count(2))
#Array to list conversion:
array_to_list=my_array.tolist()
print('Array converted to list: ',array_to_list)

