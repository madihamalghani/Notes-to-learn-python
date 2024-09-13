

# While loop:
i=1
print('Printing while loop. It will terminate after the condition is fulfilled')
while i<5:
    print(i)
    i+=1
# For loop:
a=range(3,9,2) 
# This creates a range object a that starts from 3, ends before 9(9 not included),
#  and increments by 2. The range() function takes three arguments.
i=1
# starts with 3 end before 9 increment by 2 so 3,3+2,5+2,5+2+2>=9=>terminate
for varl in a:
    print(f'Value of dummy variable in iteration {i} is = {varl}')
    i+=1
print('Now we are outside for loop')
# for item in sequence:
for num in [1, 2, 3]:
    print(f'Number is {num}')

# Iterating Over Different Data Types
# Arrays:
fruits = ['apple', 'banana', 'cherry']
    # fruit represent index
for fruit in fruits:
    print(f'Fruits include: {fruit}')
# Strings:
for letter in 'Python':
    print(f'word in letter are {letter}')
# Tuple:
numbers = (1, 2, 3)
for num in numbers:
    print(f'num include {num}')
#Dictionary: You can loop over the keys, values, or both:
student_grades = {'Alice': 90, 'Bob': 85, 'Charlie': 92}
# Loop over keys:
for name in student_grades:
    print(name)

# Loop over values:
for grade in student_grades.values():
    print(grade)

# Loop over both keys and values:
for name, grade in student_grades.items():
    print(f'{name}: {grade}')
# Range in loop:(generates sequence of numbers)
for i in range(5):
    print(i)



 

