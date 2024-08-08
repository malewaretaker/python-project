import ctypes
import subprocess
import time
import os
import random
import string
import threading
from colorama import Fore, init
import psutil

# Initialize colorama
init(autoreset=True)

# ANSI escape codes for text colors
RED = '\033[91m'
BLUE = '\033[94m'
RESET = '\033[0m'

# Windows API constants
GWL_EXSTYLE = -20
WS_EX_LAYERED = 0x00080000
LWA_ALPHA = 0x00000002

# Define a set of authorized HWIDs
AUTHORIZED_HWIDS = {
    "123456789ABCDEF0",  # Replace with actual authorized HWIDs
    "FEDCBA9876543210"
}

SPECIAL_HWID = "4C4C4544-0054-4310-8039-B4C04F584832"

def get_hwid():
    """Get the hardware ID of the machine."""
    try:
        output = subprocess.check_output('wmic csproduct get uuid').decode()
        hwid = output.split('\n')[1].strip()
        return hwid
    except Exception as e:
        print(f"{RED}Failed to retrieve HWID: {e}{RESET}")
        return None

def set_console_opacity(opacity):
    """Set console window opacity."""
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    exstyle = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
    ctypes.windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, exstyle | WS_EX_LAYERED)
    ctypes.windll.user32.SetLayeredWindowAttributes(hwnd, 0, int(255 * opacity), LWA_ALPHA)

def print_centered(text, width):
    """Print text centered in a given width."""
    padding = (width - len(text)) // 2
    print(' ' * padding + text)

def set_console_title(title):
    """Set the console window title."""
    ctypes.windll.kernel32.SetConsoleTitleW(title)

def generate_random_title(length=10):
    """Generate a random string of letters and numbers."""
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def title_updater():
    """Continuously update the console title with random strings."""
    while True:
        set_console_title(generate_random_title())
        time.sleep(0.01)  # Update every 0.01 seconds for 100x speed

def clear_console():
    """Clear the console screen."""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    # Get the width of the console
    console_width = os.get_terminal_size().columns
    
    # Text to display
    menu_title = f"{RED}Master Kodabladi's Console Menu{RESET}"
    option1 = f"{RED}Type 'inject' to Inject{RESET}"
    option2 = f"{RED}Type 'clean pc' to Clean PC{RESET}"
    option3 = f"{RED}Type 'close' to Close{RESET}"
    
    # Print centered text
    print_centered(menu_title, console_width)
    print()
    print_centered(option1, console_width)
    print_centered(option2, console_width)
    print_centered(option3, console_width)
    print()
    print_centered("Please enter a command:", console_width)

def inject():
    if not is_roblox_running():
        print_centered(f"{RED}Roblox is not open.{RESET}", os.get_terminal_size().columns)
        time.sleep(2)
        return

    file_path = r"C:\Users\lyinglol\Downloads\wind\cmake-build-release-visual-studio\wind.exe"
    
    # Print the "Injecting..." message
    print_centered(f"{RED}Injecting...{RESET}", os.get_terminal_size().columns)
    # Ensure the message is displayed for a short time
    time.sleep(1)  # Change this to control how long the message is shown
    
    # Open the file with its default application
    subprocess.Popen([file_path], shell=True)
    
    # Wait for 5 seconds to simulate the injection process
    time.sleep(2)
    
    # Print the completion message
    print_centered(f"{RED}Injection complete!{RESET}", os.get_terminal_size().columns)
    time.sleep(2)  # Give time to read the completion message
    clear_console()

def is_roblox_running():
    """Check if Roblox is running."""
    for process in psutil.process_iter(['name']):
        if process.info['name'] == "RobloxPlayerBeta.exe":
            return True
    return False

def delete_registry_keys():
    """Delete specific registry keys."""
    try:
        keys_to_delete = [
            r"HKCU\Software\SomeKey",
            r"HKLM\Software\AnotherKey"
        ]
        for key in keys_to_delete:
            subprocess.run(['reg', 'delete', key, '/f'], check=True)
        print_centered(f"{RED}Registry keys deleted successfully.{RESET}", os.get_terminal_size().columns)
    except Exception as e:
        print_centered(f"{RED}Failed to delete registry keys: {e}{RESET}", os.get_terminal_size().columns)

