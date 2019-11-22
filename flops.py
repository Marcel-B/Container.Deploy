import requests 
import os.path
from os import path
import subprocess
import time
import datetime
import sys


def writeFile(hash):
    print("  Write hash ", hash)
    f=open("ts.txt", "w")
    f.write(hash)
    f.close()

def startService(repoName, serviceName):
    subprocess.run(["docker", "service", "update", "--image", repoName, serviceName])
    print("  Update docker service")

def start():
    while True:
        try:
            print(datetime.datetime.now())
            r=requests.get(url = URL)
            data=r.json()
            #print(data)
            timeHash=data['timeHash']
            repoName=data['repoName']
            tag=data['tag']
            name=str(repoName + ":" +  tag)
            print(str("  " + name))
            e=path.exists('ts.txt')

            if e is False:
                print("  No File detected")
                writeFile(timeHash)
                startService(name, serviceName)
            else:
                f=open("ts.txt", "r")
                if f.mode == 'r':
                    contents =f.read()
                    if contents != timeHash:
                        print(timeHash)
                        writeFile(timeHash)
                        startService(name, serviceName)
        except:
            print(" ! Error occurred")
        print()
        time.sleep(60 * 5)
URL = sys.argv[1]
serviceName = sys.argv[2]

start()
