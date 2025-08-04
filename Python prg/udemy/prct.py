import random
lst=["apple","breeze","cactus","jasmine","kaleidoscope"]
word=random.choice(lst)
print("Welcome to Hangman !")
pattern=len(word)*["__"]
print(" ".join(pattern).center(10))
hits=0
lives=7
while(hits<len(word) and lives>0):
    guess=input("\nGuess a letter: ").lower()
    if(guess in word):
        for index,i in enumerate(word):
            if i==guess:
                if pattern[index]=="__":
                    pattern[index]=guess
                    hits+=1
        print(' '.join(pattern).center(10))
    else:
        lives-=1
        print(f"Wrong choice {lives} lives left !")
    if(hits==len(word)):
        print("You have WON !")
        break
if(lives==0):
    print("Sorry you lost !")
    print(f"The word was {word}.")