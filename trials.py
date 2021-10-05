import startup

def printQ():
    output = ""
    for gamer in startup.trialsQ:
        output = output + gamer + "\n"
    output = output + "Good luck gamers"
    return output

def queued(name):
    print(name)
    print (name in startup.trialsQ)
    return name in startup.trialsQ
