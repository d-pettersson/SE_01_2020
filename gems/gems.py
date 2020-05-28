def get_input():
    a, b = map(int, input('Please input the first gem\nand its replacement(separated by a whitespace): ').strip().split())
    return a, b

def move_is_valid(a, b):
    return 0 if abs(a - b) > 3 else abs(a - b) % 2

def print_welcome_message():
    msg = 'Welcome to the sparkling diamonds game.\nThe game\'s layout is:\n1 2 3\n4 5 6\n7 8 9\n\nThis is your board:\n'
    print(msg)

def print_board(board):
    for i in range(len(board)//3):
        print('{} {} {}'.format(board[i], board[i+1], board[i+2]))

def main():
    initial_board = [1, 2, 3, 4, 4, 5, 5, 3, 4]
    print_welcome_message()
    print_board(initial_board)
    a, b = get_input()
    if move_is_valid(a, b):
        print('valid move')
    else:
        print('invalid move')

if __name__ == '__main__':
    main()
