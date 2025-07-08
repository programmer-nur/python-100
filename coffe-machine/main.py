MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "coffee": 24,
            "milk": 150,
        },  
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100,
        },
        "cost": 3.0,
    },
}

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}



def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    is_enough = True
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print("​Sorry there is not enough water.​")
            is_enough = False
    return is_enough


def is_transaction_successful(mony_received, drink_cost):
    """Return True when the payment is accepted, or False mony is insufficient."""
    if mony_received <= drink_cost:
        change = round(mony_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough mony. Mony refunded.")
        return False

def process_coin():
    """Returns the total calculated form coin inserted """
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def make_coffee(drink_name, order_ingredient):
    """Deduct the required ingredients from the recourses."""
    for item in order_ingredient:
        resources[item] -= order_ingredient[item]
    print(f"Here is you {drink_name}. Enjoy!")
    


is_on = True

while is_on:
    choice = input("​What would you like? (espresso/latte/cappuccino):​")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif choice not in MENU:
         print("Sorry this flavour is not available")
        
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
           payment = process_coin()
           if is_transaction_successful(payment, drink["cost"]):
               make_coffee(choice,drink["ingredients"])
