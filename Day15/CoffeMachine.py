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
    "money": 0,
}


def insert_coins(cost):
    print("Coins inserted")
    return True


def make_espresso():
    if resources["water"] >= MENU["espresso"]["ingredients"]["water"]:
        if insert_coins(MENU["espresso"]["cost"]):
            print("Making a espresso")
            resources["water"] -= MENU["espresso"]["ingredients"]["water"]
    else:
        print("Resources not sufficient")


def make_latte():
    if resources["water"] >= MENU["latte"]["ingredients"]["water"]:
        if insert_coins(MENU["latte"]["cost"]):
            print("Making a latte")
            resources["water"] -= MENU["latte"]["ingredients"]["water"]
    else:
        print("Resources not sufficient")


def make_cappuccino():
    if resources["water"] >= MENU["cappuccino"]["ingredients"]["water"]:
        if insert_coins(MENU["cappuccino"]["cost"]):
            print("Making a cappuccino")
            resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
    else:
        print("Resources not sufficient")

# ja peguei a logica da coisa, não vou fazer todos os ifs dos ingredientes
def start_machine():
    option = input("What would you like? (espresso/latte/cappuccino):")
    if option == "espresso":
        make_espresso()
        start_machine()
    elif option == "latte":
        make_latte()
        start_machine()
    elif option == "cappuccino":
        make_cappuccino()
        start_machine()
    elif option == "report":
        print("Water: " + str(resources["water"]))
        print("Milk: " + str(resources["milk"]))
        print("Coffee: " + str(resources["coffee"]))
        print("Money: " + str(resources["money"]))
        start_machine()
    elif option == "off":
        print("Turning off...")
    else:
        print("invalid answer")
        start_machine()


start_machine()