from multiprocessing import Event
import threading
import time
import random
book = []
event = Event()

def book_writing(number, interval):
    global book
    event.set()
    while True:
        time.sleep(interval)
        chapter = "Chapter has done by writer {}".format(number)
        print(chapter)
        book.append(chapter)

def fan_base(number, interval):
    while True:
        event.wait()
        l = random.randint(1, 4)
        if l == 1:
            time.sleep(interval)
            print("Nah, I thought chapter {} would be way better - says fan {}".format(len(book), number))
        elif l == 2:
            time.sleep(interval)
            print("Wow, chapter {} is really impressive, just banger ngl - says fan {}".format(len(book), number))
        elif l == 3:
            time.sleep(interval)
            print("Total dumpster fire, who even wrote this? - says fan {}".format(len(book), number))
        elif l == 4:
            time.sleep(interval)
            print("Well, I can't say for sure about chapter {}, but will read all next chapters anyway - says fan {}".format(len(book), number))


w1 = threading.Thread(target=book_writing, args=(1, 2))
w2 = threading.Thread(target=book_writing, args=(2, 3))
fan1 = threading.Thread(target=fan_base, args=(1, 4))
fan2 = threading.Thread(target=fan_base, args=(2, 5))
fan3 = threading.Thread(target=fan_base, args=(3, 6))
fan4 = threading.Thread(target=fan_base, args=(4, 7))
w1.start()
w2.start()
fan1.start()
fan2.start()
fan3.start()
fan4.start()
