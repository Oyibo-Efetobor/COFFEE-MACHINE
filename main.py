from menu import the_menu, ingredients_available

# print(the_menu)
print(ingredients_available)

out_list =[700,500,200]
in_list =[]
is_value = True

#GETTING THE INGREDIENTS AND SUBTARCTING FROM THE ORIGINAL VALUE TO KNOW HOW MUCH IS LEFT

def ingredients_remaining(ingredient):
    global out_list
    counter = 0
    for i in ingredients_available:
        if i not in the_menu[ingredient]["ingredients"]:
            out_list[counter] = out_list[counter] - 0
        else:
            out_list[counter] = out_list[counter] - the_menu[ingredient]["ingredients"][i]
        counter += 1
    print(f"Water qty🌊: {out_list[0]},\n\n Milk qty🥛: {out_list[1]},\n\n Coffee qty☕: {out_list[2]}")
    
#VALIDATING WHETHER THE CUSTOMER IS ELIGIBLE TO BUY THE PRODUCT

def get_coins(ingredient):
    global is_value, user_coins
    user_coins = float(input("How much are you paying?💵\n $"))
    if user_coins < the_menu[ingredient]['cost']:
        print("money not enough can't buy 💔")
        is_value = False
    else:
        if user_coins > the_menu[ingredient]['cost']:
            print()
            print("Transaction Successful ✅")
            print()
            rnd_figure = round(user_coins-the_menu[ingredient]['cost'], 2)
            print(f"Here's your change ${rnd_figure} 🪙")
        else:
            print()
            print("Transaction Successful ✅")
            
def request():
    global is_value
    request_value = input("do you still wish to order again? y or n ?: ")
    if request_value == "n":
        is_value = False
    else:
        is_value = True
        
#ASKING THE ORDER

def get_order():
    bank_acct = 0
    while is_value:
        print()
        user_input = input("What would you like?\n espresso(e), latte(l), cappuccino(c)🍵 : ")
        
        if user_input == "e":
            print()
            print(f"Espresso costs ${the_menu['espresso']['cost']}")
            print()
            get_coins(ingredient="espresso")
            if is_value == True:
                bank_acct += the_menu['espresso']['cost']
                print()
                ingredients_remaining("espresso")
                print()
                print(f"Store balance is ${bank_acct}")
                print()
                request()
                print()
            else:
                break
        
        if user_input == "l":
            print()
            print(f"Latte costs ${the_menu['latte']['cost']}")
            print()
            get_coins(ingredient="latte")
            if is_value == True:
                bank_acct += the_menu['latte']['cost']
                print()
                ingredients_remaining("latte")
                print()
                print(f"Store balance is ${bank_acct}")
                print()
                request()

                print()
                
            else:
                break
            
        if user_input == "c":
            print()
            print(f"Cappuccino costs ${the_menu['cappuccino']['cost']}")
            print()
            get_coins(ingredient="cappuccino")
            
            if is_value == True:
                bank_acct += the_menu['cappuccino']['cost']
                print()
                ingredients_remaining("cappuccino")
                print()
                print(f"Store balance is ${bank_acct}")
                print()
                request()

                print()
                
            else:
                break 
        


print()
print()
get_order()

 

 



    
