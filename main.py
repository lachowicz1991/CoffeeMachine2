from data import MENU


def print_report(water, milk, coffee, money):
    print(f"Water:{water}\nMilk:{milk}\nCoffee{coffee}\nMoney:{money}")


def process_coins(coffe_type):
    print("Please insert coins (dollars = $1, quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01")
    dollars = float(input('How many dollars?')) * 1
    print(dollars)
    quarters = float(input('How many quarters?')) * 0.25
    print(quarters)
    dimes = float(input('How many dimes?')) * 0.10
    print(dimes)
    nickles = float(input('How many nickles?')) * 0.05
    print(nickles)
    pennies = float(input('How many pennies?')) * 0.01
    print(pennies)
    money_sum = dollars + quarters + dimes + nickles + pennies
    if money_sum > MENU[coffe_type]["cost"]:
        change = money_sum - MENU[coffe_type]["cost"]
        print(f"Here is {change}")
        print(f"Here is your espresso ☕.Enjoy!")
        return change
    elif money_sum == MENU[coffe_type]["cost"]:
        change = money_sum - MENU[coffe_type]["cost"]
        return change


def coffee_machine():
    coffee_type = input("What would you like?")
    process_coins(coffee_type)

coffee_machine()