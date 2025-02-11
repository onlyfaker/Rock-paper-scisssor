import random

list = ["""
rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
"""
paper
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
"""
scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]
player_score = 0
pc_score=0
rounds=1
print("Best out of 3")

while rounds<=3:
    player = int(input("Choose a number 0-rock, 1-paper, 2-scissors: "))
    computer = random.randint(0,2)
    print("Player chooses: ")
    print(list[player])
    print("Computer chooses: ")
    print(list[computer])

    if player==computer:
        print("This round doesnt count, go again!")
        print("Tie")
    elif (player==0 and computer==2) or (player==1 and computer==0) or (player==2 and computer==1):
        player_score = player_score + 1
        print("This is round: ",rounds)
        rounds += 1
        print("Player wins!")

    else:
        pc_score = pc_score + 1
        print("This is round: ",rounds)
        rounds += 1
        print("Computer wins!")


if player_score>pc_score:
    print("THE Final WINNER IS PLAYER!!! CONGRATS!!")
    print("The player won ",player_score," times")
else:
    print("THE Final WINNER IS Computer!!! I am smarter ha ha ha")
    print("The computer won ",pc_score," times")

