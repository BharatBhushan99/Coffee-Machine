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

def processs_coins():
	print("Please insert coins.")
	quaters = int(input("how many quarters?: "))
	dimes = int(input("how many dimes?: "))
	nickels = int(input("how many nickels?: ")) 
	pennies = int(input("how many pennies?: ")) 
	total = quaters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
	return total

def check_transaction(coffee_type, coins_inserted):

	global profit

	if coins_inserted < MENU[coffee_type]["cost"]:
		print("Sorry that's not enough money. Money refunded.")
		return False
	elif coins_inserted > MENU[coffee_type]["cost"]:
		print(f"Here is ${round(coins_inserted - MENU[coffee_type]['cost'], 2)} in change.")
	profit += MENU[coffee_type]["cost"]
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
			coins_inserted = processs_coins()
			if check_transaction("espresso", coins_inserted):
				print("Making espresso")

	elif user_input == "latte":
		if check_resources("latte"):
			coins_inserted = processs_coins()
			if check_transaction("latte", coins_inserted):
				print("Making latte")

	elif user_input == "cappuccino":
		if check_resources("cappuccino"):
			coins_inserted = processs_coins()
			if check_transaction("latte", coins_inserted):
				print("Making cappuccino")
	else:
		print("Incorrect input.")



