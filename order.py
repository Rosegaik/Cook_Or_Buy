def buy():
    import sys
    menu = {
   # Indian Cuisine
        1: {"name": "Paneer Butter Masala", "price": 150},
        2: {"name": "Pulikolambu", "price": 120},
        3: {"name": "Naan", "price": 30},
        4: {"name": "Poori", "price": 25},
        5: {"name": "Jeera Rice", "price": 80},
        6: {"name": "Sambar Rice", "price": 70},
        7: {"name": "Aloo Tikki", "price": 40},
        8: {"name": "Medu Vada", "price": 30},

        # Thai Cuisine
        9: {"name": "Thai Green Curry", "price": 160},
        10: {"name": "Thai Red Curry", "price": 160},
        11: {"name": "Pad Thai", "price": 140},
        12: {"name": "Glass Noodle Salad", "price": 130},
        13: {"name": "Sticky Rice with Mango", "price": 100},
        14: {"name": "Thai Coconut Pudding", "price": 90},

        # Chinese Cuisine
        15: {"name": "Schezwan Noodles", "price": 130},
        16: {"name": "Schezwan Fried Rice", "price": 130},
        17: {"name": "Gobi Manchurian", "price": 110},
        18: {"name": "Paneer Chilli", "price": 120},
        19: {"name": "Manchow Soup", "price": 60},
        20: {"name": "Sweet Corn Soup", "price": 60},

         # Japanese Cuisine
        21: {"name": "Teriyaki Chicken", "price": 170},
        22: {"name": "Katsu Curry", "price": 160},
        23: {"name": "Ramen", "price": 150},
        24: {"name": "Udon", "price": 150},
        25: {"name": "Mochi", "price": 80},
        26: {"name": "Dorayaki", "price": 90},

        # Italian Cuisine
        27: {"name": "Spaghetti Aglio e Olio", "price": 140},
        28: {"name": "Macaroni with Cheese", "price": 130},
        29: {"name": "Margherita Pizza", "price": 150},
        30: {"name": "Cheese Brust Pizza", "price": 160},
        31: {"name": "Panna Cotta", "price": 90},
        32: {"name": "Tiramisu", "price": 100},

        #mexcian cuisine
        33: {"name": " Mexican Rice", "price": 120},
        34: {"name": "Nachos with Cheese", "price": 130},
        35: {"name": "Taco Bowl", "price": 150},
        36: {"name": "Enchiladas", "price": 160},
        37: {"name": "Churros", "price": 90},
        38: {"name": "Tres Leches Cake", "price": 100}

    }

    cart = []
    total = 0

    while True:
        print("\nMenu:")
        for num, item in menu.items():
            print(f"{num}. {item['name']} - ₹{item['price']}")

        choice = int(input("Enter food number: "))
        if choice not in menu:
            print("Invalid choice. Try again.")
            continue

        qty = int(input(f"How many plates of {menu[choice]['name']}? "))
        amount = qty * menu[choice]["price"]
        cart.append((menu[choice]["name"], qty, amount))
        total += amount

        more = input("Do you want to add more? (yes/no): ").lower()
        if more != "yes":
            break
    print("\n\n🧾 Your Bill:")
    for item in cart:
        print(f"{item[0]} x {item[1]} = ₹{item[2]}")
    print(f"Total Amount: ₹{total}")
    print('\nThank you for your order!')

    import payment
    proceed = input("\nDo you want to proceed to payment? (yes/no): ").lower()
    if proceed == "yes":
        payment.process_payment(total)
    sys.exit()
    

#buy()   
    
