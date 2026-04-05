'''This is the list of poducts, all products have price and quantity.
product() stores all the items available in dictionary'''
# Product list
def product ():
    return {
    "Rice": {"price": 100, "quantity": 50},
    "flour": {"price": 120, "quantity": 60},
    "sugar": {"price": 80, "quantity": 20},
    "Tissue": {"price": 60, "quantity": 100},
    "Toothbrush": {"price": 90, "quantity": 64},
    "Soap(bar)": {"price": 70, "quantity": 30},
    "Fabric Softener": {"price": 700, "quantity":8},
    "Bleach": {"price": 700, "quantity": 14},
    "Detergent": {"price": 300, "quantity": 10},
    "Deoderant": {"price": 400, "quantity": 12},
    "Cooking oil": {"price": 350, "quantity": 19},
    "Syrup": {"price": 370, "quantity": 15},
    "Oats": {"price": 300, "quantity": 6},
    "Mackerel": {"price": 250, "quantity": 23},
    "Cornbeef": {"price": 720, "quantity": 17},
    "Lasco": {"price": 150, "quantity": 10},
    "Water(small)": {"price": 100, "quantity": 47},
    "Water(big)": {"price": 200, "quantity": 25},
    "Cola": {"price": 180, "quantity": 12},
    "Pepsi": {"price": 200, "quantity": 23},
    "Bag Juice": {"price": 60, "quantity": 70},
    "Cheesebread": {"price": 180, "quantity":6},
    "Bun": {"price": 130, "quantity": 8},
    "Blender": {"price": 5900, "quantity": 7},
    "Utensils": {"price": 1000, "quantity": 10},
    }
    return item_stock

'''display_product() allows viewers to see all available products. 
    It shows name of product,price and quantity. '''
# display product list

product_cart ={}
def display_product():
    prod=product()
    print("Products In-stock")
    for name,details in prod.items():
        print(f"{name.title()} -Price: ${details['price']} | Quantity: {details['quantity']}")

'''shooping cart() creates a cart that allows the addition of different products 
and the amount needed as long their is enough quantity and if the product exists.'''
# add product to cart

def shopping_cart ():
    prod_check = True
    prod=product()
    display_product()
    name_entered = input("Enter product name: ")
    for product_name in prod:
        if product_name.lower() == name_entered.lower():
            name = product_name
            prod_check =True
            break
    if prod_check == False:
        print("product not found")
        return
    qty = int(input("Enter quantity: "))

    available_quantity = prod[name]["quantity"]

    if qty > available_quantity:
        print("Not enough quantity")
    else:
        print(f"Price: {prod[name] ['price']}")
# get the individual price and multiply by quantity which shows total price
        unit_price = prod[name] ['price']
        total_price = unit_price * qty
        print(f"Total Price: ${total_price}")
# adds the product to cart
    if name in product_cart:
        product_cart[name]["quantity"] += qty
    else:
        product_cart[name] = {"quantity": qty}

    print(f"{name} added to cart")
    print(product_cart)
    print(qty)

# This applies a 5% discount for prices over 5000
#discount system
def apply_discount(subtotal):
    if subtotal > 5000:
        discount = subtotal * 0.05
        subtotal -= discount
        print(f"Discount Sale Applied -${discount}")
    else:
        print("No Discount Sale Applied ")
    return subtotal
#shopping_cart()

'''Allow the removal of products that are inside the cart'''
# to remove item from cart

def remove_item():
    prod = product()
    prod_check = False


    name_entered = input("Enter product to be removed: ")

    for product_name in prod:
        if product_name.lower() == name_entered.lower():
            name = product_name
            prod_check = True
            break


    if not prod_check:
        print("Product not found")
        return
    if name not in product_cart:
        print("item not in cart")
        return
    try:
            qty = int(input("Enter quantity to be removed: "))
    except ValueError:
            print("invalid quantity")


    if qty >= product_cart[name]["quantity"]:
            del product_cart[name]
            print(f"{name} removed")
    else:
            product_cart[name]["quantity"] -= qty
            print(f"{qty} {name}(s) removed")

