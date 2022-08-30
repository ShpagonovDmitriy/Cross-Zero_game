import random


def display_board(board):
    """Игровое поле и строка очистки экрана перед тем,
    как выводится новое игровое поле с новыми значениями"""
    print('\n'*20)
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('--|---|--')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('--|---|--')
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])


def player_input():
    """На выходе получаем кортеж из двух элементов Х и О
    с присвоением значения каждому игроку"""
    marker = ''
    while not (marker == 'X' or marker == 'O'):
        marker = input('Введите каким символом хотите играть (Х или О): ').upper()
    player1=marker
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    return (player1, player2)


def place_marker(board,marker,position):
    board[position]=marker

def win_check(board,mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or
        (board[4] == mark and board[5] == mark and board[6] == mark) or
        (board[7] == mark and board[8] == mark and board[9] == mark) or
        (board[1] == mark and board[5] == mark and board[9] == mark) or
        (board[7] == mark and board[5] == mark and board[3] == mark) or
        (board[1] == mark and board[4] == mark and board[7] == mark) or
        (board[2] == mark and board[5] == mark and board[8] == mark) or
        (board[3] == mark and board[6] == mark and board[9] == mark))

def choose_first():
    flip = random.randint(0,1)
    if flip == 0:
        return 'Игрок 1'
    else:
        return 'Игрок 2'

def space_check(board,positions):
    return board[positions] == ' '

def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True

def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int(input('Укажите поле для ввода (1-9): '))

    return position

def replay():
    choice = input('Хотите играть снова? Введите YES или NO ').upper()
    return choice == 'YES'

print('Добро пожаловать в игру "Крестики-Нолики"')

while True:
    the_board=[' ']*10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' ходит первым')
    play_game = input('Вы готовы играть? Yes или No ').upper()
    if play_game == 'YES':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Игрок 1':
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player1_marker,position)
            if win_check(the_board,player1_marker):
                display_board(the_board)
                print('Игрок 1 выиграл')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Ничья!')
                    game_on = False
                else:
                    turn = 'Игрок 2'
        else:
            display_board(the_board)
            position = player_choice(the_board)
            place_marker(the_board, player2_marker, position)
            if win_check(the_board, player2_marker):
                display_board(the_board)
                print('Игрок 2 выиграл')
                game_on = False
            else:
                if full_board_check(the_board):
                    display_board(the_board)
                    print('Ничья!')
                    game_on = False
                else:
                    turn = 'Игрок 1'

    if not replay():
        print('До свидания!')
        break