##Name: Melissa Aguilar

##change_Calculator_Aguilar.py

##This program will allow the user to enter the price of an item they want to buy
    ##then enter the amount of cash they have so the program can return their exact change

def main():

    ##Purpose
    print("\n\t\t\tWelcome to Change Calculator!\n")
    print("This program will calculate how much change you will receive on your recent purchase.\n")

    ##Input variable
    value_of_Items = float(input("Please enter the total cost: "))
    round(value_of_Items, 2)

    #Validate the value of the item(s)
    if value_of_Items <= 0:
        print("\nInvalid amount given - Try Again")
        value_of_Items = float(input("Please enter an amount greater than zero: "))
        round(value_of_Items, 2)

    # Input variable
    money_Given = float(input("\nEnter how much money given: "))
    round(money_Given, 2)

    #Validate the amount of money given
    if money_Given <= 0:
        print("\nInvalid amount given - Try Again")
        money_Given = float(input("Please enter an amount greater than zero: "))
        round(money_Given, 2)

    #Calculate the amount that should be given back
    change_amount = abs(value_of_Items - money_Given)

    print("\nWe owe you: ${0:0.2f}".format(change_amount))

    change_amount = change_amount * 100

    # Change in coins
    quarters = 25
    dimes = 10
    nickels = 5
    pennies = 1

    #Calculate the change
    number_of_Quarters = change_amount // quarters
    q_change = change_amount - (number_of_Quarters * quarters)

    number_of_Dimes = q_change // dimes
    d_change = q_change - (number_of_Dimes * dimes)

    number_of_Nickels = d_change // nickels
    n_change = d_change - (number_of_Nickels * nickels)

    number_of_Pennies = n_change

    number_of_Coins = int(number_of_Quarters + number_of_Dimes + number_of_Nickels + number_of_Pennies)

    # Output results
    print("\nHere is your change:")
    print("Quarters: ", int(number_of_Quarters))
    print("Dimes: ", int(number_of_Dimes))
    print("Nickels: ", int(number_of_Nickels))
    print("Pennies: ", int(number_of_Pennies))

    print("\nThere are a total of ", number_of_Coins, " coins.")

   #Ask user if they want to restart the program
    user_restart = input("\nDo you want to calculate other change? [Y/N]: ").upper()
    if user_restart == 'Y' or user_restart == 'YES':
        main()
    elif user_restart == 'N' or user_restart == 'NO':
        print("\nThank you and come again!")
    else:
        print("\nInvalid - Try Again")
        user_restart = input("\nDo you want to calculate other change? [Y/N]: ").upper()

main()












