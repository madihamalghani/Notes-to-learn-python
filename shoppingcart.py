# simple simulation of shopping cart where a user can add items,
# check total price and apply a discount if certain conditions are met
print('Hi welcome to the online store\n')
print('Can you tell your name plz\n')
customerName=input()
# String Variables:
storeName='Quick Shop'
welcomeMessage=f'Hello dear {customerName}, Welcome to {storeName}'
print(welcomeMessage)
# Initialize float and int variables:(not necessary in python to initialize it)
itemPrice=0.0
itemQuantity=0.0
totalItem=0.0
# List Variables:
cartItems=["Book", "Laptop" , "Headphones"]
# using boolean variable (initialize as false):
hasDiscount=False
# Dictionary:
item_prices={
"Book":12.99,
"Laptop":999.99,
"Headphones":49.99
}
# Dictionary:(string-type)
item_quantity_stri={
"Book":'0',
"Laptop":'0',
"Headphones":'0'
}
# Dictionary:(integer_type)
item_quantity_inte={
    "Book":0,
    "Laptop":0,
    "Headphones":0
}
# Asking from customer:
print('plz enter the number of books you want to buy')
item_quantity_stri["Book"]=input()
item_quantity_inte["Book"]=int(item_quantity_stri["Book"])

print('plz enter the number of laptops you want to buy')
item_quantity_stri["Laptop"]=input()
item_quantity_inte["Laptop"]=int(item_quantity_stri["Laptop"])

print('plz enter number of headphones you want to buy')
item_quantity_stri["Headphones"]=input()
item_quantity_inte["Headphones"]=int(item_quantity_stri["Headphones"])

# Discount Criteria
# total price over 100$ more than 2 items

# Arithmetic operations:
itemQuantity=item_quantity_inte["Book"]+item_quantity_inte["Laptop"]+item_quantity_inte["Book"]
totalPrice=item_quantity_inte["Book"]*item_prices["Book"] + item_quantity_inte["Laptop"]*item_prices["Laptop"]+item_quantity_inte["Headphones"]*item_prices["Headphones"]
# Checking discount
if totalPrice>100 and itemQuantity>2:
    hasDiscount=True
    discount=0.1 #10% discount
    totalPrice*=(1-discount) 
    # 1-0.1=0.9*total_price  (if total price=100) then:100*0.9=

# String operations:
    item_list=", ".join(cartItems)
    # The line item_list = ", ".join(cartItems) is used to join the elements of the cartItems list into a single string,
    #  where each item is separated by a comma and a space (, ).
    print(f'Items in your store: {item_list}\n')
    # print('Items in your cart\n\n',cartItems[0],"=",item_quantity_stri[str(cartItems)])


# Explicit type conversion:
    # (len())=> function to find length
    totalItem=len(cartItems)
    totalItemStr=str(itemQuantity)
    print(f'Total number of different items :{totalItemStr}\n')

    # Boolean and comparison operations:
    if hasDiscount:
        print('Congrats you have received discount on your purchase\n')
    else:
        print('No discount applied')

        # Final  Message:
print(f'Total amount you had to pay is {totalPrice}$ \n')
print(f'Thank You for shopping at {storeName}\n')



