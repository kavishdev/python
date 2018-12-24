from random import randint

print('Let\'s play Stone, Paper and Scissors !!!!')
 
ROUNDS = input('How many rounds you want to Play ??  : ')
ROUNDS=int(ROUNDS)
TOTALWIN = 0
DRAW = 0
print('\n ========== GAME START  ==============')
for x in range(ROUNDS):
  print('ROUND ',x)
  player = input(' rock(r),paper(p)scissors(s) : ')

  
  chosen = randint(1,3)
  #print(chosen)

  if chosen == 1:
    computer = 'r'

  elif chosen == 2:
    computer = 'p'
  elif chosen == 3:
    computer = 's'
    
  print(player, 'vs', computer ) 

  if player == computer:
      print('DRAW!!!!!')
      DRAW = DRAW+1

  elif player == 'r'and computer == 's':
          print ('You win!!!!!')
          TOTALWIN = TOTALWIN+1

  elif computer == 'p' and player == 'r':
          print ('Computer wins!!!!')

  elif player == 'p' and computer == 'r':
          print('You win!!!!')
          TOTALWIN = TOTALWIN+1
      
  elif computer == 's'and player == 'p':
          print('Computer wins!!!!')

  elif player == 's' and computer == 'p':
          print('You win!!!!')
          TOTALWIN = TOTALWIN+1
      
  elif computer == 's'and player == 'p':
          print('Computer wins!!!!')

  elif  player == 's' and computer == 'r':
          print('Computer wins!!!!')     

  elif player == 'p' and computer == 's':
          print('Computer wins!!!!')

print('\n ========== RESULT  ==============')
print('No. of Draw(s) = ',DRAW)
COMPCOUNT = ROUNDS-TOTALWIN-DRAW
print('Score : You vs Computer  \n      = ',TOTALWIN,' vs ',COMPCOUNT)


if COMPCOUNT>TOTALWIN:
  print('FINAL WINNER is COMPUTER')
else:
  print('Congratulations !! You won')