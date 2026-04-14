#This is my game called "Tomato stocks" where you make money by growing tomatoes in an infinite loop

#area to import functions
import os
import time
import tkinter
import json
import threading
from tkinter import messagebox



#area to define variables
#... acts as a substitute for the value 'null' as it is only used to define the variables listed below
new_life_started = "..."
money = "..."
tomato_price = "..."
current_day = "..."
tomatoes_currently_growing = "..." 
tomato_seeds = "..."
fertilizer_quantity = "..."
has_grow_light = "..."
tomato_stock = "..."
fertilizer_stock = "..."
grow_light_stock = "..."
user_in_shop = "..."
new_day_started = "..."
has_housing = "..."
tomatoes_currently_growing_with_fertilizer = "..."
amount_of_tomatoes_growing = "..."
amount_of_tomatoes_grown = "..."
max_buy = "..."

#function to clear the screen 
#this function must be initialized before all other functions or it will not properly function.
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

#script to start new life
print ("Welcome to Tomato stocks. The game where you grow tomatoes in an infinite loop to make money.")
while True:
    user_input = input("Would you like to start a new life? (y/n)")
    if user_input == "y":
        new_life_started = True
        break
    elif user_input == "n":
        new_life_started = False
        clear_console()

#code to prepare the variables for writing and reading by giving them their respective preset values
new_life_started = True
print("Welcome to Tomato stocks! Please wait while the game prepares itself.")
print("Resetting variables, please wait...")
time.sleep(0.1)
money = 1
time.sleep(0.1)
tomato_price = 2
time.sleep(0.1)
current_day = 1
time.sleep(0.1)
tomatoes_currently_growing = False
time.sleep(0.1)
tomato_seeds = 0
time.sleep(0.1)
fertilizer_quantity = 0
time.sleep(0.1)
tomato_stock = "∞" #infinity cannot be a number value in a python variable so it must be a text value
time.sleep(0.1)
has_grow_light = False
time.sleep(0.1)
grow_light_stock = 1
time.sleep(0.1)
fertilizer_stock = 10
time.sleep(0.1)
user_in_shop = False
time.sleep(0.1)
new_day_started = False
time.sleep(0.1)
has_housing = False
time.sleep(0.1)
tomatoes_currently_growing_with_fertilizer = False
time.sleep(0.1)
amount_of_tomatoes_growing = 0
time.sleep(0.1)
amount_of_tomatoes_grown = 0
time.sleep(0.1)
max_buy = 0

print("Done")
clear_console()
print("Loading intro...")
time.sleep(0.6)
print("You start out poor and homeless. You only have 1 dollar and you must use this 1 dollar to grow tomatoes in an infinite loop to make as much money as possible.")
time.sleep(1)
print("Welcome to Tomato stocks brought to you by Tomako studios!")
time.sleep(0.4)

#script for day cycle and anything dependant on it
def day_cycle():
    global current_day
    while True:
        time.sleep(1800)  # 1800 seconds = 30 minutes (full day)
        current_day += 1
        print("\nA new day has started!")
        print(f"You are now on day: {current_day}")
        print("Press 'enter' to continue.")  
pass

