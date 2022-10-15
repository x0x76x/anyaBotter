import src.DiscordRPC as discordrpc
import string, re, os, json, time, socket, random, requests, threading

config = json.load(open("config.json", "r"))

COOKIES_FILE = config['cookiesfile']

with open(f'{COOKIES_FILE}', 'r') as cookies:
    cookies = cookies.read().splitlines()

def sendFriend(cookie, userid):
    try:
        with requests.session() as session:
            session.cookies['.ROBLOSECURITY'] = cookie
            session.headers['x-csrf-token'] = session.post('https://friends.roblox.com/v1/users/1/request-friendship').headers['x-csrf-token'] # retrieves x-csrf-token
            friend = session.post(f'https://friends.roblox.com/v1/users/{userID}/request-friendship') # this is pretty self explanatory.
            if friend.status_code == 200:
                print('sent!')
            else:
                print('')
    except:
        print()

def sendFunction(): # this is what the user will see
    os.system('cls & title Anya Botter - Friend Bot')
    discordrpc.updateStatus('Anya Botter | Friend Bot')
    print('User ID')
    userID = input("> ")
    print('Amount')
    amount = input("> ")
    for x in range(int(amount)):
        cookie = cookies[x]
        threading.Thread(target=sendFriend, args=(cookie,userid,)).start()
        
    input() 