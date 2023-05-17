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
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}



def paying():
    print("Please insert coins")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    quarters_total = quarters * 0.25
    dimes_total = dimes * 0.10
    nickles_total = nickles * 0.05
    pennies_total = pennies * 0.01
    total = quarters_total + dimes_total + nickles_total + pennies_total
    return total


def checking_resources(coffee:str):
    for ingredient, quantity in MENU[coffee]["ingredients"].items():
        if resources[ingredient] >= quantity:
            resources[ingredient] -= quantity    
        elif resources[ingredient] < quantity:
            for ingredient, quantity in MENU[coffee]["ingredients"].items():
                if resources[ingredient] < quantity:
                    print(f"Sorry there is not enough {ingredient}")
            return False
    return True
        

def cofee_machine():
    
        money = 0
        cofee_machine_running = True
        while cofee_machine_running == True:
            order = input("What would you like? (espresso/latte/cappuccino): ").lower()


            if order == "off":
                quit()


            elif order == "report":
                for name, ammount in resources.items():
                    print(f"{name}:{ammount}")
                print(f"{money}$")


            elif order == "espresso" or order == "latte" or order == "cappuccino":
                if checking_resources(order) == True:
                    payment = paying()
                    if payment >= MENU[order]["cost"]:
                        money += MENU[order]["cost"]
                        change = payment - MENU[order]["cost"]
                        rounded_change = "{:.2f}".format(change)
                        print(f"Here is ${rounded_change} in change")
                        print(f"Here is your {order} ☕️. Enjoy!")
                    elif payment < MENU[order]["cost"]:
                        print("Sorry that's not enough money - money refunded")
                    elif payment == 0:
                        print("You didn't provide any coins - please try again")
            else:
                print("You provided bad input, try again")
        
cofee_machine()




