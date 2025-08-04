import random 
total_lives=7
hits=0
lst=["apple","breeze","cactus","jasmine","kaleidoscope"]
word=random.choice(lst)
pattern=len(word)*["__"]
print(' '.join(pattern).center(10))
while(total_lives>0 and hits<len(word)):
    alph=input("\nGuess the letter: ").lower()
    if alph in word:
        for index,i in enumerate(word):
            if i==alph:
                if pattern[index]=="__":
                    pattern[index]=alph
                    hits+=1
        print(' '.join(pattern).center(10))
    else:
        total_lives-=1
        print(f"Total lives left: {total_lives}")
    if hits==len(word):
        print("Congrats you won")  
        break
if(total_lives==0):
    print("Sorry you lost")
    print(f"The word was {word}")
