
from random import randrange


def display_board(board):
        print("+-------" * 3, "+", sep="")
        for row in range(3):
                print("|       " * 3, "|", sep="")
                for col in range(3):
                        print("|   " + str(board[row][col]) + "   ", end="")
                print("|")
                print("|       " * 3, "|", sep="")
                print("+-------" * 3, "+", sep="")


def enter_move(board):
    ok = False  # фальшиве припущення - це нам потрібно, щоб почати цикл
    while not ok:
        move = input("Введіть свій хід: ") 
        ok = len(move) == 1 and move >= '1' and move <= '9'  # чи коректно введено користувачем дані?
        if not ok:
            print("Невдалий хід - повторіть введення даних!")  # ні, не так - введіть дані ще раз
            continue
        move = int(move) - 1  # номер клітинки від 0 до 8
        row = move // 3  # рядок клітинки
        col = move % 3  # стовпчик клітинки
        sign = board[row ][col]  # перевірка вибраного квадрата
        ok = sign not in ['O', 'X']
        if not ok:  # зайнято - знову до введення
            print("Поле вже зайнято - повторіть введення!")
            continue
    board[row][col] = 'O'  # записати 'O' у вибраний квадрат


def make_list_of_free_fields(board):
    free = []  # список спочатку пустий
    for row in range(3):  # перебираємо рядки
        for col in range(3):  # перебираємо стовпчики
            if board[row][col] not in ['O', 'X']:  # чи вільна клітинка?
                free.append((row, col))  # так, це додає новий кортеж до списку
    return free


def victory_for(board, sgn):
    if sgn == "X":  # ми шукаємо Х?
        who = 'me'  # так - це бік комп'ютера
    elif sgn == "O":  # ... чи це O?
        who = 'you'  # так - це наш бік
    else:
        who = None  # ми не повинні попасти сюди!
    cross1 = cross2 = True  # для діагоналей
    for rc in range(3):
        if board[rc][0] == sgn and board[rc][1] == sgn and board[rc][2] == sgn:  # перевірка рядка rc
            return who
        if board[0][rc] == sgn and board[1][rc] == sgn and board[2][rc] == sgn:  # перевірка стовпця rc
            return who
        if board[rc ][rc] != sgn:  # перевірка 1-ої діагоналі
            cross1 = False
        if board[2 - rc][2 - rc] != sgn:  # перевірка 2-ої діагоналі
            cross2 = False
    if cross1 or cross2:
        return who
    return None


def draw_move(board):
    free = make_list_of_free_fields(board)  # створюємо список вільних клітинок
    cnt = len(free)
    if cnt > 0:  # якщо список не порожній, вибераємо місце для 'X' і впишемо його
        this = randrange(cnt)
        row, col = free[this]
        board[row][col] = 'X'


board = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ]  # очистити дошку
board[1][1] = 'X'  # спочатку вписуємо 'X' посередині
free = make_list_of_free_fields(board)
human_turn = True  # чія черга ходити?
while len(free):
    display_board(board)
    if human_turn:
        enter_move(board)
        victor = victory_for(board, 'O')
    else:
        draw_move(board)
        victor = victory_for(board, 'X')
    if victor != None:
        break
    human_turn = not human_turn
    free = make_list_of_free_fields(board)

display_board(board)
if victor == 'you':
    print("Ви виграли!")
elif victor == 'me':
    print("Я виграв")
else:
    print("Нічия́!")
