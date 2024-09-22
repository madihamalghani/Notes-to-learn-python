# Dictionaries:Unordered key value pair:
# Arrays:similar to list but with type-constrains

# ================Dictionary================#
my_dict={'a':1,'b':2,'c':3}
print('Original Dictionary:',my_dict)
# Accessing Elements:
print('Accessing element of a: ',my_dict['a'] )
print('Value for key b: ',my_dict['b'])
# Adding and updating elements:
my_dict['d']=4
my_dict['e']=4
print(f' e is added with key: {my_dict['e']} and  d is added with key {my_dict['d']} ')
# Updating the dictionary:
my_dict['d']=10
print(f'value of d is updating from 4 to {my_dict['d']}')
# Removing elements:
del my_dict['d']
print(f'd is removed from the dictionary remaing dectionary is {my_dict}')
# Checking membership:
print("is key 'a' in the dictionary?",'a' in my_dict)
# Dictionary key, values and items:
print('Keys',my_dict.keys())
print('Values',my_dict.values())
print('items',my_dict.items())
# Iterating over a dictionary:
print('************** Iterating over a dictionary *************')
for key,value in my_dict.items():
    print(f'Key={key} and value={value}')
# Length of dictionary:
print('length of dictionary is: ',len(my_dict))
# Clearing the dictionary:
my_dict.clear()
print('Dictionary after clearing all elements: ',my_dict)
# Using dictionary comprehension:
squares={x:x*x for x in range(1,6)}
print('Dictionary comprehension (squares): ',squares)
# get even:
add={x:x+1 for x in range(1,6)}
print('Addition is: ',add)
# Nested Dictionaries:
nested_dictionaries={
    'class1':{'student1':'Alice','student2':'Sonia'},
    'class2':{'student1':'John','student2':'Hater'}
}
print('Nested dictionary: ',nested_dictionaries)
print('Accessing nested dictionary with class1 and student1: ',nested_dictionaries['class1']['student1'])