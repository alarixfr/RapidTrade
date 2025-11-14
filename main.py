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
  
def getInput(dataType, msg):
  if dataType == "number":
    while True:
      try:
        return float(input(Fore.RESET + msg))
      except ValueError:
        print(Fore.RED + "Invalid Number")
  elif dataType == "string":
    while True:
      try:
        return str(input(Fore.RESET + msg))
      except ValueError:
        print(Fore.RED + "Invalid String")
  else:
    print(Fore.RED + "Error")

def compound():
  balance = 0
  duration = ''
  time = 2
  growth = 0
  total = 0
  
  def compoundFormula(p, r, d):
    total = p * pow(1 + (r/100), d)
    return float(f"{total:.2f}")
  
  balance = getInput("number", "Starting Balance: ")
  
  while duration not in ["yearly", "monthly", "daily"]:
    duration = getInput("string", "Duration (y/m/d): ").lower()
    if duration == "y" or duration == "yearly" or duration == "year":
      duration = "yearly"
    elif duration == "m" or duration == "monthly" or duration == "month":
      duration = "monthly"
    elif duration == "d" or duration == "daily" or duration == "day":
      duration = "daily"
    else:
      print(Fore.RED + "Invalid Duration")
  
  time = getInput("number", f"Amount of {duration}'s?: ")
  growth = getInput("number", f"Growth/{duration} (%): ")
  
  total = str(compoundFormula(balance, growth, time))
  
  print("/n")
  print(f"{balance} after {growth}% for {time} {duration}'s: " + total)
  
def menu():
  clear()
  banner()
  
  print(Fore.BLUE + "Tools Lists:")
  print("compound - Compounding Calc")
  print("profit - Profit Calc")
  print("percent - Percentage Calc")
  print("tp - TP Calc")
  print("rr - RR Ratio Calc")
  print("journal - Journal")
  print("ai - Gemini AI*\n")
  tool = str(input(Fore.GREEN + "Select Tool (by id or name): ")).lower()
  match tool:
    case "compound" | "compounding" | "c":
      compound()
    case "profit" | "pnl" | "p":
      profit()
    case "percent" | "percentage" | "%":
      percentage()
    case "takeprofit" | "tp" | "sell":
      takeProfit()
    case "riskreward" | "rr" | "rrratio":
      riskReward()
    case "journal" | "j" | "note":
      journal()
    case "ai" | "gemini" | "ask":
      askGemini()
    case _:
      print(Fore.RED + "Invalid Tool")
      menu()

menu()