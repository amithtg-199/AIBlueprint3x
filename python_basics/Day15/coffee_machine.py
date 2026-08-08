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

remaining_resources = resources.copy()

remaining_resources["cost"] = 0

def coffee_prepare(drink_name):
    drink = MENU[drink_name]
    ingredients = drink["ingredients"]
    water = ingredients.get("water", 0)
    milk = ingredients.get("milk", 0)
    coffee = ingredients.get("coffee", 0)
    cost = drink["cost"]
    return water, milk, coffee, cost

def report():
    global remaining_resources
    print(f"Water: {remaining_resources['water']}ml")
    print(f"Milk: {remaining_resources['milk']}ml")
    print(f"Coffee: {remaining_resources['coffee']}")
    print(f"Money: ${remaining_resources['cost']}")

def get_valid_coin_count(prompt_text):
    while True:
        raw_input = input(prompt_text).strip()
        try:
            count = int(raw_input)
            if count >= 0:
                return count
            else:
                print("Please enter a positive number (or 0).")
        except ValueError:
            print("That is not a valid number. Please try again.")


def check_resources(choice):
    if choice in ["espresso", "latte", "cappuccino"]:
        water_required, milk_required, coffee_required, _ = coffee_prepare(choice)

        if water_required > remaining_resources["water"]:
            return "Sorry there is not enough water."
        elif milk_required > remaining_resources["milk"]:
            return "Sorry there is not enough milk."
        elif coffee_required > remaining_resources["coffee"]:
            return "Sorry there is not enough coffee."
        
        return True

def coffee_machine():
    is_start = True
    while is_start is True:
        choice = input("What would you like? (espresso/latte/cappuccino): ").strip().lower()
        while choice not in ["espresso", "latte", "cappuccino", "report", "off"]:
            choice = input("Sorry! Kindly input proper value (espresso/latte/cappuccino): ").strip().lower()

        
        if choice == "off":
            is_start = False
            print("Turning off the Coffe Machine GoodBye!")
            continue
        elif choice == "report":
            report()
            continue

        status = check_resources(choice)
        if status is not True:
            print(status)
            continue

        print("Please insert coins.")
        quarters = get_valid_coin_count("How many quarters?: ")
        dimes = get_valid_coin_count("How many dimes?: ")
        nickles = get_valid_coin_count("How many nickles?: ")
        pennies = get_valid_coin_count("How many pennies?: ")

        total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
        choice_of_coffee_cost = coffee_prepare(choice)[3]
        if total >= choice_of_coffee_cost:
            change = round((total - choice_of_coffee_cost), 2)
            print(f"Here is ${change} in change.")
            print(f"Here is your {choice} ☕️. Enjoy!")

            remaining_resources["cost"] += choice_of_coffee_cost

            water_used, milk_used, coffee_used, _ = coffee_prepare(choice)
            for resource in remaining_resources:
                if resource == "water":
                    remaining_resources["water"] -= water_used
                elif resource == "milk":
                    remaining_resources["milk"] -= milk_used
                elif resource == "coffee":
                    remaining_resources["coffee"] -= coffee_used
        else:
            print("Sorry Amount not enough, amount is refunded")

if __name__ == "__main__":
    coffee_machine()
