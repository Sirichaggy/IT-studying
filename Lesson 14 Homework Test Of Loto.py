import random
import unittest


def get_card():
    card = [[], [], []]
    g = False
    while not g:
        for i in range(5):
            i = random.randint(1, 91)
            card[0].append(i)
            if card[0].count(i) >= 2:
                None
            else:
                g = True
    b = False
    while not b:
        for i in range(5):
            i = random.randint(1, 91)
            card[1].append(i)
            if card[1].count(i) >= 2:
                None
            else:
                b = True
    t = False
    while not t:
        for i in range(5):
            i = random.randint(1, 91)
            card[2].append(i)
            if card[2].count(i) >= 2:
                None
            else:
                t = True
    card[0].sort()
    card[1].sort()
    card[2].sort()
    for y in range(4):
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


class GlobalTest(unittest.TestCase):
    def check_card_value(self):
        test_card = get_card()
        self.assertEqual(len(test_card[0]), 9, "Something went wrong")
        self.assertEqual(len(test_card[1]), 9, "Something went wrong")
        self.assertEqual(len(test_card[2]), 9, "Something went wrong")

    def checking_victory_test(self):
        card_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        test_1 = check_victory(card_1)
        self.assertFalse(test_1), "This function is a dumpster fire (it's not False when it should be)"
        card_2 = [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]
        test_2 = check_victory(card_2)
        self.assertFalse(test_2), "This function is a dumpster fire (it's not True when it should be)"

    def rerolling_test(self):
        test_bbl = reroll_bag()
        self.assertIsInstance(test_bbl, int), "Idn what the hell just happened, but you managed to catch a mistake here"


if __name__ == '__main__':
    unittest.main()

play_loto()