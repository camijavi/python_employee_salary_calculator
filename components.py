import os


def printError(message):
    print(f"\033[31m{message}\033[0m")


def printWarning(message):
    print(f"\033[33m{message}\033[0m")


def printSucess(message):
    print(f"\033[32m{message}\033[0m")


def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')