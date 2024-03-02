#Rates how valuable a property in Salt Lake County could potentially be out of 10 based on its features and location. 

import os
os.system('cls')

price=input("Price? ")
squarefoot=input("Square feet? ")
acre=input("Acres? ")
upd=input("Has it been updated (yes/no)? ")
zipcode=input("Zipcode? ")
garage=input("Garage spaces? ")

#price = 250000
#squarefoot = 3000
#acre = .25
#upd = "yes"
#zipcode = 84094
#garage = 2

#updated = yes

#price
if int(price) / int(squarefoot) > 150:
    a = 0
if int(price) / int(squarefoot) < 115:
    a = 2
else:
    a = 1

#acre
b = float(acre)*8

#updated
if upd == "yes":
    c = 2
else:
    c = 0

nice_area = [84103, 84117, 84093, 84108, 84109, 84106, 84105, 84094, 84121, 84124]
okay_area = [84107, 84047, 84070, 84088, 84095, 84081]
not_so_great_area = [84116, 84104, 84128, 84120, 84119, 84123, 84118, 84044, 84006]

d = 0  # Initialize d with a default value

if zipcode in nice_area: 
    d = 2
elif zipcode in okay_area: 
    d = 1
elif zipcode in not_so_great_area: 
    d = 0

e = int(garage)

result = a + b + c + d + e
result_without_decimals = int(result)
print(str(result_without_decimals)+"/10") #create a string so it prints as one
