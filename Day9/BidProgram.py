import os
import art

print(art.logo)

is_anotherbidder = 'y'

user_bids = {}
while is_anotherbidder == 'y':
    try:
        name = input("What is your name?:  ")
        bid = int(input("What is your bid?:  "))
        user_bids[name] = bid
    except ValueError:
        print('The bid must be a number..')
    is_anotherbidder = input("Would you like to add another bidder? (y/n): ")

if user_bids:
    best = next(iter(user_bids))
    for i in user_bids:
        if user_bids[i] > user_bids[best]:
            best = i

    print(f'The winner is {best} with a bid of {user_bids[best]}.')


