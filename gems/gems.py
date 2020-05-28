def get_input():
    a, b = map(int, input('Please input the first gem\nand its replacement(separated by a whitespace): ').strip().split())
    return a-1, b-1

def move_is_valid(a, b):
    return 0 if abs(a - b) > 3 else abs(a - b) % 2

def switch_pos(board, old_pos, new_pos):
    if move_is_valid(old_pos, new_pos):
        temp = board[new_pos]
        board[new_pos] = board[old_pos]
        board[old_pos] = temp
        print('this is your new board:')
        print_board(board)

def is_line(board):
    if board[0] == board[1] == board[2]:
        print('we have a winner')
    elif board[3] == board[4] == board[5]:
        print('we have a winner')
    elif board[7] == board[8] == board[9]:
        print('we have a winner')

    elif board[0] == board[3] == board[6]:
        print('we have a winner')
    elif board[1] == board[4] == board[7]:
        print('we have a winner')
    elif board[2] == board[5] == board[8]:
        print('we have a winner')

    else:
        print('try again')

def print_welcome_message():
    msg = 'Welcome to the sparkling diamonds game.\nThe game\'s layout is:\n1 2 3\n4 5 6\n7 8 9\n\nThis is your board:'
    print(msg)

def print_board(board):
        print(board[0], board[1], board[2])
        print(board[3], board[4], board[5])
        print(board[6], board[7], board[8])

    # weird bug on my python cmd - this prints 'i' instead of board[i]
    # for i in range(len(board)//3):
    #     print('{} {} {}'.format(board[i], board[i+1], board[i+2]))

def main():
    initial_board = [1, 2, 3, 4, 4, 5, 5, 3, 4]
    print_welcome_message()
    print_board(initial_board)
    a, b = get_input()
    switch_pos(initial_board, a, b)
    is_line(initial_board)

if __name__ == '__main__':
    main()
