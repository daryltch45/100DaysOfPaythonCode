import random
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
choices = [rock, paper, scissors]
replay = 'y'
while replay=='y':
    choice = int(input('What do you choose ? Type 0 for Rock,1 for Paper or 2 for Scissors.'))
    if choice >= 0 and choice <= 2 :
        user_choice=choices[choice]
        print(user_choice)
        print('Computer choose: ')
        computer_choice = random.choice(choices)
        print(computer_choice)
        if computer_choice == user_choice:
            print('It\'s a tie!')
        else:
            if (computer_choice == rock and user_choice == scissors)\
            or (computer_choice == scissors and user_choice == paper)\
            or (computer_choice == paper and user_choice == rock):
                print('You loose!')
            else:
                print('You win!')
        replay= (input('Do you want to play again? (y/n) ')).lower()
    else:
        print('Invalid Choice !')

