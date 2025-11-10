# RapidTrade by Alaric Abyasa
from colorama import Fore
import json, os, time, datetime, tabulate, click

def clear(seconds=0):
  time.sleep(seconds)
  if os.name == "nt":
    os.system("cls")
  else:
    os.system("clear")

def banner():
  print(Fore.GREEN + r"""
  _____             _     _ 
 |  __ \           (_)   | |
 | |__) |__ _ _ __  _  __| |
 |  _  // _` | '_ \| |/ _` |
 | | \ \ (_| | |_) | | (_| |
 |_|__\_\__,_| .__/|_|\__,_|
 |__   __|   | |    | |     
    | |_ __ _|_|  __| | ___ 
    | | '__/ _` |/ _` |/ _ \
    | | | | (_| | (_| |  __/
    |_|_|  \__,_|\__,_|\___|
  """)
  print(Fore.YELLOW + "RapidTrade v0.0.0")

clear()
banner()