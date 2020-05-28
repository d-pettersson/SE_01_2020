def get_input():
    a, b = map(int, input('Please input the first gem\nand its replacement(separated by a whitespace): ').strip().split())
    if not check_input(a, b):
        print('invalid move')
    else:
        print('valid move')

def check_input(a, b):
    return 0 if abs(a - b) > 3 else abs(a - b) % 2

def print_welcome_message():
    msg = 'Welcome to the sparkling diamonds game.\nThe game\'s layout is:\n1 2 3\n4 5 6\n7 8 9\n\nThis is your board:'
    print(msg)

def print_board(board):
    for i in range(len(board)//3):
        print('{} {} {}'.format(board[i], board[i+1], board[i+2]))

def main():
    initial_board = [1, 2, 3, 4, 4, 5, 5, 3, 4]
    print_welcome_message()
    print_board(initial_board)
    get_input()

if __name__ == '__main__':
    main()
