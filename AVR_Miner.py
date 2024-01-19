import Setup as SU
import random
import colorama
import time
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

# COIN = 0

liczba1 = 1
czas = 0
COINM = 0

x = 1
y = 0


print(Fore.GREEN + f"Aktualna ilość MarchwCoinów na koncie: " + Fore.RED + f"{SU.COIN}")
print(Fore.GREEN + f"Dziekujemy za skorzystanie z naszych usług\n")
print(Fore.BLUE + "Developer: " + Fore.RED + "Marchewka10")


print("\n\nInstrukcja:")
print(Fore.WHITE + Back.RED + "R5" + Fore.RESET + Back.RESET + " Znaleziono block")
print(Fore.WHITE + Back.MAGENTA + "C7" + Fore.RESET + Back.RESET + " Nie naleziono blocku")
print(Fore.WHITE + Back.GREEN + "S1" + Fore.RESET + Back.RESET + " Podsumowanie")
time.sleep(3)
print("\n\n")

while True:
    for i in range(0, 60):
        for i in range(0, 333):
            if x == y:
                COINM += 1
                time.sleep(0.04)
                KONIEC = COINM + SU.COIN
                file = open("Setup.py", "w")
                file.write(f"COIN = {KONIEC}")
                file.flush()

                a2 = Fore.WHITE + time.ctime(second_since_epoch) + " "
                b2 = Fore.WHITE + Back.RED + "R5"
                c2 = Fore.WHITE + Back.RESET + f" {liczba1}/{liczba1} "
                d2 = Fore.GREEN + str(random.randint(300, 400)) + "KH/s "
                exit2 = a2 + b2 + c2 + d2
                print(exit2)
                x = (random.randint(1, 10))
                y = (random.randint(1, 10))

        x = (random.randint(0, 10))
        y = (random.randint(0, 10))
        second_since_epoch = time.time()
        a = Fore.WHITE + time.ctime(second_since_epoch) + " "
        b = Fore.WHITE + Back.MAGENTA + "C7"
        c = Fore.WHITE + Back.RESET + f" {liczba1}/{liczba1} "
        d = Fore.GREEN + str(random.randint(300, 400)) + "H/s "
        exit = a + b + c + d
        liczba1+=1
        print(exit)
        time.sleep(1)

    KONIEC = COINM + SU.COIN

    czas+=1
    b1 = Fore.WHITE + Back.GREEN + "S1" + Fore.RESET + Back.RESET
    a1 = Fore.WHITE + time.ctime(second_since_epoch) + " " + b1
    c1 = f"         | Koparka działa przez {czas} minut"
    d1 = f"         | Rozwiązała 19980 hasów"
    e1 = f"         | Ilosć MarchwCoinów: {KONIEC}"
    print(a1)
    print(c1)
    print(d1)
    print(e1)
    time.sleep(1.5)

    file = open("Setup.py", "w")
    file.write(f"COIN = {KONIEC}")
    file.flush()