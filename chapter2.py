

print('''
Hello, I have written this in Python.My name is Kavish.I am will be 10 on 3rd April. I study in fifth (5th) standard. My hobbies are:
Outdoor-badminton & cycling 
Indoor- studying MATHS,SCIENCE AND COMPUTER
I live in Tower-5-502, SARE crescent ParC,sector-92,Gurugram-122505,Haryana.
   _________  
  |         |
  |         |
  |         |
  |         |
  |         |
  |         |
  |         |
  |         |
  |         |
  |         |
__|_________|_________''')

Myborn=input('What year were you born?')
Myborn=int(Myborn)
Myage= 2018 - Myborn
print('You are ',Myage,'years old')

Fborn=input('What year was your father born? ' )
Fborn=int(Fborn)
Fage = 2018 - Fborn
if  Fage <= 90 :
  print('You Father is ',Fage,'years old.')
else:
  print('Oh!,your father lived so long. ')
  


Mborn=input('What year was you Mother born? ' )
Mborn=int(Mborn)
Mage = 2018 - Mborn
print('Your Mother is  ',Mage,'years old.')

print('Oh, the difference between your Mothers age and Fathers age is only ',Fage-Mage,'years.')


