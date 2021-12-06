import pyautogui, time, os, sys
from colorama import Fore

clear = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')
clear()
while True:
    try: 
        messages = int(input(f'                                            {Fore.LIGHTRED_EX}Enter the amount of messages to send: '))
        break
    except:
        print(f'{Fore.RED}                                                      Only numbers can be used.')
        time.sleep(1)
        clear()

message_content = input('                                                       Message to send: ')

VERSION = "0.1"
AUTHOR = "YeetDisDude#0001"

def banner():
    sys.stdout.buffer.write(f'''\
{Fore.LIGHTRED_EX}
                             ██████╗██████╗  █████╗ ███╗   ███╗███╗   ███╗███████╗██████╗ 
                            ██╔════╝██╔══██╗██╔══██╗████╗ ████║████╗ ████║██╔════╝██╔══██╗
                            ╚█████╗ ██████╔╝███████║██╔████╔██║██╔████╔██║█████╗  ██████╔╝  Version: {VERSION}
                             ╚═══██╗██╔═══╝ ██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══╝  ██╔══██╗  Made by: {AUTHOR}
                            ██████╔╝██║     ██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║███████╗██║  ██║
                            ╚═════╝ ╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝    
'''.encode('utf8'))

clear()
banner()

print("                 Go to somewhere that you can spam, you have 10 seconds. (something like a text box)")

for i in range(10,0,-1):
    time.sleep(1)
    print(f'                                                     {i}')
time.sleep(1)
print(f'                                              {Fore.RED}Starting to spam "{message_content}" {messages} times.')

for num in range(messages):
    pyautogui.write(message_content)
    pyautogui.press('enter')
clear()
banner()

print(f'{Fore.LIGHTGREEN_EX}                                         Successfully spammed "{message_content}" {messages} time(s)')
time.sleep(1)
print("Exiting...")
time.sleep(5)