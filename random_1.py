import random
import time

# this part allow us to input the name by yourself. turn off the comment and comment the list down below.

# n = int(input("How many people will present? "))
# names = []

# for i in range(n):
#     name = input(f"{i+1}° person: ")
#     names.append(name) #aaaaaaaaaaaaaadd to name list (NOW I GOT IT)

names = ["Keven", "Murilo", "Leticia", "Hitalo"]

random.shuffle(names)

print("order of presentation")
for i, name in enumerate(names, start=1):
    print(f"{i}° {name}")
    time.sleep(2)

trollface = """
⠀⠀⠀⠀⠀⣀⡴⠖⠒⠒⢒⣒⡖⠒⠒⠒⠒⠒⠒⠶⠶⠤⣤⣀⣀
⠀⠀⠀⠀⣴⠋⠀⠀⠤⣪⣝⡲⠯⠭⠥⠀⠀⠀⠀⠀⣀⣐⣒⡒⠉⠙⢦⡀⠀⠀
⠀⠀⠀⣼⠃⠀⠈⠰⠫⠋⣀⣀⣀⣀⠀⠃⠀⠀⠀⠸⠀⠀⠀⠈⠆⠀⠀⢧⠀⠀
⠀⣠⡾⠁⠀⡀⠠⠄⢰⣿⠿⠿⢯⣍⣙⣶⠀⠀⢀⣠⣶⣾⣿⠶⠆⠤⠤⢜⢷⡄
⡾⢻⢡⡞⠋⣽⠛⠲⠤⡤⠴⠋⠀⠀⠉⠁⠀⠀⠈⣿⠁⠀⢀⣀⣠⠶⠶⣽⣵⣿
⣇⢠⢸⡥⠶⣟⠛⠶⣤⣀⠀⠀⠀⢲⡖⣂⣀⠀⠀⠈⢳⣦⡀⠉⠉⣽⡄⠰⣻⣿
⠙⣮⡪⠁⠀⠻⣶⣄⣸⣍⠙⠓⠶⣤⣥⣉⣉⠀⠠⠴⠋⠁⣈⣥⣴⣿⡇⠈⣽⠃
⠀⠈⢻⡄⠀⠀⠙⣆⢹⡟⠷⣶⣤⣇⣀⠉⠙⡏⠉⢻⡟⢉⣹⣅⣼⣿⡇⠀⡏⠀
⠀⠀⠀⠻⣄⠀⠀⠈⠻⢦⡀⠀⣽⠉⠛⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⡇⠀
⠀⠀⠀⠀⠙⢦⣀⠄⡀⢄⡙⠻⠧⣤⣀⣀⣿⠀⠀⣿⢀⣼⣃⣾⣼⠟⠁⠀⡇⠀
⠀⠀⠀⠀⠀⠀⠉⠓⢮⣅⡚⠵⣒⡤⢄⣉⠉⠉⠉⠉⠉⠉⠉⢀⡠⠀⠀⠀⣷⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠳⢦⣄⡉⠙⠛⠃⠀⠀⠀⠀⠉⠁⠀⠀⠀⠀⡿⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠲⠶⢤⣤⣀⣀⣀⣀⣀⣀⡤⠞⠁⠀
"""

lines = trollface.split('\n')

for line in lines:
    print("\033[31m" + line + "\033[0m")
    time.sleep(0.05)