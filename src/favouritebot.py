import src.DiscordRPC as discordrpc
import string, re, os, json, time, socket, random, requests, threading

config = json.load(open("config.json", "r"))

PROXY_TYPE = config['proxymode']
COOKIES_FILE = config['cookiesfile']
PROXIES_FILE = config['proxiesfile']

with open(f'{COOKIES_FILE}', 'r') as cookies:
    cookies = cookies.read().splitlines()

with open(f'{PROXIES_FILE}', 'r') as proxies:
    proxies = proxies.read().splitlines()

def sendFavourite(cookie, assetid, prox):
    try:
        with requests.session() as session:
            session.cookies['.ROBLOSECURITY'] = cookie
            session.headers['x-csrf-token'] = session.post('https://friends.roblox.com/v1/users/1/request-friendship').headers['x-csrf-token']
            proxy = {'http':f'{PROXY_TYPE}://'+prox, 'https':f'{PROXY_TYPE}://'+prox}
            favourite = session.post(f'https://www.roblox.com/favorite/toggle', proxies=proxy, data={'assetID':assetid})
            if favourite.status_code == 200:
                print('omg worked!?')
            else:
                print('omg didnt work!? dogshit proxies or cookies bruv')
    except:
        print('idk skipped or somet!?')

def sendFunction():
    os.system('cls & title Anya Botter - Favourite Bot')
    discordrpc.updateStatus('Anya Botter | Favourite Bot')
    print('Asset ID')
    asset = input("> ")
    print('Amount')
    amount = input("> ")
    for x in range(int(amount)):
        cookie = cookies[x]
        try:
            proxy = proxies[x]
            pos += 1
        except:
            proxy = random.choice(proxies)
        threading.Thread(target=sendFavourite,args=(cookie, asset,proxy,)).start()
        time.sleep(0.001)
    input()