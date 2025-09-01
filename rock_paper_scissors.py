from random import randint

choices = ["rock", "paper", "scissors"]

userChoice = ["You chose: ✊", "You chose: ✋", "You chose: ✌️"]

cpuChoice =["CPU chose: ✊", "CPU chose: ✋", "CPU chose: ✌️"]

messages = ["It's a tie!", "Sorry, You lose! But try win it next time.", "You won!"]

print("================================")
print("Rock Paper Scissors")
print("================================")
print("")
print("1) ✊")
print("2) ✋")
print("3) ✌️")
user = int(input("Pick a number: "))
computer = randint(1, 3)

x = """
user = 0

firstTime = True

while user < 1 or user > 3:
    if not(firstTime):
        print("Invalid option")
    user = int(input("Pick a number: "))
    firstTime = False
"""
if user == 1 and computer == 1:
    print(userChoice[0])
    print(cpuChoice[0])
    print(messages[0])
elif user == 1 and computer == 2:
    print(userChoice[0])
    print(cpuChoice[1])
    print(messages[1])
    
elif user == 1 and computer == 3:
    print(userChoice[0])
    print(cpuChoice[2])
    print(messages[2])
elif user == 2 and computer == 1:
    print(userChoice[1])
    print(cpuChoice[0])
    print(messages[2])
elif user == 2 and computer == 2:
    print(userChoice[1])
    print(cpuChoice[1])
    print(messages[0])
elif user == 2 and computer == 3:
    print(userChoice[1])
    print(cpuChoice[2])
    print(messages[1])
elif user == 3 and computer == 1:
    print(userChoice[2])
    print(cpuChoice[0])
    print(messages[1])
elif user == 3 and computer == 2:
    print(userChoice[2])
    print(cpuChoice[1])
    print(messages[2])
elif user == 3 and computer == 3:
    print(userChoice[2])
    print(cpuChoice[2])
    print(messages[0])
else:
    print("Invalid input request")