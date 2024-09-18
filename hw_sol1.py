import random

player1_name: str = input('Enter first player name:') # 'adam'
player2_name: str = input('Enter second player name:')
player3_name: str = input('Enter third player name:')
player4_name: str = input('Enter fourth player name:')

winner: str = random.choice([player1_name, player2_name, player3_name,player4_name])

print(f'the winner is : {winner}')
