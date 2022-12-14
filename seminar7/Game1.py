


field = list(range(1, 10))

def show_field(field):
    print("-" * 13)
    for i in range(3):
        print("|", field[0+i*3], "|", field[1+i*3], "|", field[2+i*3], "|")
        print("-" * 13)

def player_choce(symbol):
    print('Крестик или нолик можно поставить на незанятые позиции от 1 до 9')
    print()
    player = int(input(f'Куда поставишь {symbol}? Введи число: '))
    if player >= 1 and player <= 9:
        if (str(field[player-1]) not in "XO"):
            field[player-1] = symbol
        else:
            print('Эта клетка занята! Выбери другую')
    else:
        print('Вам необходимо ввести число от 1 до 9!')

def check_winer(field):
    win = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
            (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for i in win:
        if field[i[0]] == field[i[1]] == field[i[2]]:
            return field[i[0]]


def run_game():
    count = 0
    while True:
        show_field(field)
        if count % 2 == 0:
            player_choce('X')
        else:
            player_choce('O')
        count += 1
        if count > 4:
            win = check_winer(field)
            if win == 'O' or win == 'X':
                print(f'Победили {win}-ки')
                return (f'Победили {win}-ки')
                break

        if count == 9:
            print('Ничья')
            break
        
