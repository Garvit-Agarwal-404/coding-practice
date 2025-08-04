rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
options=["rock","paper","scissors"]
your_choice=input("Enter your choice :Rock,Paper or Scissors?").lower()
import random 
comp_choice=random.choice(options)
if(your_choice=="rock" and comp_choice=="scissor"):
    print(f"Your choice: {rock}")
    print(f"Computer's choice: {scissors}")
    print("You won !!!!")
elif(your_choice=="rock" and comp_choice=="paper"):
    print(f"Your choice: {rock}")
    print(f"Computer's choice: {paper}")
    print("You Loose !!!!")
elif(your_choice=="scissors" and comp_choice=="paper"):
    print(f"Your choice: {scissors}")
    print(f"Computer's choice: {paper}")
    print("You Win !!!!")
elif(comp_choice=="rock" and your_choice=="scissor"):
    print(f"Your choice: {scissors}")
    print(f"Computer's choice: {rock}")
    print("You Loose !!!!")
elif(comp_choice=="rock" and your_choice=="paper"):
    print(f"Your choice: {paper}")
    print(f"Computer's choice: {rock}")
    print("You Win !!!!")
elif(comp_choice=="scissors" and your_choice=="paper"):
    print(f"Your choice: {paper}")
    print(f"Computer's choice: {scissors}")
    print("You Loose !!!!")
elif(comp_choice == your_choice):
    print("Tie.....")
else:
    print("Invalid command")
    











