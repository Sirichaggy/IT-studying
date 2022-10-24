#!/usr/bin/python3
#== Лото ==
#Правила игры в лото.
#Игра ведется с помощью специальных карточек, на которых отмечены числа, 
#и фишек (бочонков) с цифрами.
#Количество бочонков — 90 штук (с цифрами от 1 до 90).
#Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
#расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
#--------------------------
#    9 43 62          74 90
# 2    27    75 78    82
#   41 56 63     76      86
#--------------------------
#В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
#случайная карточка. 
#Каждый ход выбирается один случайный бочонок и выводится на экран.
#Также выводятся карточка игрока и карточка компьютера.
#Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
#Если игрок выбрал "зачеркнуть":
#	Если цифра есть на карточке - она зачеркивается и игра продолжается.
#	Если цифры на карточке нет - игрок проигрывает и игра завершается.
#Если игрок выбрал "продолжить":
#	Если цифра есть на карточке - игрок проигрывает и игра завершается.
#	Если цифры на карточке нет - игра продолжается.
#Побеждает тот, кто первый закроет все числа на своей карточке.
#Пример одного хода:
#Новый бочонок: 70 (осталось 76)
#------ Ваша карточка -----
# 6  7          49    57 58
#   14 26     -    78    85
#23 33    38    48    71   
#--------------------------
#-- Карточка компьютера ---
# 7 11     - 14    87      
#      16 49    55 77    88    
#   15 20     -       76  -
#--------------------------
#Зачеркнуть цифру? (y/n)
#Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
#с помощью функции-генератора.

import random
def get_card():
    card = [[],[],[]]
    G = False
    while not G:
        for i in range(5):
            i = random.randint(1, 91)
            card[0].append(i)
            if card[0].count(i) >= 2:
                None
            else:
                G = True
    B = False
    while not B:
        for i in range(5):
            i = random.randint(1, 91)
            card[1].append(i)
            if card[1].count(i) >= 2:
                None
            else:
                B = True
    T = False
    while not T:
        for i in range(5):
            i = random.randint(1, 91)
            card[2].append(i)
            if card[2].count(i) >= 2:
                None
            else:
                T = True
    card[0].sort()
    card[1].sort()
    card[2].sort()
    for b in range(4):
        card[0].insert(random.randint(0, 6), "-")
        card[1].insert(random.randint(0, 6), "-")
        card[2].insert(random.randint(0, 6), "-")
    return card

def check_victory(x):
    for i in x[0].copy():
        if i == '-':
            x[0].remove(i)
    if len(x[0]) == 0:
        for i in x[1].copy():
            if i == '-':
                x[1].remove(i)
        if len(x[1]) == 0:
            for i in x[2].copy():
                if i == '-':
                    x[2].remove(i)
            if len(x[2]) == 0:
                return True
            else: 
                return False
        else:
            return False
    else: 
        return False

def play_loto():
    player = get_card()
    computer = get_card()
    def c1():
        print("Ваша карточка: {}".format(player))
    def c2():
        print("Карточка противника: {}".format(computer))
    c1()
    c2()
    used_bbl = []
    def reroll_bag():
        rule = False
        while not rule:
            bbl = random.randint(1, 90)
            if bbl in used_bbl:
                None
            else:
                print("Номер боченка: {}".format(bbl))
                used_bbl.append(bbl)
                return bbl
                rule = True
    game = False
    while not game:
        L = reroll_bag()
        c1()
        turn = float(input("Ваш ход: '1' - зачеркнуть, '2' - продолжить "))
        if turn == 1:
            if L in player[0].copy():
                player[0].remove(L)
            else:
                if L in player[1].copy():
                    player[1].remove(L)
                else:
                    if L in player[2].copy():
                        player[2].remove(L)
                    else:
                        print("Game Over")
                        game = True
        elif turn == 2:
            if L in player[0].copy():
                print("Game Over")
                game = True
            else:
                if L in player[1].copy():
                    print("Game Over")
                    game = True
                else:
                    if L in player[2].copy():
                        print("Game Over")
                        game = True
                    else:
                        None
        if game == False:
            c1()
            print("Ход противника...")
            for i in computer[0].copy():
                if L in computer[0].copy():
                    computer[0].remove(L)
            for i in computer[1].copy():
                if L in computer[1].copy():
                    computer[1].remove(L)
            for i in computer[2].copy():
                if L in computer[2].copy():
                    computer[2].remove(L)
            c2()
            w1 = check_victory(player)
            if w1 == True:
                print("Ты выиграл!")
                game = True
            w2 = check_victory(computer)
            if w2 == True:
                print("ИИ одержал победу")
                game = True

play_loto()
