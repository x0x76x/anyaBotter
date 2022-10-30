import string, re, os, json, time, socket, random, requests, threading, sys
import src.DiscordRPC as discordrpc
import src.friendbot as feature1
import src.favouritebot as feature2

config = json.load(open("config.json", "r"))

PROXY_TYPE = config['proxymode']
COOKIES_FILE = config['cookiesfile']
PROXIES_FILE = config['proxiesfile']

with open(f'{COOKIES_FILE}', 'r') as cookies:
    cookies = cookies.read().splitlines()

with open(f'{PROXIES_FILE}', 'r') as proxies:
    proxies = proxies.read().splitlines()


def main():
    os.system('cls & title Anya Botter #1')
    discordrpc.updateStatus("Anya Botter | #1")
    print("""
    ┌───────────────────────────────────────────────────────────────────────────────────────┐
    │ [1.] Friend Bot                                                                       │
    │ [2.] Favourite Bot                                                                    │
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
    
    if selection == "2":
        feature2.sendFunction()
main()