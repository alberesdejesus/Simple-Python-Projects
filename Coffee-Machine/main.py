from data import MENU, resources

money = 0
is_on = False


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def modify_resources(coffee):
    """Deduct the required ingredients from the resources."""
    for item in MENU[choice]['ingredients']:
        resources[item] -= MENU[coffee]['ingredients'][item]


def check_money(coffee, money_machine):
    """Verify if payment is accepted, or if money is insufficient."""
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total_money = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    if total_money >= MENU[coffee]['cost']:
        print(f"Here is ${total_money - MENU[coffee]['cost']:.2f} in change")
        return money_machine + MENU[coffee]['cost']
    else:
        print("Sorry that's not enough money. Money refunded")


while not is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == 'report':
        print(
            f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${money:.2f}")
    elif choice == 'espresso' or choice == 'latte' or choice == 'cappuccino':
        if is_resource_sufficient(MENU[choice]['ingredients']):
            money = check_money(choice, money)
            modify_resources(choice)
            print(f"Here is your {choice}. Enjoy!")
    elif choice == 'off':
        print("Coffee machine is shutdown")
        is_on = True
    else:
        print("Sorry, i don't have this coffee")
