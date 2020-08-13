suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
#This is a comment
total_chips=0
bet_chips=0
def bet():
    global total_chips,bet_chips
    while True:
        try:
            total_chips=int(input('How many chips would you like to buy?'))
        except:
            print("Oops! it is not a number. Try again")       
        else:
            break
    while True:
        try:
            bet_chips=int(input('Enter the number of chips you would want to bet'))
        except:
            print("Oops! It is not a number. Try again")       
        else:
            break

    if bet_chips> total_chips:
        print('You can\'t exceed {}, the total chips purchased'.format(total_chips))        


#setting up deck func
def Deck():
    deck=[]
    for suit in suits:
        for rank in ranks:
            deck.append((rank,suit))

    from random import shuffle
    shuffle(deck)
    return deck


#cards distribute to players function 
cards_p=[]
cards_d=[]
def cards_distr_player(deck):

    global cards_p

    a1,b1=deck.pop()
    a2,b2=deck.pop()


    cards_p.append((a1,b1))
    cards_p.append((a2,b2))

    return a1,a2

#cards distribute to dealer function 
a4=0
b4=0
def cards_distr_dealer(deck):

    global cards_d,a4,b4

    a3,b3=deck.pop()
    a4,b4=deck.pop()

    cards_d.append((a3,b3))
    cards_d.append((a4,b4))

    return a3,a4
#initial value calc func
sum_p=0
sum_d=0
def value_calc_init(who,val1,val2):
    sum=0
    global sum_p
    global sum_d

    if who=='p':
        sum_p= sum_p + values [val1] + values [val2]
        sum=sum_p

    elif who=='d':
        sum_d=sum_d + values [val1] + values [val2]
        sum=sum_d

#value calculate func
def value_calc(who,val):
    sum=0
    global sum_p
    global sum_d

    if who=='p':
        sum_p= sum_p + values [val] 
        sum=sum_p

    elif who=='d':
        sum_d= sum_d + values [val] 
        sum=sum_d



#cards show for dealers func
def show_dealers_cards(cards_list_player):
    print('\nDealer\'s cards are:')
    print('<Hidden Card>')
    print(a4 + ' of ' + b4 ) 


#cards show for players func
def show_players_cards(cards_list):
    print('\nThe player\'s cards are:')
    for rank,suit in cards_list:
        print(rank + ' of ' + suit)

#hit or stand func
flag=0
def hit_or_stand():

    hit_stand=input('\nDo you want to hit or stand?: h or s ')
    if hit_stand=='h':
        hit('p',deck1,sum_p)
    else:
        global flag
        flag=1  
    return hit_stand
#hit func 
def hit(who,deck,sum):

    flag=0
    a3,b3=deck.pop()


    global cards_p
    global cards_d


    if who=='p':  
        cards_p.append((a3,b3))

    elif who=='d':
        cards_d.append((a3,b3))  

    if sum <=10:
        values ['Ace']= 11
    else:
        values ['Ace']=1
        flag=1

    value_calc(who,a3)

    if flag==1:
        values ['Ace']=11



# player bust function
bust=0
def player_bust(val):

    global bust
    if val>21:
        print('\nPlayer busts! Dealer wins.')
        print('Player\'s winnings stand at {}'.format(total_chips-bet_chips))
        bust=1
    return bust

# show all dealers cards
def show_all_dealers_cards(cards_list):
    print('\nThe Dealer\'s cards are:')
    for rank,suit in cards_list:
        print(rank + ' of ' + suit)

# dealer hit func
def dealer_hit(sum):
    sum_less_17=0
    if sum<17:
        hit('d',deck1,sum_d)
        sum_less_17=1
    return sum_less_17  

# show final cards with values
def show_final_cards(cards_list_player,cards_list_dealer):
    print('The player\'s cards are:')
    for rank,suit in cards_list_player:
        print(rank + ' of ' + suit)
    print('Player\'s hand: {}'.format(sum_p))

    print('\nThe dealer\'s cards are:')
    for rank,suit in cards_list_dealer:
        print(rank + ' of ' + suit)
    print('Dealer\'s hand: {}'.format(sum_d))

# check who wins
def win_check(sum_player,sum_dealer):
    if sum_player > sum_dealer or sum_dealer>21:
        print('THE PLAYER WINS!')
        print('Player\'s winnings stand at {}'.format(total_chips+bet_chips))

    elif sum_player < sum_dealer and sum_dealer<=21:
            print('THE DEALER WINS!')
            print('Player\'s winnings stand at {}'.format(total_chips-bet_chips))

    else:
        print('It was a draw!')


#main code
print('Welcome to BlackJack! Get as close to 21 as you can without going over!')
print('Dealer hits until it reaches 17. Aces count as 1 or 11.')   
# bet func call
bet()

# Deck call func
deck1=Deck()

# cards distribute for dealers plus initial value calc
val3,val4=cards_distr_dealer(deck1)
value_calc_init('d',val3,val4)

#call cards show for dealers
show_dealers_cards(cards_d)

# cards distribute for players plus initial value calc
val1,val2=cards_distr_player(deck1)
value_calc_init('p',val1,val2)

#call cards show for players
show_players_cards(cards_p)

hs_flag=1
while hs_flag:
    hs=hit_or_stand()
    if hs=='h':
        show_dealers_cards(cards_d)
        show_players_cards(cards_p)
        hs_flag=not player_bust(sum_p)

        ############

    else:
        hs_flag=0 

if hs_flag==0 and bust==0:
    print('\nPlayer stands. Dealer is playing')
    show_all_dealers_cards(cards_d)
    show_players_cards(cards_p)
    print('\n')

    dh=1
    while dh:
        dh=dealer_hit(sum_d)
        if dh==1:
            show_all_dealers_cards(cards_d)
            show_players_cards(cards_p)
            print('\n')
        else:
            dh=0
            print('The final evaluation is as:\n')
            show_final_cards(cards_p,cards_d)
            print('\n')
            win_check(sum_p,sum_d)

else:
    pass


