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

# Define the footer text
footer_text = "Made by R4t_D3v"

# Function to center text
def center_text(text):
    lines = text.splitlines()
    centered_lines = [line.center(os.get_terminal_size().columns) for line in lines]
    return '\n'.join(centered_lines)

# Function to clear the console
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function to print the full menu with footer
def print_menu():
    clear_console()
    print(Fore.CYAN + center_text(ascii_art))
    print(Style.RESET_ALL + center_text(menu_text))
    print(center_text(footer_text))

# Function to handle user input
def handle_input():
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            roblox_script = 'loadstring(game:HttpGet("https://raw.githubusercontent.com/LittleThingsMods/Dorzo-Hub/main/Main%20Script"))()'
            pyperclip.copy(roblox_script)
            clear_console()
            print("Roblox script copied to clipboard.")
        elif choice == "2":
            webbrowser.open("https://discord.gg/tCxppmmgcv")
            clear_console()
            print("Discord server link opened.")
        elif choice == "3":
            webbrowser.open("https://t.me/DorzoHubRoblox")
            clear_console()
            print("Telegram link opened.")
        else:
            clear_console()
            print("Invalid choice, please try again.")

        input("Press Enter to return to the menu...")

        print_menu()  # Print the menu again after user input

# Run the input handler
handle_input()
