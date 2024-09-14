# 7 types
# List:
#  can store any data type
list=["amna",1965,12.45]
for i in list:
    print(f'list is this: {i}')
# Can del item using: del
del list[2]
for i in list:
    print(f'deleting an item from the list using del so item left: {i}')
# Concatenate list:
add=["its list 2 item",78]
list=list + add
for i in list:
    print(f'list after concatenation: {i}')
# Append method: add at the last
list.append(29)
# slicing: seperate few values: it will not take last index
sliced_list=list[1:3]
print(f'slices list is {sliced_list}')
# Testing Membership:
is_1965=1965 in list
print(f'is 1965 in the list? {is_1965}')
# Length:
length=len(list)
print(f'length of the list is {length}')
# we can also find max() and mini():
list2=[34,67,886,54,34]
print(f'maximum is {max(list2)} and minimum is {min(list2)}')
# Sorting a list:sort alphabatically
sort_list=["apple","mango","banana","grapes"]
# sort_list=sort_list.sort()
# it sorts the original list
sort_list.sort()
print('sorted list is:',sort_list)
# If you want to keep the original list unchanged and return a new sorted list, you can use the sorted() functio
sort_list = ["apple", "mango", "banana", "grapes"]
sorted_list = sorted(sort_list)  # This returns a new sorted list
print('Original list is:', sort_list)
print('Sorted list is:', sorted_list)

# insert
list.insert(2,'melon')
for i in list:
    print(i)

