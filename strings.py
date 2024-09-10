#concatinate strings:
firstName=input('input your first name ')
lastName=input('input your last name ')
fullName=firstName + ' ' + lastName
print('Your name is ' + fullName)
# string index 
nicName=firstName[0] + lastName[0]
print('Nic Name is ' + nicName)
# ===================some functions of string==============
uppercase=firstName.upper()
print('Upper Case: '+ uppercase)
lowercase=firstName.lower()
print('Lower Case: ' + lowercase)
capitalized=firstName.capitalize()
print('Capitalize Case: ' + capitalized)
# We can repeat a string 
identity='princess'
print('You know what? I am '+ (identity + ' ' )*3)
# And you can assign the same value to multiple variables in one line:
a,b,c='banana','mango','apple'
print(a)
print(b)
print(c)
# Unpack a list:
fruits = ["apple", "banana", "cherry"]
d,e,f = fruits
print('here is the unpacked list')
print(d)
print(e)
print(f)
# use of strip remove spaces from begning and end
institute='   university of education lahore   '
withoutSpace='universityofeducationlahore'

print('institute is:' + institute)
nowInstitute=institute.strip()
print('institue after using strip method:' + nowInstitute)
# ===========isalpha()====================
# isalpha() applies on string => boolean type method 
# if we apply it on numeric variable it will return false
# on boolean variable it will return true
# for true there must not be any space left
print(institute.isalpha())
print(withoutSpace.isalpha())
print('Institute after using strip method:', nowInstitute)
print('Is without space only alphabetic:', withoutSpace.isalpha())
# We can check types of variables:
print('type of without space: ')
print(type(withoutSpace))
# checking type of float:
w1=43567.998477
print('type of w',type(w1))













