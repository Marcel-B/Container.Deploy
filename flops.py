#!/usr/bin/env python3
import requests 
import os.path
from os import path
import subprocess
import time
import datetime
import sys

def writeFile(serviceName, timeHash):
    print("  Write hash ", timeHash)
    f=open(str(serviceName + ".txt"), "w")
    f.write(timeHash)
    f.close()

def startService(repoName, serviceName):
    subprocess.run(["docker", "service", "update", "--image", repoName, serviceName])
    print("  Update docker service")

def fetchImage(imageId):
    path=str("  " + URL + imageId)
    print(path)
    r=requests.get(path)
    data=r.json()
    timeHash=data['timeHash']
    repoName=data['repoName']
    tag=data['tag']
    repoName=str(repoName + ":" +  tag)
    return timeHash, repoName

def start():
    print(datetime.datetime.now())
    try:
        file=open("imageIds.txt", "r")
        for line in file:
            try:
                line=line.replace("\n","")
                fields=line.split(",")
                imageId=fields[0]
                serviceName=fields[1]
                timeHash, repoName=fetchImage(imageId)
                exists=path.exists(str(serviceName) + ".txt")
                if exists is False:
                    writeFile(serviceName, timeHash)
                    startService(repoName, serviceName)
                else:
                    f=open(str(serviceName + ".txt"), "r")
                    if f.mode == "r":
                        contents=f.read()
                        if contents != timeHash:
                            writeFile(serviceName, timeHash)
                            startService(repoName, serviceName)
            except:
                print(str("! Error with with line '" + line + "'"))
                print()

    except:
        print("! Error occurred")
    print()
URL = sys.argv[1]

start()
