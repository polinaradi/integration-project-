"""A game which lets the user decide how to spend one million dollars. """

__author__ = "Polina Radinsky"


# Polina Radinsky
# a program which integrates the skills and concepts that I have learned
# Source I used for if, elif, and else statements https://www.programiz.com/python-programming/if-elif-else
# def defines a function
def main():
    """
This function is the beginning of the program. It prints out instructions.
    """
    congrats = "Congratulations! You won "
    million = "one million dollars!"
    # the + concatenates the strings together
    statement = congrats + million
    # the print function outputs a message on the screen
    print(statement)
    # the end=" " statement ends the last line with a space before the next line
    print("Decide on what you would like to spend your money on.", end=" ")
    print("Please enter 'yes' or 'no'.")


# source I used for the main function -
# https://www.programiz.com/python-programming/main-function
if __name__ == "__main__":
    main()

print("Have you won enough to buy everything offered?")
# returns False because not is used to reverse the actual result
mil = 1000000
print(not (mil > 0 and 0 < mil))
# answer is a variable
# a variable is a name for a location in memory
# input is a function that allows the user to enter data
answer = input("Would you like to buy a Toyota Camry for $24,425? ")
toyota = 24425
helicopter = 600000
# the if statement executes the body only when the user inputs a "yes"
# == means equal to
if answer == "yes":
    # ** means exponentiation
    # // means floor division
    toy_limit = (1000 ** 2) // 24425
    print("Okay! Your maximum limit is", toy_limit)
    # try: causes an exception that allows the program to jump to except
    # except: is the exception for the try statement
    # int turns the string into an integer
    # the break statement ends the loop but isn't required
    # source for program not crashing when a string is entered
    #https://sites.google.com/site/profvanselow/swebok/cmp-cf/15-human-factors
    while True:
        try:
            # the int function converts the amount purchased into an integer
            t_limit = int(input("How many would you like to purchase? "))
            break
        except ValueError:
            print("Error. Must be a whole number.")
        # int turns the string into an integer
        # % means modulus
    toy_amount = int(t_limit) * (toyota % mil)
    # - means subtraction
    toys_balance = mil - toy_amount
    # != means not equal to
    while mil != toys_balance:
        # sep="" is a separator between commas
        print("Your remaining balance is $", toys_balance, sep="")
        # break stops the true statement from looping
        break
    # / means division
    # * means multiplication
    toy_percent = int(toy_amount) / 1000000 * 100
    # sep="" is a separator between commas
    print("Out of your initial balance, a toyota cost %", toy_percent, sep="")
    print("Based on your purchase history, do you have enough money to purchase a helicopter? ")
    # prints True if both statements are true
    print(toys_balance > helicopter and helicopter < toys_balance)
    # <= means less than or equal to
    if toys_balance <= 600000:
        print("Thanks for playing!")
        print("Please try again and use yes or no")
    # >= means greater than or equal to
    if toys_balance >= 600000:
        answer = input("Would you like to buy a Helicopter for $600,000? ")
        if answer == "no":
            print("Thanks for playing!")
        if answer == "yes":
            # range is a function which returns a list of numbers up to one before the specified number from 0
            # in checks if a value exists in a sequence
            for y in range(2):
                print("Your helicopter purchase can be limited to", y)
            heli_limit = int(toys_balance) // 600000
            h_limit = input("How many would you like to purchase? ")
            heli_amount = int(h_limit) * 600000
            helis_balance = toys_balance - heli_amount
            print("Your remaining balance is $", helis_balance, sep="")
            heli_percent = (int(toy_amount) + int(heli_amount)) / 1000000 * 100
            print("Out of your initial balance, your purchases cost %", heli_percent, sep="")
            print("Thanks for playing!")
            print("Please try again and use yes or no")
        else:
            print("Please try again and use yes or no")

elif answer == "no":
    print("Based on your purchase history, do you have enough money to purchase a helicopter? ")
    # prints True if one of the conditions is true
    print(mil > helicopter or helicopter < mil)
    answer = input("Would you like to buy a Helicopter for $600,000? ")
    if answer == "no":
        print("Thanks for playing!")
        print("Please try again and use yes or no")
    elif answer == "yes":
        heli_limit = 1000000 // 600000
        answer = ["Okay! Your maximum limit is", heli_limit]
        # for executes a set of statements
        for x in answer:
            print(x)
            while True:
                try:
                    h_limit = int(input("How many would you like to purchase? "))
                    break
                except ValueError:
                    print("Error. Must be a whole number.")
        heli_amount = h_limit * 600000
        helis_balance = mil - heli_amount
        print("Your remaining balance is $", helis_balance, sep="")
        heli_percent = int(heli_amount) / 1000000 * 100
        print("Out of your initial balance, your purchases cost %", heli_percent, sep="")
        print("Thanks for playing!")
        print("Please try again and use yes or no")
    else:
        print("Please try again and use yes or no")

else:
    print("Please try again and use yes or no")


# def defines a function
def endgame():
    """
This function executes at the end of the game and prints three dots.
    """
    period = "."
    # the * multiplies the string
    end = period * 3
    print(end)


# the function endGame is returning the parameter collected
endgame()
