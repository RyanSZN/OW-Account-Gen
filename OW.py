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
    
    #grabs how many lines are found in the email implying how many accounts can be made
    def grabEmailLength():
        file1 = open('emails.txt', 'r') 

        number_of_lines = 0

        for line in file1:
            line = line.strip("\n")

            words = line.split()
            global number_of_lines
            number_of_lines += 1
            
    #starting the session
    def getSession(number):
        print(Fore.YELLOW + f'[{datetime.datetime.now()}] [Task #{str(number)}] - Getting Session.')
        
        #grabs the email from the text file
        with open('emails.txt', 'r')  as f:
            for line in f:
                global email
                email = line.strip("\n")
                
        #list of chars to create a random passwrod
        chars = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*'
        
        #creating the random password
        for p in range(1):
            global password
            password = ''
            for c in range(9):
                password += random.choice(chars)
                
        #grabbing a random proxy and splitting it to a dict
        proxyLines = open('proxies.txt').read().splitlines() #reading each line
        randomProxy = random.choice(lines) #grabbing a random line
        finalProxy = randomProxy.split(':') #splitting the proxy between each ":"

        r = session.get(url='https://www.off---white.com/en-us/account/register') #generating a session on the website
        
        #session headers for making the post request
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
        
        #configuring how the proxy will be sent when making the request
        try:
            proxies = {
                'http': f'http://{finalProxy[2]}:{finalProxy[3]}:{finalProxy[0]}:{finalProxy[1]}/' #proxy with username and pass (unsecured)
                'https':f'http://{finalProxy[2]}:{finalProxy[3]}:{finalProxy[0]}:{finalProxy[1]}/' #proxy with username and pass (secured)
            }
        except:
            proxies = {
                'http':f'http://{finalProxy[0]}:{finalProxy[1]}', #proxy for no username or password (unsecured)
                'https':f'https://{finalProxy[0]}:{finalProxy[1]}' #proxy for no username or password (secured)
            }   
            
        #the data being sent including a random name being genned and the email grabbed with the random generated password
        payload = {
            "name": names.get_full_name(), #random full name
            "username":email, #email
            "email":email, #email
            "password":password, #random gen password
            "countryCode":"US", #country
            "receiveNewsletters":False
        }
        
        #letting the user know what email and password is being used
        print(Fore.YELLOW + f'[{datetime.datetime.now()}] [Task #{str(number)}] - Sending Email: {email} and Sending Password: {password}')
        
        #sending a post request to the url and submitting it with the headers, proxies, payload set previously
        sessionResponse = session.post(url='https://www.off---white.com/en-us/account/register', headers=sessionHeaders, proxies=proxies, data=payload) 
        
        #setting the post request response to a json format to get information easier.
        sessionJson = json.loads(sessionResponse.text)
        
        #checking if the post request was successful or received an error (plan to add an error reason)
        if sessionJson['success'] == False:
            print(Fore.YELLOW + f'[{datetime.datetime.now()}] [Task #{str(number)}] - Email: {email} and Password: {password} sent Unsuccessfully.')
        else:
            print(Fore.YELLOW + f'[{datetime.datetime.now()}] [Task #{str(number)}] - Email: {email} and Password: {password} sent Successfully!')
            
    #threading which starts the x amount of tasks
    def runTask(number):
        #initializing the task
        print(Fore.YELLOW + f'[{datetime.datetime.now()}] Starting Task #{str(number)}')
        #starting the main session
        getSession(number)
    
    #misc
    threads = []
    
    #for every line found in the emails.txt file it will start this command which will essentially start the whole bot
    for i in range(number_of_lines):
        t = threading.Thread(target=runTask, args=(i,))
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

OffWhiteGen()
