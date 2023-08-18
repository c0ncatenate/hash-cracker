import hashlib
import itertools
import sys
import threading
import time
from datetime import datetime
from timeit import default_timer
from colorama import Fore, Back


class Style:
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


done = False


def cracked(don):  # Cadenza
    don = True
    print(Fore.LIGHTWHITE_EX + '\r> ' + Style.BOLD + Fore.LIGHTMAGENTA_EX + '--Decryption complete!--' +
          Fore.RESET + Style.END)
    return don


def print_end(crack, time1):  # Coda
    time2 = default_timer()
    print(Fore.LIGHTGREEN_EX + "\nINPUT".ljust(11, ' ') + Fore.LIGHTWHITE_EX + ': ' + Fore.LIGHTYELLOW_EX + Back.BLACK + sha256hash + Fore.RESET + Back.RESET)
    if crack:
        print(Fore.LIGHTRED_EX + "STATUS".ljust(10, ' ') + Fore.LIGHTWHITE_EX + ': ' + Fore.LIGHTRED_EX + Back.BLACK + "CRACK SUCCESS" + Back.RESET)
        print(Fore.LIGHTBLUE_EX + "VERDICT".ljust(10, ' ') + Fore.LIGHTWHITE_EX + ': ' + Back.RED + Fore.LIGHTWHITE_EX + str(f"'{guess.decode('UTF-8')}' is your password.  Try something stronger!") + Back.RESET)
    else:
        print(Fore.LIGHTRED_EX + "STATUS".ljust(10, ' ') + Fore.LIGHTWHITE_EX + ': ' + Fore.LIGHTGREEN_EX + Back.BLACK + "CRACK FAIL" + Back.RESET)
        print(Fore.LIGHTBLUE_EX + "VERDICT".ljust(10, ' ') + Fore.LIGHTWHITE_EX + ': ' + Back.GREEN + Fore.LIGHTWHITE_EX + "I couldn't crack your hash, you have a strong password!" + Back.RESET)
    print(Fore.WHITE + "\nDecryption runtime: " + str(f"{time2 - time1:5.3f}s") + Fore.RESET)


# Headers
print(Fore.LIGHTGREEN_EX + '░░░██╗░██╗' + Fore.LIGHTRED_EX + '  ░██╗░░██╗░█████╗░░██████╗██╗░░██╗' + Fore.LIGHTBLUE_EX + '  ░█████╗░██████╗░░█████╗░░█████╗░██╗░░██╗███████╗██████╗░')
print(Fore.LIGHTGREEN_EX + '██████████╗' + Fore.LIGHTRED_EX + '  ██║░░██║██╔══██╗██╔════╝██║░░██║' + Fore.LIGHTBLUE_EX + '  ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗')
print(Fore.LIGHTGREEN_EX + '╚═██╔═██╔═╝' + Fore.LIGHTRED_EX + '  ███████║███████║╚█████╗░███████║' + Fore.LIGHTBLUE_EX + '  ██║░░╚═╝██████╔╝███████║██║░░╚═╝█████═╝░█████╗░░██████╔╝')
print(Fore.LIGHTGREEN_EX + '██████████╗' + Fore.LIGHTRED_EX + '  ██╔══██║██╔══██║░╚═══██╗██╔══██║' + Fore.LIGHTBLUE_EX + '  ██║░░██╗██╔══██╗██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗')
print(Fore.LIGHTGREEN_EX + '╚██╔═██╔══╝' + Fore.LIGHTRED_EX + '  ██║░░██║██║░░██║██████╔╝██║░░██║' + Fore.LIGHTBLUE_EX + '  ╚█████╔╝██║░░██║██║░░██║╚█████╔╝██║░╚██╗███████╗██║░░██║')
print(Fore.LIGHTGREEN_EX + '░╚═╝░╚═╝░░░' + Fore.LIGHTRED_EX + '  ╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝' + Fore.LIGHTBLUE_EX + '  ░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝' + Fore.RESET + '\n')
print(Fore.GREEN + 'SHA256'.rjust(45, ' ') + Fore.RED + ' Hash' + Fore.BLUE + ' Cracker\n' + Fore.MAGENTA + 'Written by: c0ncatenate'.rjust(60, ' ') + Fore.RESET)
print(Fore.WHITE + 'For the purposes of decrypting encrypted text, via Secure Hash Algorithm 256'.rjust(88, '_').ljust(99, '_') + Fore.RESET)
print('')

# Get a hash input from the user
sha256hash = input(Fore.LIGHTWHITE_EX + '> ' + Fore.LIGHTYELLOW_EX + "Encrypted Password: " + Fore.RESET)
print('')
current_time = datetime.now().strftime("%H:%M:%S %m/%d/%Y")
print(Fore.BLACK + Back.LIGHTWHITE_EX + "Decryption initiated @ " + current_time + Fore.RESET + Back.RESET + '\n')
time_start = default_timer()


# Animated loading
def animate():
    for c in itertools.cycle(['--', '<>', '[]', '<>']):
        if done:
            break
        sys.stdout.write(Fore.LIGHTWHITE_EX + '\r> ' + Style.BOLD + Fore.LIGHTCYAN_EX + c + 'Decrypting' + c + Fore.RESET + Style.END)
        sys.stdout.flush()
        time.sleep(0.2)


t = threading.Thread(target=animate)
t.start()

wordlist = bytes(open("milwordlist.txt").read(), encoding='utf-8')

# Hash the passwords in the wordlist
for guess in wordlist.split():
    hashed = hashlib.sha256(guess).hexdigest()

    # Compare the hashes and give an output
    if hashed == sha256hash:
        time.sleep(1)
        done = cracked(done)
        print_end(True, time_start)
        quit()

done = cracked(done)
print_end(False, time_start)
