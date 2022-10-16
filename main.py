#Python homework - 15 October 

#HLT1
#Ask for the total price of the bill, then ask how many diners there are. Divide the total bill by the number of diners and show how much each person must pay. 

def totalbill():
    totalbill = int(input("What is the total bill?: "))
    diners = int(input ("How many diners are?: "))

    return totalbill/diners

print(totalbill())

#HLT2
#Write a program that will ask for a number of days and will then show how many hours, minutes and seconds are in that number of days 

days=int(input("Please enter the number of days:"))
hours = days*24
minutes = hours*60
seconds = minutes*60

print("In", days, "days, there are")
print(hours, "hours")
print(minutes, "minutes")
print(seconds, "seconds")

#HLT3
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


#HLT4
#Ask the user to enter their first name. If the length of their first name is under five characters, ask them to enter their surname and display their full name in upper case. If the length of the first name is five or more characters, display their name in lower case. 
  
fname = input("Please enter your first name:")
lname = input("Please enter your last name:")
if fname <= '5':
  print(fname.upper())

  
#HLT5
#Ask how many people the user wants to invite to a party. If they enter a number below 10, ask for the names and after each name display “name” has been invited. If they enter a number which is 10 or higher, display the message “Too many people”. 

num=int(input("How many friends do you want to invite to the party?"))
if num < 10:
  for i in range(0, num):
    name = input ("Enter a name:")
    print(name, "has been invited")
else:
  print("Too many people!")