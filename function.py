# Functions in python:

def greet(name): #where name is a parameter
    print(f'Hello {name}')
# Now call the function as many times as you want:
greet('Madiha')
# You can also input name whom you want to greet:
print('Enter name of the person you want to greet')
name1=input()
greet(name1)

# How parameters are passed:
# types of parameters : 1.positional(maintain values in order) 2.keyword 3.default
def pets_desc(pet_name,animal_type="dog"):
    print(f'I have a {animal_type} whose name is {pet_name}')

pets_desc('Buddy') #default parameter
pets_desc('Female German Sepherd','Stella') #Be careful while passing posional arguments
pets_desc('Stella','Female German Sepherd') # correct arrangement
pets_desc(animal_type='hamster',pet_name='Harry')

# Return value of a function:
def operations(x,y):
    product=x*y
    sum=x+y
    strOpertons='The Sum and product of given number is: '
    return strOpertons,product,sum

operation_result=operations(3,4)
print(operation_result)
# with 3,9
strglobe,productglobe,sumglobe=operations(3,9)
print(strglobe,productglobe,sumglobe)

