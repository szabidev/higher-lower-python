import random
from logo import logo, vs, win, lose
from game_data import data

# Shuffle data each time the game starts
random.shuffle(data)
print(logo)
correct = True
player_decision = 0
cpu_decision = 0

while correct:
# Iterate over the data list
    for index in range((len(data) - 1)):
        correct_answer = data[index]
        print(f"Compare A: {correct_answer['name']}, a {correct_answer['description']}, from {correct_answer['country']}")
        print(vs)
        print(f"Against B: {data[index + 1]['name']}, a {data[index + 1]['description']}, from {data[index + 1]['country']}")
        answer = input(f"Who has more followers? Type 'A' or 'B'\n").lower()

        # Check if the player's answer is correct
        if answer == 'a':
            player_decision = data[index]['follower_count']
            cpu_decision = data[index + 1]['follower_count']
            correct_answer = data[index]
        if answer == 'b':
            player_decision = data[index + 1]['follower_count']
            cpu_decision = data[index]['follower_count']
            correct_answer = data[index + 1]
        if answer not in ['a', 'b']:
            print('Invalid input please try again')


        # print(player_decision, 'Player decision')
        # print(cpu_decision, 'CPU decision')

        if player_decision < cpu_decision:
            print(lose)
            print(f"Your score is {index}")
            correct = False
            # break the loop if the player's answer is incorrect
            break

# If all answers are correct, player has won the game
if correct:
    print(win)
    print('You have won the game')