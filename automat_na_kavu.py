

from source_data import MENU
from source_data import resources




def calculate_rests(resource, water, milk, coffee):
    if resource["water"] < water or resource["milk"] < milk or resource["coffee"] < coffee:
        print("Na váš nápoj nemáme dostatek surovin")
        return False


    else:

        resource["water"] -= water
        resource["milk"] -= milk
        resource["coffee"] -= coffee
        print(resource["water"])
        print(resource["milk"])
        print(resource["coffee"])
        print("Na váš nápoj máme dostatek ingrediencí")
        return True

def print_price(drink):
    price = MENU[drink]["cost"]
    return price


 # hlavní kod
def coffee():
    continues = True
    coins = [1, 2, 5, 10, 20, 50]
    total_coins = []

    while continues:
        choice = input("Co byste si dal?(espresso/latte/cappuccino")
        print(resources)

        if choice == "espresso":
            continues = calculate_rests(resources, MENU[choice]["ingredients"]["water"], MENU[choice]["ingredients"]["milk"], MENU[choice]["ingredients"]["coffee"])
        elif choice == "latte":
            continues = calculate_rests(resources, MENU[choice]["ingredients"]["water"], MENU[choice]["ingredients"]["milk"], MENU[choice]["ingredients"]["coffee"])
        elif choice == "cappuccino":
            continues = calculate_rests(resources, MENU[choice]["ingredients"]["water"], MENU[choice]["ingredients"]["milk"], MENU[choice]["ingredients"]["coffee"])
        elif choice == "report":
            print(resources)





        if continues == False or choice == "report":
            break


        else:
            print("prosím, vložte mince 1,2,5,10,20,50")
            for one_coin in coins:
                number_of_coins = int(input(f"Kolik {one_coin} Kč chcete vložit?"))
                value_coins = number_of_coins * one_coin
                total_coins.append(value_coins)

            print(f"celkem jste vložili {sum(total_coins)}")

            print(f" cena nápoje je: {print_price(choice)}")

            if sum(total_coins) == print_price(choice):
                print("Děkuji za přesnou částku platby za nápoj")
            elif sum(total_coins) < print_price(choice):
                print("Vhozená částka na nápoj nestačí")
            elif sum(total_coins) > print_price(choice):
                print(f"Nápoj se připravuje, vrácená částka je: {sum(total_coins) - print_price(choice)} Kč.")




coffee()