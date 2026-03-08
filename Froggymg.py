#!/usr/bin/env python3

import os
import time
import requests
import random

API_URL = "https://smmcheep.com/api/v2"
API_KEY = "28ada1150823bfadd8f84149b19203e6"

def clear():
    os.system("clear")

def banner():
    print("""
======================================
   🐸 FROGGY REACTION TOOL 🐸
======================================
Owner : SiamTheFrog
Github: https://github.com/
======================================
""")

def progress():
    bar = ["[░░░░░░░░░░] 0%",
           "[████░░░░░░] 40%",
           "[███████░░░] 70%",
           "[██████████] 100%"]

    for i in bar:
        print(i)
        time.sleep(1)

def start_task():

    link = input("\n📌 Facebook Post Link: ")
    qty = input("🔥 Reaction Quantity: ")

    print("\n🚀 Starting injection...\n")
    progress()

    try:
        data = {
            "key": API_KEY,
            "action": "add",
            "service": 10122,
            "link": link,
            "quantity": qty
        }

        r = requests.post(API_URL, data=data).json()

        if "order" in r:
            print("\n✅ TASK STARTED")
            print("Task ID :", r["order"])
            print("\nUse option 2 to check status\n")
        else:
            print("\n❌ Failed to start task")

    except:
        print("\n❌ Network error")

def check_status():

    order = input("\n🔎 Enter Task ID: ")

    try:
        data = {
            "key": API_KEY,
            "action": "status",
            "order": order
        }

        r = requests.post(API_URL, data=data).json()

        print("\n📡 TASK STATUS\n")

        print("Status    :", r.get("status"))
        print("Start     :", r.get("start_count"))
        print("Remaining :", r.get("remains"))

        status = r.get("status")

        if status == "Completed":
            print("\nProgress: [██████████] 100%")
        elif status == "Processing":
            print("\nProgress: [█████░░░░░] 50%")
        else:
            print("\nProgress: [█░░░░░░░░░] 10%")

    except:
        print("\n❌ Status check failed")

def menu():

    while True:

        print("""
1️⃣ Start Reaction Task
2️⃣ Check Task Status
3️⃣ Exit
""")

        choice = input("Select option: ")

        if choice == "1":
            start_task()

        elif choice == "2":
            check_status()

        elif choice == "3":
            print("\n👋 Exiting tool")
            break

        else:
            print("Invalid option")

clear()
banner()
menu()
