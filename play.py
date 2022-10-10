import emoji
play_board = list(range(1, 10))
print(emoji.emojize(':sparkles:ДОБРО ПОЖАЛОВАТЬ В ИГРУ КРЕСТИКИ-НОЛИКИ:sparkles:'))
def draw_board(board):
    print('-------------')
    for i in range(3):
        print(f"'|'{board[0+i*3]}'|'{board[1+i*3]}'|'{board[2+i*3]}'|'")
        
def take_input(player_token):
    flag = False
    while not flag:
        player_answer = int(input(f'Куда поставим {player_token}? '))
        if (player_answer >= 1) and (player_answer <= 9):
            if (str(play_board[player_answer-1]) not in "XO"):
                play_board[player_answer-1] = player_token
                flag = True
            else:
                print(emoji.emojize(':cross_mark: Эта клетка уже занята.'))
        else:
            print('Некорректный ввод. Введите число от 1 до 9: ')

def check_win(board):
    win_end = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for i in win_end:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            return board[i[0]]
    return False

def play(board):
    counter = 0
    win = False
    while not win:
        draw_board(board)
        if counter % 2 == 0:
            take_input('X')
        else:
            take_input('O')
        counter += 1
        if counter > 4:
            end = check_win(board)
            if end:
                print(emoji.emojize((f':trophy: {end} ПОБЕДА!')))
                win = True
                break
        if counter == 9:
            print(emoji.emojize((':handshake: Ничья')))
            break
    draw_board(board)

playing = play(play_board)