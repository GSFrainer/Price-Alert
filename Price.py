from binance.websockets import BinanceSocketManager
from binance.client import Client
from binance.enums import *

from playsound import playsound
from pprint import pprint
import time

import config

symbol = 'BTCUSDT'
upper = 45000.0
lower = 38000.0

sounds = {
    "Alert": "./Sounds/Alert.wav",
    "Effect1": "./Sounds/Effect_1.wav",
    "Effect2": "./Sounds/Effect_2.wav",
    "Effect3": "./Sounds/Effect_3.wav",
}

client = Client(config.KEY, config.SECRET)
manager = BinanceSocketManager(client)


def process_message(msg):
    try:
        if float(msg['k']['l']) > upper:
            pprint(symbol+' price above '+str(upper))
            playsound(sounds['Effect1'])
            time.sleep(5)

        if float(msg['k']['l']) < lower:
            pprint(symbol+' price under '+str(lower))
            playsound(sounds['Alert'])
            time.sleep(5)

        if msg['k']['x'] == True:
            pprint(msg['k']['c'])

    except Exception as e:
        print('Error: '+symbol)
        pprint(e)


price = manager.start_kline_socket(symbol, process_message, interval=KLINE_INTERVAL_1MINUTE)

manager.start()
    
