import os
import shutil
import hashlib
cntr = 0
def encrypting(data):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
def getmda5(data):
    mda = hashlib.md5()
    data1 = data.encode('utf-8')
    mda.update(data1)
    m = mda.hexdigest()
    return m
def packetname(cntr):
    newname = "packet"+str(cntr)
    return newname
def packetcover1(n, name):
    coverage = '<'+str(name)+'>'
    return coverage
def packetcover2(n, name):
    coverage = '<'+'/'+str(name)+'>'
    return coverage
def createpacket(packetdata, packetnumber):
    name = packetname(packetnumber)
    md5 = getmda5(packetdata)
    f = open(name, "w+")
    data = packetcover1(packetnumber,name )+'\n'+packetdata+'\n'+packetcover2(packetnumber,name)+'\n'+md5
    f.write(data)
    return 0
cntr = 0
def read(packetnumber):
    name = 'packet'+str(packetnumber)
    packettoopen = open(name, 'r')
    target = packettoopen.readlines()[1]
    print(target)
    return 0 

def send(cntr):
    print('Got', cntr, 'packets')
    last_CNTR = cntr
    for i in range(cntr):
        read(cntr)
        cntr -=1
    mainstream(last_CNTR)
def mainstream(cntr):
    while True:
        inp = input(('Type packet data '))
        if inp == '__END__' or inp == '__SEND__' or inp == '__READ__' or inp == '__CHECK__':
            break
        cntr += 1
        createpacket(inp, cntr)
    if inp == '__CHECK__':
        via = input('Number of packet to check ')
        name = 'packet'+via
        packettoopen = open(name, 'r')
        lastline = packettoopen.readlines()[-1]
        packettoopen = open(name, 'r')
        target = packettoopen.readlines()[1]
        target = target[:-1]
        mdhash = getmda5(target)
        print(mdhash, ' ', lastline, ' ' ,target)
        if mdhash == lastline:
            print('Integrity OK')
            mainstream(cntr)

        else:
            print('Integrity bad')
            mainstream(cntr)

    elif inp == '__READ__':
        via = input('Number of packet to read ')
        read(via)
        mainstream(cntr)
    elif inp == '__SEND__':
        print('Opening sending daemon')
        send(cntr)

    return 0

try:
    os.mkdir('packetdir')
    os.chdir('packetdir')
except:
    shutil.rmtree('packetdir')
    os.mkdir('packetdir')
    os.chdir('packetdir')
if __name__ == "__main__":
    mainstream(cntr)
        
