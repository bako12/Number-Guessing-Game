import random

# will generate from 0 to 10000
# print(random.randrange(-1,10001))
# When we don't include the first number it assumes 0 as the starter
# print(random.randrange(11))

top_of_range = input("Type a number: ")
if top_of_range.isdigit():
  top_of_range = int(top_of_range)
  if top_of_range <= 5:
    print("Please enter a number greater than 5 next time ")
  else:
    random_number = random.randrange(0, top_of_range)
    print(random_number)
else:
  print("Please enter a number next time ")

user_guess = int(input("Enter your guess "))
guess = 0
while user_guess != random_number:
  user_guess = int(input("Try again loser "))
  guess += 1

if user_guess == random_number:
  print("Congrats you loser you won! Only took you " + str(guess) +
        " guesses ")

# BTW always go int(input("Enter bla bla ")) not the other way around
# Also btw when you wanna add shi to your print dont forget to st() that bitch first
