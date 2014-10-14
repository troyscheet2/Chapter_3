# Guess My Number
#
# The player picks a random number between 1 and 100
# The computer tries to guess it and the player lets
# the computer know if the guess is too high, too low
# or right on the money

import random  

print("\tWelcome to 'Guess Your Number'!")
print("\nI want you to think of a number between 1 and 100.")
print("I'll try to guess it in as few attempts as possible.\n")

# set the initial values
yournumber = int(input("Type in a number: ")
guess_number = random.randint(0, 100)
guess = int(input("Hmm...Is it", guess_number, "? Higher or lower?")
tries = 1

# guessing loop
while guess_number != yournumber: 
	if guess == "higher":
		print("Higher? Alirght, I'll try again...")
	else:
		print("Lower? Okay...")

	guess = int(input("Hmm...Is It", guess_number, "? Higher or lower?")
	tries += 1
	
if guess_number = yournumber:
print("I guessed it!  The number was", the_number)
print("And it only took me", tries, "tries!\n")
  
input("\n\nPress the enter key to exit.")
