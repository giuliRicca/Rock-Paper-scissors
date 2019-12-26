import random
from time import sleep as slp

options = 'rock paper scissors'.split()
score = [0,0]

def game():
    while(True):
        print('rock!')
        slp(.5)
        print('paper!')
        slp(.5)
        print('scissors!')
        slp(.5)
        user_pick = input('Your: ').lower()
        comp_pick = options[random.randint(0,3)]
        print('Me: ' + comp_pick)
        
        if user_pick != comp_pick:
            if (user_pick == 'rock'):
                if comp_pick == 'scissors':
                    score[0] += 1
                    print('You win!')
                    print('Score: ' + str(score))
                    slp(1)
                else:
                    score[1] += 1
                    print('I won!')
                    print('Score: ' + str(score))
                    slp(1)
                    
            if (user_pick == 'paper'):
                if comp_pick == 'scissors':
                    score[1] += 1
                    print('I won!')
                    print('Score: ' + str(score))
                    slp(1)
                else:
                    score[0] += 1
                    print('You won!')
                    print('Score: ' + str(score))
                    slp(1)
                    
            if (user_pick == 'scissors'):
                if comp_pick == 'rock':
                    score[1] += 1
                    print('I won!')
                    print('Score: ' + str(score))
                    slp(1)
                else:
                    score[0] += 1
                    print('You won!')
                    print('Score: ' + str(score))
                    slp(1)


            if input('Wanna play again? (y/n)').lower() == 'n':
                print('Goodbye!')
                break

game()
