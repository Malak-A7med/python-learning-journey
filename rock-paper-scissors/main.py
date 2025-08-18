import random
user_score = 0
computer_score = 0
lst = ["paper", "rock", "scissors"]

while True:
    ch1 = input("Enter paper, rock or scissors: ").lower()
    ch2 = random.choice(lst)

    print("Your Choice:", ch1)
    print("Computer Choice:", ch2)

    if ((ch1 == "paper" and ch2 == "scissors") or 
        (ch1 == "rock" and ch2 == "paper") or 
        (ch1 == "scissors" and ch2 == "rock")):
        print("I Won!!!")
        computer_score += 1
    elif ch1 == ch2:
        print("It's a draw!")
    elif ((ch2 == "paper" and ch1 == "scissors") or 
          (ch2 == "rock" and ch1 == "paper") or 
          (ch2 == "scissors" and ch1 == "rock")):
        print("You Won")
        user_score += 1
    else:
        print("Invalid input.")

    print(f"Score → You: {user_score} | Computer: {computer_score}")
    print("-" * 30)

    msg = input("Do you want to continue? (y/n): ").lower()
    if msg != 'y':
        print("Final Score:")
        print(f"You: {user_score} | Computer: {computer_score}")
        print("Goodbye")
        break
