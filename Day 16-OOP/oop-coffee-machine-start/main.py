from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# TODO: 1. Print report of all coffee resources
# TODO: 2. Check resources sufficient to make drink order
# TODO: 3. Process coins
# TODO: 4. Check transaction successful
# TODO: 5. Make Coffee

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()

is_on = True

while is_on:
    options = Menu()
    choice = input(f"What would you like? ({options.get_items()}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = options.find_drink(choice)
        print(drink)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
                

