import os
import pyperclip
import webbrowser
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Define the ASCII art text
ascii_art = '''
██████╗  ██████╗ ██████╗ ███████╗ ██████╗     ██╗  ██╗██╗   ██╗██████╗ 
██╔══██╗██╔═══██╗██╔══██╗╚══███╔╝██╔═══██╗    ██║  ██║██║   ██║██╔══██╗
██║  ██║██║   ██║██████╔╝  ███╔╝ ██║   ██║    ███████║██║   ██║██████╔╝
██║  ██║██║   ██║██╔══██╗ ███╔╝  ██║   ██║    ██╔══██║██║   ██║██╔══██╗
██████╔╝╚██████╔╝██║  ██║███████╗╚██████╔╝    ██║  ██║╚██████╔╝██████╔╝
╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚══════╝ ╚═════╝     ╚═╝  ╚═╝ ╚═════╝ ╚═════╝ 
'''

# Define the additional text menu
menu_text = '''
*************************
*1 - Copy roblox script *
*2 - Open discord server*
*3 - Open telegram      *
*************************
'''

# Function to center text
def center_text(text):
    lines = text.splitlines()
    centered_lines = [line.center(os.get_terminal_size().columns) for line in lines]
    return '\n'.join(centered_lines)

# Print the ASCII art in cyan and the centered text menu
print(Fore.CYAN + center_text(ascii_art))
print(Style.RESET_ALL + center_text(menu_text))

# Function to handle user input
def handle_input():
    while True:
        choice = input("Enter your choice: ")
        if choice == "1":
            roblox_script = 'loadstring(game:HttpGet("https://raw.githubusercontent.com/LittleThingsMods/Dorzo-Hub/main/Main%20Script"))()'
            pyperclip.copy(roblox_script)
            print("Roblox script copied to clipboard.")
        elif choice == "2":
            webbrowser.open("https://discord.gg/tCxppmmgcv")
            print("Discord server link opened.")
        elif choice == "3":
            webbrowser.open("https://t.me/DorzoHubRoblox")
            print("Telegram link opened.")
        else:
            print("Invalid choice, please try again.")

# Run the input handler
handle_input()
