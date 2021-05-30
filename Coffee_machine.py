MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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


def check_resources():
    a = resources['water'] - MENU[choice]['ingredients']['water']
    b = resources['milk'] - MENU[choice]['ingredients']['milk']
    c = resources['coffee'] - MENU[choice]['ingredients']['coffee']
    if a < 0:
        print("Sorry there is not enough water.")
        return False
    elif b < 0:
        print("Sorry there is not enough milk.")
        return False
    elif b < 0:
        print("Sorry there is not enough coffee.")
        return False
    else:
        return True


def check_money():
    if change < 0:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        print(f"Here is ${change} in change.")
        return True


money = 0
coffee_machine_on = True
while coffee_machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == 'off':
        coffee_machine_on = False
    elif choice == 'report':
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g"
              f"\nMoney: ${money}")
    else:
        if check_resources():
            print("Please insert coins.")
            quarters = int(input("how many quarters?: "))
            dimes = int(input("how many quarters?: "))
            nickles = int(input("how many quarters?: "))
            pennies = int(input("how many quarters?: "))
            total_inserted = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
            change = (total_inserted - MENU[choice]['cost']).__round__(2)
            if check_money():
                money += MENU[choice]['cost']
                resources['water'] -= MENU[choice]['ingredients']['water']
                resources['milk'] -= MENU[choice]['ingredients']['milk']
                resources['coffee'] -= MENU[choice]['ingredients']['coffee']
                print(f"Here is your {choice}  ☕ Enjoy!")
