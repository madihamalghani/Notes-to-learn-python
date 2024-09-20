# immutable: no item change 
# constant during program execution

# creating a tuple:
my_tuple=(1,2,3,4,5)
print('original tuple',my_tuple)
# Accessing elements:
print('First element',my_tuple[0])
# -1 index of last element:
print('Second Element',my_tuple[-1])
# Slicing the tuple:
print('Sliced tuple(2 to 4 element):',my_tuple[1:4])
# Repetition:
repeated_tuple=my_tuple*2
print('Repeated tuples: ',repeated_tuple)
# Membership test:
print('is three is the tuple? ',3 in my_tuple)
print('Is 6 in the tuple?', 6 in my_tuple)
# Length of tuple
print('Length of tuple: ', len(my_tuple))
# Index of an element:
print('Index of element 3: ', my_tuple.index(3))
# Count of an element:
print('count of element 2: ', my_tuple.count(2))
# Demonsonstrating immutability,try to change an element:
try:
    my_tuple[0]=10
except TypeError as e:
    print('Error: Tuples value can not be changed i.e: immutable')
# using tuple for multiple return values:
def get_person():
    name='Alice'
    age=20
    return name,age
person=get_person() #store in person
print('Name is:',person[0])
print('Age is:',person[1])


# ===============Sets====================#
# Creating a set:
my_SetA={1,2,3,4,5}
print('Original Set',my_SetA)
# Adding an Element:
my_SetA.add(6)
print('Set after adding 6:',my_SetA)
# Remove Element:
my_SetA.remove(2)
print('Set after removing 2:',my_SetA)
# Membership test:
print('Is 3 in the set?', 3 in my_SetA)
print('Is 6 in the set? ', 6 in my_SetA)
# Unions of sets:
my_SetB={4,5,6,7,8}
AunionB=my_SetA.union(my_SetB)
print('Union of set A and set B',AunionB)
# Intersection of sets:
A_intersection_B=my_SetA.intersection(my_SetB)
print('intersection of set a with set b',A_intersection_B)
# Difference of set A and set B
A_differ_B=my_SetA.difference(my_SetB)
print('Difference of set A and set B',A_differ_B)
# Symmetric Difference of set:
symmetric_difference=my_SetA.symmetric_difference(my_SetB)
print('Symmetric difference:',symmetric_difference)
# Length of set:
Length_mySetA=len(my_SetA)
print('Length of set A')
# Clearing the set:
clear=my_SetA.clear()
print('Set after clearing all elements:',clear)
# Demonstrating set properties:
unordered_set={3,1,4,2}
print('Unordered set:',unordered_set)
unique_element_set={1,2,2,3,3,3}
print('Set with unique elements only: ',unique_element_set)


