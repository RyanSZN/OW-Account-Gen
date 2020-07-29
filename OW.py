'''
------------------------modules-----------------------------
'''

import requests
from bs4 import BeautifulSoup
import json
import threading
import datetime
import time
import os
from discord_webhook import DiscordWebhook, DiscordEmbed
from colorama import Fore, Back, Style
import names
import random

'''
------------------------misc-----------------------------
'''
class OffWhiteGen():
    session = requests.Session()
    clear = lambda: os.system("cls")
    clear()

    '''
    ------------------------CLI-----------------------------
    '''

    asciiArt = ('''
       ____ _       __   ___                               __     ______         
      / __ \ |     / /  /   | ______________  __  ______  / /_   / ____/__  ____ 
     / / / / | /| / /  / /| |/ ___/ ___/ __ \/ / / / __ \/ __/  / / __/ _ \/ __ \ 
    / /_/ /| |/ |/ /  / ___ / /__/ /__/ /_/ / /_/ / / / / /_   / /_/ /  __/ / / /
    \____/ |__/|__/  /_/  |_\___/\___/\____/\__,_/_/ /_/\__/   \____/\___/_/ /_/
    \nby RyanSZN#3588    
    ===============================================================================                                                                     
    ''')
    print(Fore.LIGHTBLACK_X + asciiArt)
    print(Fore.LIGHTBLACK_X + f'[{datetime.datetime.now()}]','[PROFILE]', 'Loading Emails and Passwords...')
    time.sleep(2)
    print(Fore.LIGHTBLACK_X + f'[{datetime.datetime.now()}]','[PROFILE]', 'Emails and Passwords Loaded!')
    time.sleep(.5)
    print(Fore.LIGHTBLACK_X + "===============================================================================")
    grabEmailLength()

    def grabEmailLength():
        file1 = open('emails.txt', 'r') 

        number_of_lines = 0

        for line in file1:
            line = line.strip("\n")

            words = line.split()
            global number_of_lines
            number_of_lines += 1

    def getSession(number):
        print(Fore.YELLOW + f'[{datetime.datetime.now()}] [Task #{str(number)}] - Getting Session.')

        with open('emails.txt', 'r')  as f:
            for line in f:
                global email
                email = line.strip("\n")

        chars = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*'

        for p in range(1):
            global password
            password = ''
            for c in range(9):
                password += random.choice(chars)

        proxyLines = open('proxies.txt').read().splitlines()
        randomProxy = random.choice(lines)
        finalProxy = randomProxy.split(':')

        r = session.get(url='https://www.off---white.com/en-us/account/register')

        sessionHeaders = {
            'accept': 'application/json, text/plain, */*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'en-US',
            'content-length': '147',
            'content-type': 'application/json',
            'ff-country': 'US',
            'ff-currency': 'USD',
            'origin': 'https://www.off---white.com',
            'referer': 'https://www.off---white.com/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'
        }
        try:
            proxies = {
                'http': f'http://{finalProxy[2]}:{finalProxy[3]}:{finalProxy[0]}:{finalProxy[1]}/'
                'https':f'http://{finalProxy[2]}:{finalProxy[3]}:{finalProxy[0]}:{finalProxy[1]}/'
            }
        except:
            proxies = {
                'http':f'http://{finalProxy[0]}:{finalProxy[1]}',
                'https':f'https://{finalProxy[0]}:{finalProxy[1]}'
            }   

        payload = {
            "name": names.get_full_name(),
            "username":email,
            "email":email,
            "password":password,
            "countryCode":"US",
            "receiveNewsletters":False
        }

        print(Fore.YELLOW + f'[{datetime.datetime.now()}] [Task #{str(number)}] - Sending Email: {email} and Sending Password: {password}')

        sessionResponse = session.post(url='https://www.off---white.com/en-us/account/register', headers=sessionHeaders, proxies=proxies, data=payload) 

        sessionJson = json.loads(sessionResponse.text)

        if sessionJson['success'] == False:
            print(Fore.YELLOW + f'[{datetime.datetime.now()}] [Task #{str(number)}] - Email: {email} and Password: {password} sent Unsuccessfully.')
        else:
            print(Fore.YELLOW + f'[{datetime.datetime.now()}] [Task #{str(number)}] - Email: {email} and Password: {password} sent Successfully!')

    def runTask(number):
        print(Fore.YELLOW + f'[{datetime.datetime.now()}] Starting Task #{str(number)}')
        getSession(number)

    threads = []

    for i in range(number_of_lines):
        t = threading.Thread(target=runTask, args=(i,))
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

OffWhiteGen()