def delete_temp_files():
    """Delete temporary files."""
    temp_dir = os.getenv('TEMP')
    try:
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                os.remove(os.path.join(root, file))
        print_centered(f"{RED}Temporary files deleted successfully.{RESET}", os.get_terminal_size().columns)
    except Exception as e:
        print_centered(f"{RED}Failed to delete temporary files: {e}{RESET}", os.get_terminal_size().columns)

def delete_recent_files():
    """Delete recent files."""
    recent_dir = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Recent')
    try:
        for root, dirs, files in os.walk(recent_dir):
            for file in files:
                os.remove(os.path.join(root, file))
        print_centered(f"{RED}Recent files deleted successfully.{RESET}", os.get_terminal_size().columns)
    except Exception as e:
        print_centered(f"{RED}Failed to delete recent files: {e}{RESET}", os.get_terminal_size().columns)

def delete_event_logs():
    """Delete event logs."""
    try:
        logs_to_clear = [
            'Application', 'Security', 'System'
        ]
        for log in logs_to_clear:
            subprocess.run(['wevtutil', 'cl', log], check=True)
        print_centered(f"{RED}Event logs cleared successfully.{RESET}", os.get_terminal_size().columns)
    except Exception as e:
        print_centered(f"{RED}Failed to clear event logs: {e}{RESET}", os.get_terminal_size().columns)

def delete_downloads():
    """Delete files in Downloads folder."""
    downloads_dir = os.path.join(os.path.expanduser('~'), 'Downloads')
    try:
        for root, dirs, files in os.walk(downloads_dir):
            for file in files:
                os.remove(os.path.join(root, file))
        print_centered(f"{RED}Files in Downloads folder deleted successfully.{RESET}", os.get_terminal_size().columns)
    except Exception as e:
        print_centered(f"{RED}Failed to delete files in Downloads folder: {e}{RESET}", os.get_terminal_size().columns)

def clear_app_data():
    """Clear application data."""
    app_data_dir = os.getenv('APPDATA')
    try:
        for root, dirs, files in os.walk(app_data_dir):
            for file in files:
                os.remove(os.path.join(root, file))
        print_centered(f"{RED}Application data cleared successfully.{RESET}", os.get_terminal_size().columns)
    except Exception as e:
        print_centered(f"{RED}Failed to clear application data: {e}{RESET}", os.get_terminal_size().columns)

def clear_browser_history():
    """Clear browser history."""
    try:
        # For simplicity, this example only covers Chrome history.
        # Extend this to other browsers as needed.
        chrome_history = os.path.join(os.getenv('LOCALAPPDATA'), 'Google', 'Chrome', 'User Data', 'Default', 'History')
        if os.path.exists(chrome_history):
            os.remove(chrome_history)
        print_centered(f"{RED}Browser history cleared successfully.{RESET}", os.get_terminal_size().columns)
    except Exception as e:
        print_centered(f"{RED}Failed to clear browser history: {e}{RESET}", os.get_terminal_size().columns)

def clean_pc():
    """Handle cleaning options."""
    def set_console_opacity(opacity):
        hwnd = ctypes.windll.kernel32.GetConsoleWindow()
        if hwnd:
            try:
                from ctypes.wintypes import HWND, BOOL, UINT, LPCVOID
                from ctypes import windll, byref, c_int
                DWM_API = windll.dwmapi
                DWM_API.DwmSetWindowAttribute.argtypes = [HWND, UINT, LPCVOID, UINT]
                DWM_API.DwmSetWindowAttribute(hwnd, 2, byref(c_int(int(opacity * 255))), 4)
            except Exception as e:
                print("Failed to set opacity:", e)

    def generate_random_title():
        return ''.join(random.choices(string.ascii_letters + string.digits, k=16))

    def title_spammer():
        while True:
            set_console_title(generate_random_title())
            time.sleep(0.01)  # Change title 100 times per second

    def print_centered(text, width=85):
        padding = (width - len(text)) // 2
        print(Fore.RED + ' ' * padding + text)

    # Set console opacity and start title spamming
    set_console_opacity(0.75)
    title_thread = threading.Thread(target=title_spammer, daemon=True)
    title_thread.start()

    while True:
        clear_console()
        print_centered("Select an option:", width=85)
        print_centered("[1] Delete Registry Keys Traces", width=85)
        print_centered("[2] Delete Temp Files", width=85)
        print_centered("[3] Delete Recent File Traces", width=85)
        print_centered("[4] Delete Event Log Traces", width=85)
        print_centered("[5] Delete Files in Downloads Folder", width=85)
        print_centered("[6] Clear Application Data", width=85)
        print_centered("[7] Clear Browser History", width=85)
        print_centered("[0] Exit", width=85)

        choice = input().strip()
        if choice == '1':
            delete_registry_keys()
        elif choice == '2':
            delete_temp_files()
        elif choice == '3':
            delete_recent_files()
        elif choice == '4':
            delete_event_logs()
        elif choice == '5':
            delete_downloads()
        elif choice == '6':
            clear_app_data()
        elif choice == '7':
            clear_browser_history()
        elif choice == '0':
            break
        else:
            print_centered(f"{RED}Invalid choice. Please try again.{RESET}", os.get_terminal_size().columns)
        time.sleep(2)  # Wait for a moment before showing the menu again

