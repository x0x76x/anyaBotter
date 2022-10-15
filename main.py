import string, re, os, json, time, socket, random, requests, threading, sys
import src.DiscordRPC as discordrpc
import src.friendbot as feature1

config = json.load(open("config.json", "r"))

COOKIES_FILE = config['cookiesfile']

with open(f'{COOKIES_FILE}', 'r') as cookies:
    cookies = cookies.read().splitlines()


def main():
    os.system('cls & title Anya Botter #1')
    discordrpc.updateStatus("Anya Botter | #1")
    print("""
    ┌───────────────────────────────────────────────────────────────────────────────────────┐
    │ [1.] Friend Bot                                                                       │
    │                                                                                       │
    │                                                                                       │
    │                                                                                       │
    │                                                                                       │
    │                                                                                       │
    │                                                                                       │
    │                                                                                       │
    └───────────────────────────────────────────────────────────────────────────────────────┘
    """)
    selection = input("> ")

    if selection == "1":
        feature1.sendFunction()
main()