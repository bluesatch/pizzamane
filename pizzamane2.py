import time

def notitem(topping): #when item is not in menu
        print(f"Sorry, we don't have {topping} on the menu. However, we will add it for the future. See?")
        menu.append(topping.lower())
        time.sleep(2)
        print(menu)
        print("Please make another selection.")
            

def choice1(): #For 1-topping pizzas
    choice = []
    while len(choice) < 1:
        print("What topping would you like to add?")
        topping = input()
        if topping.lower() in menu:
            choice.append(topping.lower())
            print(f"Ok. A {topping} pizza is on your way. That will be $8.55")
        elif topping.lower() not in menu:
            notitem(topping)
        else:
            print("Error")

def choice2(): #For 2-topping pizzas
    choice = []
    while len(choice) < 2:
        print("Make your first selection.")
        topping = input()
        if topping.lower() in menu:
            choice.append(topping.lower())
            print(f"Ok. {topping} is your first choice. What is your second?")
            topping = input()
            if topping.lower() in menu:
                choice.append(topping.lower())
                print(f"Ok. A {choice[0]} and {choice[1]} pizza is coming your way. That will be $9.62")
            elif topping.lower() not in menu:
                notitem(topping)
            else:
                print("Error")
        elif topping.lower() not in menu:
            notitem(topping)
        else:
            print("Error")

def choice3(): # For 3-topping pizzas
    choice = []
    while len(choice) < 3:
        print("Got it. Three toppings. What is your first topping?")
        topping = input()
        if topping.lower() in menu:
            choice.append(topping.lower())
            print(f"Ok, {topping} is your first choice. And for your second?")
            topping = input()
            if topping.lower() in menu:
                choice.append(topping.lower())
                print(f"Alright {topping} is your second choice. And lastly, your third?")
                topping = input()
                if topping.lower() in menu:
                    choice.append(topping.lower())
                    print(f"So we have a {choice[0]}, {choice[1]}, and {choice[2]} pizza for you. That will be $11.76")
                elif topping.lower() not in menu:
                    notitem(topping)
                else:
                    print("Error")
            elif topping.lower() not in menu:
                notitem(topping)
            else:
                print("Error")
        elif topping.lower() not in menu:
            notitem(topping)
        else:
            print("Error")

menu = ['pepperoni', 'sausage', 'beef', 'chicken', 'ham', 'tomato', 'spinach', 'peppers', 'onion', 'pineapple']
print("Welcome to Satch's Pizzeria where nobody tops our toppings!\nWe are offering large pizzas for up to three toppings.\nHave a look at our menu.")
time.sleep(2)
print(menu)
print("Would you like 1, 2, or 3 toppings?") 
selection = input()
while int(selection) <= 0 or int(selection) >= 4:
    print("Please type 1, 2, or 3")
    selection = input() 

if int(selection) == 1:
    choice1()
elif int(selection) == 2:
    choice2()
elif int(selection) == 3:
    choice3()

    

