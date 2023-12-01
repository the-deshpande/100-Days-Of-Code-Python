from resources import logo
from resources import MENU

storage = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money":0,
}

print(logo)

while(True):
    n = input("What would you like? (espresso/latte/cappuccino) : ").lower()
    if(n == 'off'):
        print("Thank-you for using our coffee machine")
        print(logo)
        break
    if(n == 'report'):
        for key,value in storage.items():
            print(f'{key} : {value}')
        continue
    if(n not in ['espresso','latte','cappaccino']):
        print("I'm sorry we don't offer that drink")
        continue
    else:
        for i in MENU[n]['ingredients']:
            if(storage[i]<MENU[n]['ingredients'][i]):
                print(f"Sorry there is not enough {i}")
                break
        else:
            print(f"The cost is {MENU[n]['cost']}")
            total = 0.25*int(input("Quarters : "))
            total+= 0.10*int(input("Dimes : "))
            total+= 0.05*int(input("Nickles : "))
            total+= 0.01*int(input("Pennies : "))
            print(f'Total : {total}')
            if(total < MENU[n]['cost']):
                print("Sorry that's not enough money. Money refunded")
                continue
            elif(total > MENU[n]['cost']):
                print(f"Here is the ${round(total-MENU[n]['cost'],2)} in change")
            for i in MENU[n]['ingredients']:
                storage[i]-=MENU[n]['ingredients'][i]
            storage['money']+=MENU[n]['cost']
            print(f'Here is your {n} enjoy!')