#script for tomato growth (threaded)
def tomato_growth():
    global tomatoes_currently_growing
    global tomatoes_currently_growing_with_fertilizer
    global has_grow_light
    global amount_of_tomatoes_growing
    global amount_of_tomatoes_grown
    global money
    global tomato_price

    while True:
        if tomatoes_currently_growing_with_fertilizer and has_grow_light:
            time.sleep(120) # 120 seconds = 2 minutes which is the growth time with fertilizer and grow light
            print("\nThe tomatoes have finished growing. They have been automatically harvested.", flush=True)
            amount_of_tomatoes_grown = amount_of_tomatoes_growing * 4
            money += amount_of_tomatoes_grown * tomato_price
            tomatoes_currently_growing_with_fertilizer = False
            tomatoes_currently_growing = False
            print("Tomato stocks>", end="", flush=True)

        elif tomatoes_currently_growing_with_fertilizer:
            time.sleep(240) # 240 seconds = 4 minutes the growth time with fertilizer
            print("\nThe tomatoes have finished growing. They have been automatically harvested.", flush=True)
            amount_of_tomatoes_grown = amount_of_tomatoes_growing * 4
            money += amount_of_tomatoes_grown * tomato_price
            tomatoes_currently_growing_with_fertilizer = False
            tomatoes_currently_growing = False
            print("Tomato stocks>", end="", flush=True)

        elif tomatoes_currently_growing and has_grow_light:
            time.sleep(480) # 480 seconds = 8 minutes the growth time with grow light
            print("\nThe tomatoes have finished growing. They have been automatically harvested.", flush=True)
            amount_of_tomatoes_grown = amount_of_tomatoes_growing * 4
            money += amount_of_tomatoes_grown * tomato_price
            tomatoes_currently_growing = False
            print("Tomato stocks>", end="", flush=True)

        elif tomatoes_currently_growing:
            time.sleep(960) # 960 seconds = 16 minutes which is base growth time for tomatoes
            print("\nThe tomatoes have finished growing. They have been automatically harvested.", flush=True)
            amount_of_tomatoes_grown = amount_of_tomatoes_growing * 4
            money += amount_of_tomatoes_grown * tomato_price
            tomatoes_currently_growing = False
            print("Tomato stocks>", end="", flush=True)

        else:
            time.sleep(1)
                        

#code for the actual game
threading.Thread(target=tomato_growth, daemon=True).start()
threading.Thread(target=day_cycle, daemon=True).start()

print("Type 'help' for commands.")
while True:
    user_input = input("Tomato stocks>") 

#script that displays the help message
    if user_input == ("help"):
        print("Command list.")
        print("help - displays this message")
        print("current day - displays the current day")
        print("balance - shows your current balance")
        print("tomato price - displays the current price of your tomatoes")
        print("inventory - opens the inventory")
        print("quit game - quits the game")
        print("exit - exits the current menu the user is in")
        print("shop - opens the shop where you can buy different items")
        print("product info - shows item prices and stock (when in shop)")
        print("buy tomato seeds - purchases tomato seeds (when in shop)")
        print("buy fertilizer - purchases fertilizer (when in shop)")
        print("buy grow light - purchases grow light (when in shop)")
        print("plant tomatoes - plants tomatoes using available seeds")
        print("clear - clears the screen")
        #print("export - exports your progress to a file")
        #print("import - imports saved progress from a file")
        #print("use - allows the user to use items from inventory")
        #print("set price - sets the tomato selling price (minimum $2)")
        #print("time till maturity - shows time until tomatoes are ready")
        print("NOTE: ALL COMMANDS ARE CASE SENSITIVE")
    
#script that displays the current day you are on
    if user_input == ("current day"):
        print(f"Day: {current_day}")    

#script to display the users balance
    if user_input == ("balance"):
        print(f"Current balance: ${money}")

#script to display what is in the users inventory
    if user_input == ("inventory"):
        print("Items in your inventory.")
        print(f"Tomatoes: {tomato_seeds}")
        print(f"Fertilizer: {fertilizer_quantity}")    
        
#script to display the current price of your tomatoes
    if user_input == ("tomato price"):
        print(f"Current tomato price: ${tomato_price}")
        
#script to quit the game
    if user_input == ("quit game"):
     result_bool = messagebox.askyesno("Quit game", "Are you sure you want to quit the game as of now this will reset your progress.")
     if result_bool:
         result_bool = messagebox.askyesno("Quit game", "Are you absolutely sure you want to quit? again this WILL RESET your progress!")
         if result_bool:
             quit()
         else:
             pass
     else:
         pass
     
