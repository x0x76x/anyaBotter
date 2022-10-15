from pypresence import Presence
import time, json
    
config = json.load(open("config.json", "r"))
client_id = 1030638252060844093
RPC = Presence(client_id)
RPC.connect()

def updateStatus(status):
    if config["RPCEnabled"] == True:
        RPC.update(
            buttons =
            [
                {
                    "label": "GitHub", 
                    "url": "https://github.com/velayius/anyaBotter"
                }
            ],
            large_image = "https://i.imgur.com/wtZNBtj.jpg", 
            large_text = "Anya Botter #1", 
            details = status,
            start=time.time()
        )