#remove_item()

'''Shows all products that were previously added to the cart'''
# to view what is in the cart

def view_cart():
    if not shopping_cart:
        print("shopping cart empty")
        return

    print("\n---Shopping Cart---")
    subtotal= 0
    products = product()

    for name,details in product_cart.items():
        quantity = details["quantity"]
        unit_price = products[name]["price"]
        total_price = unit_price * quantity
        subtotal += total_price
        print(f"{name} | Quantity: {quantity} | Unit Price: ${unit_price} | Total: ${total_price}")

    print(f"Subtotal: ${subtotal}")
    print("---------------------\n")
    return subtotal

#view_cart()

'''checkout() is when all product has been choosen that are in  the cart. 
It will display the subtotal of each product and the overall amount recieves payment and calculates change.
This adds a discount if needed while also adding the sales tax which is 10% of the total
The last process of this section of the code collects the payment and return the correct change'''
# Checkout Process
def checkout():
    if not product_cart:
        print("shopping cart empty")
        return

    print("\n---Shopping Cart---")
    subtotal = view_cart()
    products = product()

#Applying discount if needed
    subtotal = apply_discount(subtotal)
    print(f"Subtotal: ${subtotal}")

#Applying sales tax
    tax= subtotal * 0.10
    total_due = subtotal + tax
    print(f"Tax: ${tax}")

#Collect Payment
    while True:
        try:
            amount_collected = int(input("Enter amount collected: "))
            if amount_collected < total_due:
                print("invalid amount")
            else:
                break
        except ValueError:
            print("invalid amount")

    change = amount_collected - total_due
    print(f"Change to return: ${change}")
    print("Payment successful Thanks you come again.\n")

#This is to clear the cart
#checkout()

'''Prints a receipt that shows all items purchased along with tax and discount with the total price 
money collected and change'''

# receipt
def receipt():
    if not product_cart:
        print("Shopping cart is empty")
        return

    products = product()
    subtotal = 0

    print("\n========================")
    print("        WELCOME TO MS CHIN'S MINI MART       ")

#List of itemized items
    for name, details in product_cart.items():
        quantity= details["quantity"]
        unit_price = products[name]["price"]
        total_price= unit_price * quantity
        subtotal += total_price

        print(f"{name:20} {quantity:>5} ${unit_price:>5} ${total_price:>9}")

    #End of loop

#Apply Discount
    suntotal = apply_discount(subtotal)

    # Tax and the total
    tax = subtotal * 0.10
    total_due= subtotal + tax

    print("_______________________")
    print(f"{'Subtotal':>34}: ${subtotal:7}")
    print(f"{'Tax':>34}: ${tax:7}")
    print(f"{'Amount Due':>34}: ${total_due:7}")

    #Payment Collection
    while True:
        try:
            amount_collected = int(input("Enter amount collected: "))
            if amount_collected < total_due:
                print("invalid amount")
            else:
                break
        except ValueError:
            print("invalid amount")

    change = amount_collected - total_due
    print(f"{'Amount Paid':>34}: ${amount_collected:7}")
    print(f"{'Change':>34}: ${change:7}")
    print("Thank You For Shopping, Come Again")

#clear the cart
#receipt()
#product_cart.clear()

'''This is the main menu it is where you select the option that you wish to proceed with  '''

def main():
    while True:
        print("\n--- Main Menu---")
        print("1. Shop")
        print("2. View Cart")
        print("3. Checkout")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            shopping_cart()
        elif choice == "2":
            view_cart()
        elif choice == "3":
            receipt()
            checkout()
        elif choice == "4":
            print("Exit Session. Thank you")
            break
        else:
            print("Invalid choice. Choose between 1-4")

main()