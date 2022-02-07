from drinks import MENU, resources

# TODO: Prompt the user by giving choices of drinks.
# take input from the user: “What would you like? (espresso/latte/cappuccino):”
# There are hidden options too, report, this publishes the resources left at any given time
# and "off" which terminates the machine/program for execution.

action = input("What would you like? (espresso/latte/cappuccino): ").lower()

print(action)


# TODO: Print Report.

def publish_report():
    """Report publishes the resources left at any given time."""
    cash = 0.0
    # if action == "report":
    Money = cash
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    return water, milk, coffee, cash
    # return print(f"REPORT:==> \n Water: {water}ml \n Milk: {milk}ml \n Coffee: {coffee}g \n Money: ${cash}")
    #     if ingredient == "coffee":
    #         print(f"{ingredient} : {resources[ingredient]}g")
    #     else:
    #         print(f"{ingredient} : {resources[ingredient]}ml")
    # print(f"Money: ${cash}")
    # return water, milk, coffee, cash


# TODO: Check resources sufficient?
# When the user chooses a drink, the program should check if there are enough resources to make that drink.
# water.”
# The same should happen if another resource is depleted, e.g. milk or coffee.
def check_resources(choice):
    # for drink in MENU:
    #     print(f"Drink is : {drink}")
    water, milk, coffee = 0, 0, 0
    for ingredient in MENU[choice]:
        # print(f"{ingredient}: {MENU[drink][ingredient]}")
        cost = MENU[choice]["cost"]
        for _ in MENU[choice]["ingredients"]:
            if _ == "water":
                water = MENU[choice]["ingredients"]["water"]
            elif _ == "coffee":
                coffee = MENU[choice]["ingredients"]["coffee"]
            else:
                milk = MENU[choice]["ingredients"]["milk"]

    # print(f" water for the {choice}: {water}")
    # print(f" milk for the {choice}: {milk}")
    # print(f" coffee for the {choice}: {coffee}")
    # print(f" cost for the {choice}: {cost}")

    available_resources = publish_report()
    if available_resources[0] >= water and available_resources[1] >= milk and available_resources[2] >= coffee:
        print(f"Cost of drink: {cost}")
        return cost
    else:
        print("Sorry there is not enough resources")
        return


# TODO: Process Coins
# b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
def process_coins(price):
    """If there are sufficient resources to make the drink selected, then the program should prompt the user to
    insert coins. """
    print("Please insert coins.")
    quater = int(input("how many quarters?:"))
    dime = int(input("how many dimes?:"))
    nickel = int(input("how many nickels?:"))
    penny = int(input("how many pennies?:"))
    calculate_total = (quater * 0.25) + (0.1 * dime) + (0.05 * nickel) + (0.01 * penny)
    # print(type(inserted_money))
    # # cash_in_machine = publish_report()[3]
    # print(f"Cash Earned so far: ${publish_report()[3]}")

    change = 0.0
    # resources_available = check_resources(action)
    # cost_of_drink =check_resources(action)
    # print(type(resources_available[3]))
    if price <= calculate_total:
        change = calculate_total - price
        print(f"Here's is your change: $ {round(change, 2)}")
        return change
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False



cash = publish_report()[3]
if action == "report":
    # publish_report()
    print(f"REPORT:==> \n Water: {publish_report()[0]}ml \n Milk: {publish_report()[1]}ml \n Coffee: {publish_report()[2]}g \n Money: ${publish_report()[3]}")
    # print(publish_report())
else:
    cost_of_drink = check_resources(action)
    print(f"Cost of {action}: {cost_of_drink}")
    while process_coins(cost_of_drink):
        cash = cash + cost_of_drink
        print(f"Here is your {action} ☕️. Enjoy!")

    print(f"Total Earnings: {cash}")






# cash_in_machine = publish_report()[3]
# print(f"Again, Cash Earned so far: ${cash_in_machine}")
# TODO: Check transaction successful?
# Also calculate the value of instead coins and if more than the value of drink, offer change by subtracting the cost.
# The cost of drink must be added to the Money earned by machine after each serving.

# TODO: Make Coffee
# a) If the transaction is successful and there are enough resources to make the drink the
# user selected, then the ingredients to make the drink should be deducted from the
# coffee machine resources
# b) Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
# latte was their choice of drink.
