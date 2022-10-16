#Python homework - 15 October 


#Ask for the total price of the bill, then ask how many diners there are. Divide the total bill by the number of diners and show how much each person must pay. 

def totalbill():
    totalbill = int(input("What is the total bill?: "))
    diners = int(input ("How many diners are?: "))

    return totalbill/diners

print(totalbill())

#Ask the user’s age. If they are 18 or over, display the message “You can vote”. If they are aged 17, display the message “You can learn to drive”. If they are 16, display the message, “You can buy a lottery ticket”. If they are under 16, display the message “You can go trick or treating” 

age=int(input("What is your age?"))
if age >= 18:
  print("You can vote!")
elif age == 17:
  print("You can learn to drive!")
elif age == 16:
  print("You can buy a lottery ticket!")
else:
  print("You can go trick or treating!")


