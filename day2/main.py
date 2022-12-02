import typing

def get_move(input: str):
    if input == "A" or input == "X":
        return "rock"
    elif input == "B" or input == "Y":
        return "paper"
    elif input == "C" or input == "Z":
        return "scissors"
    else:
        return None

def should_win_or_lose(move_key, opponent_move):
    if move_key == "X":
        # lose
        if opponent_move == "rock":
            player_move = "scissors"
        elif opponent_move == "paper":
            player_move = "rock"
        elif opponent_move == "scissors":
            player_move = "paper"
        
    elif move_key == "Y":
        # draw
        if opponent_move == "rock":
            player_move = "rock"
        elif opponent_move == "paper":
            player_move = "paper"
        elif opponent_move == "scissors":
            player_move = "scissors"

    elif move_key == "Z":
        # win
        if opponent_move == "rock":
            player_move = "paper"
        elif opponent_move == "paper":
            player_move = "scissors"
        elif opponent_move == "scissors":
            player_move = "rock"
            
    return check_winner(opponent=opponent_move, player=player_move)

def check_winner(opponent:str, player:str):
    score = 0
    win_bonus = 6
    draw_bonus = 3
    loss_penalty = 0

    if player == 'rock':
        score += 1
    if player == 'paper':
        score += 2
    if player == 'scissors':
        score += 3

    if opponent == player:
        return score + draw_bonus

    elif opponent == "rock":
        if player == "paper":
            return score + win_bonus
        else:
            return score - loss_penalty

    elif opponent == "paper":
        if player == "scissors":
            return score + win_bonus
        else:
            return score - loss_penalty

    elif opponent == "scissors":
        if player == "rock":
            return score + win_bonus
        else:
            return score - loss_penalty

def solution1(input: typing.List[str]):
    score = 0

    for line in input:
        shapes = line.split(" ")
        if len(shapes) >= 2 :
            opponent = get_move(shapes[0])
            player = get_move(shapes[1])
            score += check_winner(opponent, player)

    return score

def solution2(input: typing.List[str]):
    score = 0

    for line in input:
        split_line = line.split(" ")
        if len(split_line) >= 2 :
            opponent = get_move(split_line[0])
            move = split_line[1]
            score += should_win_or_lose(move, opponent)

    return score

if __name__ == "__main__":
    input = open("day2/input.txt", "r").read().split('\n')

    print(f'Total score: {solution1(input)}')
    print(f'Total score: {solution2(input)}')