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

def roiFormula(startAmount, finalAmount):
  netProfit = float(finalAmount) - float(startAmount)
  roi = netProfit/startAmount * 100
  
  return float(f"{roi:.2f}")

def isProfit(amount):
  if float(amount) > 0:
    return True
  else:
    return False

def compound():
  balance = 0
  duration = ''
  time = 0
  growth = 0
  total = 0
  
  def compoundFormula(p, r, d):
    total = p * pow(1 + (r/100), d)
    return float(f"{total:.2f}")
  
  balanceCheck = 0
  timeCheck = 0
  growthCheck = 0
  
  while balanceCheck <= 0:
    balanceCheck = getInput("number", "Starting Balance: ")
    if balanceCheck <= 0:
      print(Fore.RED + "Number Need To Be > 0")
      continue
    else:
      balance = balanceCheck
      break
  
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
  
  while timeCheck <= 0:
    timeCheck = getInput("number", f"Amount Of {duration}'s: ")
    if timeCheck <= 0:
      print(Fore.RED + "Number Need To Be > 0")
      continue
    else:
      time = timeCheck
      break
  
  while growthCheck <= 0:
    growthCheck = getInput("number", f"Growth/{duration} (%): ")
    if growthCheck <= 0:
      print(Fore.RED + "Number Need To Be > 0")
      continue
    else:
      growth  = growthCheck
      break
  
  total = str(compoundFormula(balance, growth, time))
  roi = str(roiFormula(balance, total))
  profit = str(isProfit(total))
  
  print("\n")
  print(f"{balance} after {growth}% for {time} {duration}'s:")
  print("Final Amount: " + total)
  print("ROI: " + roi + "%")
  print("Is Profit: " + profit)
 
def profit():
  startAmount = 0
  finalAmount = 0
  
  startAmountCheck = 0
  finalAmountCheck = 0
  
  while startAmountCheck <= 0:
    startAmountCheck = getInput("number", "Buy: ")
    if startAmountCheck <= 0:
      print(Fore.RED + "Number Need To Be > 0")
      continue
    else:
      startAmount = startAmountCheck
      break
  
  while finalAmountCheck <= 0:
    finalAmountCheck = getInput("number", "Sell: ")
    if finalAmountCheck <= 0:
      print(Fore.RED + "Number Need To Be > 0")
      continue
    else:
      finalAmount = finalAmountCheck
      break
  
  roi = str(roiFormula(startAmount, finalAmount))
  profit = str(isProfit(roi))
  
  print("\n")
  print(f"Initial Investment: {startAmount:.2f}\nSell Price: {finalAmount:.2f}")
  print("ROI: " + roi + "%")
  print("Is Profit: " + profit)
  
def menu():
  clear()
  banner()
  
  print(Fore.BLUE + "Tools Lists:")
  print("compound - Compounding Calc")
  print("profit - Profit/ROI Calc")
  print("journal - Journal")
  print("ai - Gemini AI*\n")
  tool = str(input(Fore.GREEN + "Select Tool (by id or name): ")).lower()
  match tool:
    case "compound" | "compounding" | "c" | "g":
      compound()
    case "profit" | "roi" | "p" | "r":
      profit()
    case "journal" | "j" | "note":
      journal()
    case "ai" | "gemini" | "ask":
      askGemini()
    case _:
      print(Fore.RED + "Invalid Tool")
      menu()

menu()