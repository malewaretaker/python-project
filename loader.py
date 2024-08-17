import ctypes
import subprocess
import time
import os     # some random said it was chat gpt, etc, so i recoded this (probally worst now did this in a rush icba) but yeah here!
import random
import string
import threading
from colorama import Fore, init
import psutil

init(autoreset=True)

RED = '\033[91m'
BLUE = '\033[94m'
RESET = '\033[0m'

AUTHORIZED_HWIDS = {
    "123456789ABCDEF0",
    "FEDCBA9876543210"
}

SPECIAL_HWID = "4C4C4544-0054-4310-8039-B4C04F584832"

def get_hwid():
    try:
        output = subprocess.check_output('wmic csproduct get uuid').decode()
        hwid = output.split('\n')[1].strip()
        return hwid
    except Exception as e:
        print(f"{RED}Error retrieving HWID: {e}{RESET}")
        return None

def set_console_opacity(opacity):
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    exstyle = ctypes.windll.user32.GetWindowLongW(hwnd, -20)
    ctypes.windll.user32.SetWindowLongW(hwnd, -20, exstyle | 0x00080000)
    ctypes.windll.user32.SetLayeredWindowAttributes(hwnd, 0, int(255 * opacity), 0x00000002)

def print_centered(text, width):
    padding = (width - len(text)) // 2
    print(' ' * padding + text)

def set_console_title(title):
    ctypes.windll.kernel32.SetConsoleTitleW(title)

def generate_random_title(length=10):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def title_updater():
    while True:
        set_console_title(generate_random_title())
        time.sleep(0.01)

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_menu():
    console_width = os.get_terminal_size().columns
    menu_title = f"{RED} idk what to put here type shit{RESET}"
    options = [
        "Type 'inject' to Inject",
        "Type 'clean pc' to Clean PC",
        "Type 'close' to Close"
    ]
    print_centered(menu_title, console_width)
    print()
    for option in options:
        print_centered(f"{RED}{option}{RESET}", console_width)
    print()
    print_centered("Please enter a command:", console_width)

def inject():
    if not is_roblox_running():
        print_centered(f"{RED}Roblox is not running.{RESET}", os.get_terminal_size().columns)
        time.sleep(2)
        return

    file_path = r"C:\Users\lyinglol\Downloads\wind\cmake-build-release-visual-studio\wind.exe"
    print_centered(f"{RED}Injecting...{RESET}", os.get_terminal_size().columns)
    time.sleep(1)
    subprocess.Popen([file_path], shell=True)
    time.sleep(2)
    print_centered(f"{RED}Injection complete!{RESET}", os.get_terminal_size().columns)
    time.sleep(2)
    clear_console()

def is_roblox_running():
    for process in psutil.process_iter(['name']):
        if process.info['name'] == "RobloxPlayerBeta.exe":
            return True
    return False

def delete_registry_keys():
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
    temp_dir = os.getenv('TEMP')
    try:
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                os.remove(os.path.join(root, file))
        print_centered(f"{RED}Temporary files deleted successfully.{RESET}", os.get_terminal_size().columns)
    except Exception as e:
        print_centered(f"{RED}Failed to delete temporary files: {e}{RESET}", os.get_terminal_size().columns)

def delete_recent_files():
    recent_dir = os.path.join(os.getenv('APPDATA'), 'Microsoft', 'Windows', 'Recent')
    try:
        for root, dirs, files in os.walk(recent_dir):
            for file in files:
                os.remove(os.path.join(root, file))
        print_centered(f"{RED}Recent files deleted successfully.{RESET}", os.get_terminal_size().columns)
    except Exception as e:
        print_centered(f"{RED}Failed to delete recent files: {e}{RESET}", os.get_terminal_size().columns)

def delete_event_logs():
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
    downloads_dir = os.path.join(os.path.expanduser('~'), 'Downloads')
    try:
        for root, dirs, files in os.walk(downloads_dir):
            for file in files:
                os.remove(os.path.join(root, file))
        print_centered(f"{RED}Files in Downloads folder deleted successfully.{RESET}", os.get_terminal_size().columns)
    except Exception as e:
        print_centered(f"{RED}Failed to delete files in Downloads folder: {e}{RESET}", os.get_terminal_size().columns)

def clear_app_data():
    app_data_dir = os.getenv('APPDATA')
    try:
        for root, dirs, files in os.walk(app_data_dir):
            for file in files:
                os.remove(os.path.join(root, file))
        print_centered(f"{RED}Application data cleared successfully.{RESET}", os.get_terminal_size().columns)
    except Exception as e:
        print_centered(f"{RED}Failed to clear application data: {e}{RESET}", os.get_terminal_size().columns)

def clear_browser_history():
    try:
        chrome_history = os.path.join(os.getenv('LOCALAPPDATA'), 'Google', 'Chrome', 'User Data', 'Default', 'History')
        if os.path.exists(chrome_history):
            os.remove(chrome_history)
        print_centered(f"{RED}Browser history cleared successfully.{RESET}", os.get_terminal_size().columns)
    except Exception as e:
        print_centered(f"{RED}Failed to clear browser history: {e}{RESET}", os.get_terminal_size().columns)

def clean_pc():
    set_console_opacity(0.75)
    title_thread = threading.Thread(target=title_updater, daemon=True)
    title_thread.start()

    while True:
        clear_console()
        print_centered("Select an option:", width=85)
        print_centered("[1] Delete Registry Keys", width=85)
        print_centered("[2] Delete Temporary Files", width=85)
        print_centered("[3] Delete Recent Files", width=85)
        print_centered("[4] Clear Event Logs", width=85)
        print_centered("[5] Delete Files in Downloads Folder", width=85)
        print_centered("[6] Clear Application Data", width=85)
        print_centered("[7] Clear Browser History", width=85)
        print_centered("[0] Exit", width=85)

        choice = input("Please enter your choice: ").strip()
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
            print_centered("Invalid choice. Please try again.", width=85)

def main():
    clear_console()
    hwid = get_hwid()
    if hwid in AUTHORIZED_HWIDS or hwid == SPECIAL_HWID:
        print_centered(f"{RED}HWID is authorized.{RESET}", os.get_terminal_size().columns)
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
                print_centered(f"{RED}Unknown command.{RESET}", os.get_terminal_size().columns)
    else:
        print_centered(f"{RED}HWID is not authorized.{RESET}", os.get_terminal_size().columns)
        time.sleep(2)

if __name__ == "__main__":
    main()
