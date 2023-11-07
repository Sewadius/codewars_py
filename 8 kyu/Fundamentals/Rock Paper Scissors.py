def rps(p1: str, p2: str) -> str:
    player_1 = 'Player 1 won!'
    player_2 = 'Player 2 won!'
    draw = 'Draw!'

    if p1 == 'scissors':
        match p2:
            case 'paper':
                return player_1
            case 'scissors':
                return draw
            case 'rock':
                return player_2
    if p1 == 'paper':
        match p2:
            case 'paper':
                return draw
            case 'scissors':
                return player_2
            case 'rock':
                return player_1
    if p1 == 'rock':
        match p2:
            case 'paper':
                return player_2
            case 'scissors':
                return player_1
            case 'rock':
                return draw


print(rps('scissors', 'paper'))     # -> 'Player 1 won!'
print(rps('scissors', 'rock'))      # -> 'Player 2 won!'
print(rps('paper', 'paper'))        # -> 'Draw!'