#script to show shop
    if user_input == ("shop"):
        user_in_shop = True
        print("Type 'buy' [item name] to buy an item (case sensitive).")
        print("Type 'product info' to get item stocks and prices (case sensitive).")
        print("Type 'shop commands' for a list of the different commands to buy items from the shop (case sensitive).")
        while user_in_shop == True:
            user_input = input("shop>")    
            if user_input == ("product info"):
                print("Tomato seeds | $1 | stock: " + tomato_stock)
                print(f"Fertilizer | $10 | stock: {fertilizer_stock}")
                print(f"Grow light | $500 | stock: {grow_light_stock}")
            if user_input == ("shop commands"):
                print("buy tomato seeds - purchases tomato seeds")
                print("buy fertilizer - purchases fertilizer")
                print("buy grow light - purchases grow light")
            if user_input == ("buy tomato seeds"):
                print("Processing...")
                if money >= 1:
                    max_buy = money // 1
                    if max_buy > 1:
                        try:
                            qty = int(input(f"How many tomato seeds do you want to buy? (max {max_buy}): "))
                            if 1 <= qty <= max_buy:
                                money -= qty * 1
                                tomato_seeds += qty
                                print(f"Bought {qty} tomato seeds, you now have ${money} remaining.")
                            else:
                                print(f"Invalid quantity. Must be between 1 and {max_buy}.")
                        except ValueError:
                            print("Please enter a valid number.")
                    else:
                        money -= 1
                        tomato_seeds += 1
                        print(f"Bought 1 tomato seed, you now have ${money} remaining.")
                else:
                    print("Not enough money to buy tomato seeds.") 
            pass         
            if user_input == ("buy fertilizer"):
                print("Processing...")
                if fertilizer_stock > 0:
                    if money >= 10:
                        max_buy = min(money // 10, fertilizer_stock)
                        if max_buy > 1:
                            try:
                                qty = int(input(f"How many fertilizer do you want to buy? (max {max_buy}): "))
                                if 1 <= qty <= max_buy:
                                    money -= qty * 10
                                    fertilizer_quantity += qty
                                    fertilizer_stock -= qty
                                    print(f"Bought {qty} fertilizer, you now have ${money} remaining.")
                                else:
                                    print(f"Invalid quantity. Must be between 1 and {max_buy}.")
                            except ValueError:
                                print("Please enter a valid number.")
                        else:
                            money -= 10
                            fertilizer_quantity += 1
                            fertilizer_stock -= 1
                            print(f"Bought 1 fertilizer, you now have ${money} remaining.")
                    else:
                        print("Not enough money to buy fertilizer!")
                else:
                    print("Insufficient stock!")
            pass   
            if user_input == ("buy grow light"):   # TODO/FIXME: Make it so you can only buy grow light if you have a house
                print("Processing...")
                if grow_light_stock >= 1:        
                    if money >= 500:
                        money -= 500
                        has_grow_light = True
                        grow_light_stock -= 1
                        print(f"bought 1 grow light, you now have ${money} remaining.")
                    elif money < 500:
                        print("Not enough money to buy grow light!")        
                elif grow_light_stock == 0:
                    print("You already have the grow light!")
            pass  
            if user_input == ("exit"):
                print("Exiting shop...")
                time.sleep(1)
                user_in_shop = False
        pass
    
#script for planting tomatoes
    if user_input == "plant tomatoes":
        print("Processing...")
        if tomato_seeds >= 1:
            if fertilizer_quantity >= 1:
                choice = input("would you like to use fertilizer? (y/n) ")
                if choice == "y":
                    print(f"Planted {tomato_seeds} tomatoes with fertilizer")
                    fertilizer_quantity -= 1
                    tomatoes_currently_growing_with_fertilizer = True
                    tomatoes_currently_growing = True
                    amount_of_tomatoes_growing = tomato_seeds
                    tomato_seeds = 0
                else:
                    print(f"Planted {tomato_seeds} tomatoes without fertilizer")
                    tomatoes_currently_growing = True
                    amount_of_tomatoes_growing = tomato_seeds
                    tomato_seeds = 0
            else:
                # Automatic planting if not enough fertilizer for all seeds
                print(f"Planted {tomato_seeds} tomatoes (not enough fertilizer for all)")
                tomatoes_currently_growing = True
                amount_of_tomatoes_growing = tomato_seeds
                tomato_seeds = 0
        else:
            print("Not enough tomato seeds to plant tomatoes!")
    pass

#script for clearing the screen
    if user_input == "clear":
        clear_console()

# script for tomato growth 
#    if tomatoes_currently_growing == "true":
#        time.sleep(960)  # 960 seconds = 16 minutes which is base growth time for tomatoes
#        print("tomatoes done growing they have been automatically harvested")
#        amount_of_tomatoes_grown = amount_of_tomatoes_growing * 4 
#        money = amount_of_tomatoes_grown * tomato_price
#    elif tomatoes_currently_growing == "true" and has_grow_light == "true":
#        time.sleep(480) # 480 seconds = 8 minutes half the growth time 
#        print("tomatoes done growing they have been automatically harvested")
#        money = amount_of_tomatoes_grown * tomato_price
#    elif tomatoes_currently_growing_with_fertilizer:
#        time.sleep(240) # 240 seconds = 4 minutes quarter of the growth time
#        print("tomatoes done growing they have been automatically harvested")
#        amount_of_tomatoes_grown = amount_of_tomatoes_growing * 4 
#        money = amount_of_tomatoes_grown * tomato_price
#    elif tomatoes_currently_growing_with_fertilizer == "true" and has_grow_light == "true":   
#        time.sleep(120)
#        print("tomatoes done growing they have been automatically harvested")
#        amount_of_tomatoes_grown = amount_of_tomatoes_growing * 4 
#        money = amount_of_tomatoes_grown * tomato_price

#the code above is deprecated and will most likely stay unused and may be deleted in a later version.


# script for debug
    if user_input == "show_debug":
        print("Printing debug")
        print("Showing variables")
        print(f"Money: ${money}")
        print(f"New Day Started: {new_day_started} (unused variable)")
        print(f"New Life Started: {new_life_started}")
        print(f"Tomato price: ${tomato_price}")
        print(f"Current day: {current_day}")
        print(f"Tomatoes currently growing: {tomatoes_currently_growing}")
        print(f"Tomato seeds: {tomato_seeds}")
        print(f"Fertilizer quantity: {fertilizer_quantity}")
        print(f"Tomato stock: {tomato_stock}")
        print(f"Fertilizer stock: {fertilizer_stock}")
        print(f"Grow light stock: {grow_light_stock}")
        print(f"Has grow light: {has_grow_light}")
        print(f"User in shop: {user_in_shop}")
        print(f"Has housing: {has_housing}")
        print(f"Tomatoes currently growing with fertilizer: {tomatoes_currently_growing_with_fertilizer}")
        print(f"Amount of tomatoes growing: {amount_of_tomatoes_growing}")
        print(f"Amount of tomatoes grown: {amount_of_tomatoes_grown}")
        print(f"Max buy: {max_buy}")

    
    
    
# TODO:  Add commands listed below 
#//-current day
#//-help
#//-balance
#//-tomato price
#//-quit game
#-export (used for exporting your progress to a file so you can continue where you left off)
#-import (used for importing saves)
#//-inventory
#-use (allows the user to use items they have in their inventory) (this command will most likely not be added to the game)
#//-shop
#//-exit (exits the current menu the user is in like the inventory or shop)
#//-plant tomatoes
#-set price (sets the tomato inflation price that you sell your tomatoes at (minimum $2)) (this command  may be left out for simplicity)
#-time till maturity (tells the user how long until the tomatoes are mature)
#//-Add shop system to buy different items 
#-add a housing system and tax system 
#//-Add items to the shop that are listed below
#//-Tomato seeds
#//-Fertilizer (decrease tomato growth time to 4 mins) 
#//-Grow light (decreases the overall grow time of plants (can only go down to 15 minutes out of 30 minutes))
#-1 bedroom apartment ($5k)
#-2 bedroom bungalow ($20k)
#-3 bedroom house ($50k)


# NOTE: base growth time for tomatoes = 16 mins | with grow light = 8 mins | with fertilizer = 4 mins | with fertilizer and grow light = 2 mins
# TODO: Add Enhanced gameplay DLC
# add the items to enhanced gameplay DLC listen below
# TODO: Add tax system
