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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def print_report():
	print(f"Water: {resources['water']}ml\nMilk:  {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${profit:.2f}")
	     
def check_resources(coffee_type):
	items = ["water", "milk", "coffee"]

	for item in items:
		if resources[item] < MENU[coffee_type]["ingredients"][item]:
			print(f"Sorry there is not enough {item}.")
			return False
	return True

turn_off = False


while not turn_off:
	user_input = input(" What would you like? (espresso/latte/cappuccino): ")

	if user_input == "off":
		turn_off = True

	elif user_input == "report":
		print_report()
		
	elif user_input == "espresso":

		if check_resources("espresso"):
			print("Making espresso")

	elif user_input == "latte":
		if check_resources("latte"):
			print("Making latte")

	elif user_input == "cappuccino":
		if check_resources("cappuccino"):
			print("Making cappuccino")
	else:
		print("Incorrect input.")



