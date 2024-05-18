products = [{"laptop":"lenovo" , "price":"1000$" , "discount":"20%"},
            {"laptop":"acer" , "price":"900$" , "discount":"25%"},
            {"laptop":"mac Book Air " , "price":"4000$" , "discount":"20%"},
]
print(type(products))
name = input("Enter the nsme of the laptop you want to buy : ")
name=name.lower()
print(name)
for product in products:
    print(type(product))
    if product["laptop"]==name:
        print("Matched successfulyy")
        break
    else:
        print("No such item found")    