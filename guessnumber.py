import sys, random
def Loop():
 randomnumber= random.randint(1,11)
 print("Guess my random number!")
 for i in range(0,3):
    print("You have " + str(3-i) + " guesses left." )
    userguess= int(input())
    if userguess > randomnumber:
        print("Your guess is too high.")
    elif userguess < randomnumber:
        print("Your guess is too low.")
    elif userguess == randomnumber:
        print("It's correct.")
        print("Do you want to play again? [y or n]")
        if input() =="y":
         Loop()
        elif input() =="n":
         sys.exit("Fun is over.")
    if i ==2:
     print("You lose. You have 0 guesses left.")
     print("Do you want to play again? [y or n]")
     if input() =="y":
       Loop()
     elif input() =="n":
       sys.exit("Fun is over.")
Loop()






