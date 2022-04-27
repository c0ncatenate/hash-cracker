import hashlib
import itertools
import threading
import time
from datetime import datetime
import sys
from colorama import Fore, Back


class style:
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


done = False

# Headers

print(Fore.RED + '░░░██╗░██╗  ░██╗░░██╗░█████╗░░██████╗██╗░░██╗' + Fore.BLUE + '  ░█████╗░██████╗░░█████╗░░█████╗░██╗░░██╗███████╗██████╗░')
print(Fore.RED + '██████████╗  ██║░░██║██╔══██╗██╔════╝██║░░██║' + Fore.BLUE + '  ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║░██╔╝██╔════╝██╔══██╗')
print(Fore.RED + '╚═██╔═██╔═╝  ███████║███████║╚█████╗░███████║' + Fore.BLUE + '  ██║░░╚═╝██████╔╝███████║██║░░╚═╝█████═╝░█████╗░░██████╔╝')
print(Fore.RED + '██████████╗  ██╔══██║██╔══██║░╚═══██╗██╔══██║' + Fore.BLUE + '  ██║░░██╗██╔══██╗██╔══██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗')
print(Fore.RED + '╚██╔═██╔══╝  ██║░░██║██║░░██║██████╔╝██║░░██║' + Fore.BLUE + '  ╚█████╔╝██║░░██║██║░░██║╚█████╔╝██║░╚██╗███████╗██║░░██║')
print(Fore.RED + '░╚═╝░╚═╝░░░  ╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░╚═╝░░╚═╝' + Fore.BLUE + '  ░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝' + Fore.RESET)
print('')
print(Fore.RED + '                                          SHA256 Hash' + Fore.MAGENTA + ' Cracker Written ' + Fore.BLUE + 'by' + ' concatenate' + Fore.RESET)
print('')

# Get a hash input from the user
sha256hash = input(Fore.LIGHTWHITE_EX + "[i] " + Fore.LIGHTBLUE_EX + "Put in your password hash here\n  > " + Fore.RESET)
print('')
current_time = datetime.now().strftime("%H:%M:%S")
print(Fore.LIGHTWHITE_EX + "[i] " + Fore.LIGHTMAGENTA_EX + "Cracking started: " + Fore.LIGHTWHITE_EX + current_time + '\n' + Fore.RESET)


# here is the animation
def animate():
    for c in itertools.cycle(['...', '..', '.']):
        if done:
            break
        sys.stdout.write(style.BOLD + Fore.LIGHTRED_EX + '\rCracking' + c + Fore.RESET + style.END)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\r')


t = threading.Thread(target=animate)
t.start()

wordlist = bytes(open("10-million-password-list-top-1000000.txt").read(), encoding='utf-8')

# Hash the passwords in the wordlist
for guess in wordlist.split():
    hashed = hashlib.sha256(guess).hexdigest()

    # Compare the hashes and give an output
    if hashed == sha256hash:
        time.sleep(1)
        done = True
        print(Fore.LIGHTWHITE_EX + "\n\nYour hash   :", Fore.LIGHTYELLOW_EX + sha256hash + Fore.RESET)
        print(Fore.LIGHTWHITE_EX + "STATUS      : " + Fore.LIGHTGREEN_EX + "CRACKED")
        print(Fore.LIGHTWHITE_EX + "GUESS       : " + Back.GREEN + Fore.LIGHTWHITE_EX + guess.decode(
            'UTF-8') + Back.RESET)
        print(Fore.LIGHTMAGENTA_EX + "\nCracking ended: " + Fore.LIGHTWHITE_EX + current_time + Fore.RESET)
        quit()

    # Output if the hashes don't match
    elif hashed != sha256hash:
        pass
done = True
print(Fore.LIGHTWHITE_EX + "\n\nYour hash   :", Fore.MAGENTA + sha256hash + Fore.RESET)
print(Fore.LIGHTWHITE_EX + "STATUS      : " + Fore.LIGHTRED_EX + "UNCRACKED")
print(
    Fore.LIGHTWHITE_EX + "GUESS       : " + Back.RED + Fore.LIGHTWHITE_EX + "I couldn't crack your hash, you have a strong password! :)" + Back.RESET)
print(Fore.LIGHTMAGENTA_EX + "\nCracking ended: " + Fore.LIGHTWHITE_EX + current_time + Fore.RESET)