def main():
    # Start title updater in a separate thread
    title_thread = threading.Thread(target=title_updater, daemon=True)
    title_thread.start()

    # Set console opacity
    set_console_opacity(0.75)

    # Check HWID authentication
    hwid = get_hwid()
    if hwid == SPECIAL_HWID:
        clear_console()
        
        # Print the first ASCII art
        print_centered(" ____  ____  _____     ___  _____ _____ ", os.get_terminal_size().columns)
        print_centered("|  _ \\|  _ \\|_ _\\ \\   / / \\|_   _| ____|", os.get_terminal_size().columns)
        print_centered("| |_) | |_) || | \\ \\ / / _ \\ | | |  _|  ", os.get_terminal_size().columns)
        print_centered("|  __/|  _ < | |  \\ V / ___ \\| | | |___ ", os.get_terminal_size().columns)
        print_centered("|_|   |_| \\_\\___|  \\_/_/   \\_\\_| |_____|", os.get_terminal_size().columns)
        print_centered("                                         ", os.get_terminal_size().columns)

        time.sleep(2)  # Display for 2 seconds
        clear_console()

        # Print the second ASCII art
        print_centered("███▄ ▄███▓▓█████  ███▄    █  █    ██ ", os.get_terminal_size().columns)
        print_centered("▓██▒▀█▀ ██▒▓█   ▀  ██ ▀█   █  ██  ▓██▒", os.get_terminal_size().columns)
        print_centered("▓██    ▓██░▒███   ▓██  ▀█ ██▒▓██  ▒██░", os.get_terminal_size().columns)
        print_centered("▒██    ▒██ ▒▓█  ▄ ▓██▒  ▐▌██▒▓▓█  ░██░", os.get_terminal_size().columns)
        print_centered("▒██▒   ░██▒░▒████▒▒██░   ▓██░▒▒█████▓ ", os.get_terminal_size().columns)
        print_centered("░ ▒░   ░  ░░░ ▒░ ░░ ▒░   ▒ ▒ ░▒▓▒ ▒ ▒ ", os.get_terminal_size().columns)
        print_centered("░  ░      ░ ░ ░  ░░ ░░   ░ ▒░░░▒░ ░ ░ ", os.get_terminal_size().columns)
        print_centered("░      ░      ░      ░   ░ ░  ░░░ ░ ░ ", os.get_terminal_size().columns)
        print_centered("       ░      ░  ░         ░    ░     ", os.get_terminal_size().columns)
        print_centered("                                      ", os.get_terminal_size().columns)

        time.sleep(2)  # Display for 2 seconds
        clear_console()

        # Loading spinner
        print_centered("Loading", os.get_terminal_size().columns)
        for _ in range(10):  # 5 seconds with a 0.5-second delay per step
            for ch in '|/-\\':
                print_centered(f"{RED}{ch*5}{RESET}", os.get_terminal_size().columns)
                time.sleep(0.5)
                clear_console()
        clear_console()

    if hwid not in AUTHORIZED_HWIDS and hwid != SPECIAL_HWID:
        print_centered(f"{RED}Unauthorized access. This HWID is not authorized.{RESET}", os.get_terminal_size().columns)
        time.sleep(5)
        return

    while True:
        clear_console()
        display_menu()
        command = input().strip().lower()
        if command == 'inject':
            inject()
        elif command == 'clean pc':
            clean_pc()
        elif command == 'close':
            break
        else:
            print_centered(f"{RED}Invalid command. Please try again.{RESET}", os.get_terminal_size().columns)
        time.sleep(2)

if __name__ == "__main__":
    main()
