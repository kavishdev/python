from random import randint
ROUNDS = input('How many rounds you want to Play ??  : ')
ROUNDS=int(ROUNDS)
TOTALWIN = 0
DRAW = 0
print('\n ========== GAME START  ==============')
for x in range(ROUNDS):
  print('ROUND ',x)
  player = input(' bomb(b), flat(f), gun(g) : ')



print(player, 'vs', end=' ') 

chosen = randint(1,3)
#print(chosen)

if chosen == 1:
  computer = 'b'

elif chosen == 2:
  computer = 'f'
elif chosen == 3:
  computer = 'g'
  
print(computer)

if player == computer:
    print('DRAW!!!!!')

elif player == 'b'and computer == 'f':
        print ('You win!!!!!')
        TOTALWIN = TOTALWIN+1

elif computer == 'b' and player == 'f':
        print ('Computer wins!!!!')

elif player == 'g' and computer == 'b':
         print('You win!!!!')
         TOTALWIN = TOTALWIN+1

elif computer == 'g'and player == 'b':
         print('Computer wins!!!!')

elif player == 'f' and computer == 'g':
         print('You win!!!!')
         TOTALWIN = TOTALWIN+1

elif computer == 'f'and player == 'g':
         print('Computer wins!!!!')


print('\n ========== RESULT  ==============')
COMPCOUNT = ROUNDS-TOTALWIN-DRAW
print('Score : You vs Computer  \n      = ',TOTALWIN,' vs ',COMPCOUNT)


if COMPCOUNT>TOTALWIN:
  print('FINAL WINNER is COMPUTER')
else:
  print('Congratulations !! You won')

 