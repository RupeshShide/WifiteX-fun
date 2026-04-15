#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
import random

# ===== COLORS =====
RESET = "\033[0m"
BOLD = "\033[1m"

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BLUE = "\033[94m"

# ===== CLEAR =====
def clear():
    os.system("clear")

# ===== BANNER =====
def banner():
    print(BOLD + GREEN + "### WiFiteX Simulation Tool ###" + RESET)
    print(CYAN + "Developed by Jugnu\n" + RESET)

# ===== PROGRESS BAR =====
def progress(task):
    print("\n" + CYAN + task + RESET)

    total_length = 30

    for i in range(0, 101, 5):
        filled = int((i/100) * total_length)
        bar = GREEN + "#" * filled + RESET + "-" * (total_length - filled)

        print(f"\r[{bar}] {i}%", end="")
        time.sleep(0.1)

    print("\n")

# ===== FAKE NETWORK SCAN =====
def scan():
    clear()
    banner()

    progress("🔍 Scanning WiFi networks...")

    print(GREEN + "Network scan completed. Select network below:\n" + RESET)

    networks = [
        ("JioFiber", "WPA2", "-40 dBm"),
        ("Airtel_X", "WPA2", "-55 dBm"),
        ("HomeNet", "WEP", "-70 dBm"),
        ("Cafe_Free", "OPEN", "-80 dBm"),
    ]

    for i, net in enumerate(networks):
        print(f"{BLUE}[{i}]{RESET} {net[0]} | {net[1]} | Signal: {net[2]}")

    return networks

# ===== SIMULATION =====
def simulate_attack(network):
    clear()
    banner()

    print(GREEN + f"🎯 Target: {network[0]}" + RESET)
    print(YELLOW + f"🔐 Security: {network[1]}\n" + RESET)

    steps = [
        "Checking interface...",
        "Switching to monitor mode...",
        "Capturing handshake...",
        "Running dictionary attack...",
        "Analyzing packets..."
    ]

    for step in steps:
        progress(step)

    result = random.choice([
        "⚠️ Weak password detected! Saved in ~/wifitex/passwords.txt",
        "❌ Attack failed! Network is secure",
        "🔓 Password cracked! Check ~/wifitex/output.txt"
    ])

    print(BOLD + YELLOW + "📊 Result: " + RESET + result)

# ===== MAIN =====
def main():
    while True:
        print(BOLD + GREEN + "### WiFiteX Beta Developed by Jugnu ###" + RESET)
        print(CYAN + "Download tool from GitHub:" + RESET)
        print(YELLOW + "https://github.com/WifiteX-Fun\n" + RESET)

        print(BLUE + "1. Scan Networks" + RESET)
        print(RED + "0. Exit" + RESET)

        try:
            choice = input("\n] Select: ")

            if choice == "1":
                nets = scan()

                try:
                    idx = int(input("\nSelect target: "))
                    
                    if idx < 0 or idx >= len(nets):
                        raise ValueError

                    simulate_attack(nets[idx])

                except:
                    print(RED + "❌ Invalid selection!" + RESET)

            elif choice == "0":
                print(GREEN + "Thank you 👋" + RESET)
                break

            else:
                print(RED + "❌ Invalid option!" + RESET)

        except KeyboardInterrupt:
            print(RED + "\n❌ Interrupted! Returning to menu..." + RESET)
            continue

        input("\nPress Enter to continue...")
        clear()

# ===== RUN =====
if __name__ == "__main__":
    main()