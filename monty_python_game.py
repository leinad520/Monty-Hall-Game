from random import randrange, choice

print("You have three doors to choose from. Behind one door is the prize; two other doors have nothing. Which do you choose?")

choicesArr = ["1","2","3"]
prize = choice(choicesArr)

your_choice = input("type 1 2 or 3\n> ")

choicesArr.remove(prize)

if prize != your_choice:
    choicesArr.remove(your_choice)

opendoor = choice(choicesArr)
choicesArr.remove(opendoor)

choicesArr2 = ["1","2","3"]
choicesArr2.remove(your_choice)
choicesArr2.remove(opendoor)

print(f"You choose door {your_choice}. Now let me open one of the remaining two doors that does not have the prize, door {opendoor}.")
print(f"*opens door {opendoor} to show there is nothing there.*")
print(f"You now have the option to stick with your original choice, door {your_choice}, or switch to the other remaining door, door {choicesArr2[0]}. Switch?")
switch_decision = input("Type y or n \n> ")

if switch_decision == "y":

    if your_choice == prize:
        print(f"You lose by switching to door {choicesArr[0]}! Your original door {your_choice} had the prize")

    if your_choice != prize:
        print(f"You win by switching! You switched from door {your_choice} to door {prize} which had the prize")
        

if switch_decision == "n":

    if your_choice == prize:
        print(f"You win by not switching! Your original door {your_choice} had the prize")

    if your_choice != prize:
        print(f"You lose by not switching! The other door, door {prize}, has the prize")

