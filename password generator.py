#!/usr/bin/env python3
"""
Password Generator PRO v2
Author : Vins
Description : Advanced password generator with save option & strength checker
"""

import random
import string
import os
from colorama import Fore, Style, init

# Init warna
init(autoreset=True)

def banner():
    os.system("clear" if os.name != "nt" else "cls")
    print(Fore.CYAN + Style.BRIGHT + """
██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ 
██╔══██╗██╔══██╗╚══███╔╝██╔════╝██║    ██║██╔═══██╗██╔══██╗
██████╔╝███████║  ███╔╝ █████╗  ██║ █╗ ██║██║   ██║██████╔╝
██╔═══╝ ██╔══██║ ███╔╝  ██╔══╝  ██║███╗██║██║   ██║██╔═══╝ 
██║     ██║  ██║███████╗███████╗╚███╔███╔╝╚██████╔╝██║     
╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝     
                """ + Fore.GREEN + "Password Generator PRO v2\n")

def generate_password(length=12, use_digits=True, use_symbols=True):
    chars = string.ascii_letters
    if use_digits:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation
    
    return ''.join(random.choice(chars) for _ in range(length))

def check_strength(password):
    length = len(password)
    score = 0
    if any(c.islower() for c in password): score += 1
    if any(c.isupper() for c in password): score += 1
    if any(c.isdigit() for c in password): score += 1
    if any(c in string.punctuation for c in password): score += 1
    if length >= 12: score += 1

    if score <= 2:
        return Fore.RED + "Weak ❌"
    elif score == 3:
        return Fore.YELLOW + "Medium ⚠️"
    else:
        return Fore.GREEN + "Strong ✅"

def save_to_file(passwords):
    with open("passwords.txt", "a") as f:
        for p in passwords:
            f.write(p + "\n")
    print(Fore.BLUE + "[+] Password disimpan di passwords.txt\n")

def main():
    banner()
    print(Fore.YELLOW + "=== Menu ===")
    print("1. Generate 1 password")
    print("2. Generate multiple passwords")
    print("3. Super Strong Mode (16+ chars)")
    print("0. Exit")

    choice = input(Fore.CYAN + "\n[?] Pilih menu: ")

    if choice == "1":
        length = int(input("[?] Panjang password: ") or 12)
        pw = generate_password(length)
        print(Fore.GREEN + f"\n[+] Password: {Fore.MAGENTA}{pw}")
        print("[*] Strength:", check_strength(pw))
        save = input(Fore.CYAN + "\nSimpan ke file? (y/n): ")
        if save.lower() == "y":
            save_to_file([pw])

    elif choice == "2":
        jumlah = int(input("[?] Berapa password mau dibuat: ") or 5)
        length = int(input("[?] Panjang password: ") or 12)
        passwords = [generate_password(length) for _ in range(jumlah)]
        print("\n[+] Passwords:")
        for p in passwords:
            print(Fore.MAGENTA + p, Fore.WHITE + "| Strength:", check_strength(p))
        save = input(Fore.CYAN + "\nSimpan semua ke file? (y/n): ")
        if save.lower() == "y":
            save_to_file(passwords)

    elif choice == "3":
        pw = generate_password(16, True, True)
        print(Fore.GREEN + f"\n[+] Super Strong Password: {Fore.MAGENTA}{pw}")
        print("[*] Strength:", check_strength(pw))
        save_to_file([pw])

    else:
        print(Fore.RED + "Keluar...")

if __name__ == "__main__":
    main()
