import random 
def deal_card():
    '''Returns a random card from the deck'''
    cards=[11,2,3,4,5,6,7,8,9,10,10,10]
    card=random.choice(cards)
    return card
def cal_score(cards):
    """Takes a list of cards and returns the score calculated from the cards"""
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)
user_cards=[]
computer_cards=[]
is_game_over=False
for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
user_score=cal_score(user_cards)
computer_score=cal_score(computer_cards)
print(f"Your Cards: {user_cards},Current Score: {user_score}")
print(f"Computer's first Card: {computer_cards[0]}")
if(user_score==0 or computer_score==0 or user_score>21 or computer_score>21):
    is_game_over=True



