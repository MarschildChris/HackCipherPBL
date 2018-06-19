import random

#give a string message and return the converted cipherText
def caesarEncoding(message,key):
    result = ''
    if(key==0):
        key = int(random.random()*24+1)
    for i in message:
        if(i==' '):
            result+=' '
            continue
        if(ord(i)+key<123):
            result+=chr(ord(i)+key)
        else:
                result+=(chr(ord(i)+key-26))
    return result





#give a cipherText and return the hacked origin massage
def caesarDecoding(code):
    for i in range(1,25):
        possible = ""
        for c in code:
            if(c==' '):
                possible+=' '
                continue
            if(ord(c)+i<123):
                possible+=chr(ord(c)+i)
            else:
                possible+=chr(ord(c)+i-26)
        print(possible)
        if(input('Is it make sense(y/n)').lower()=='y'):
            return possible

def transpositionEncoding(message):
    cipherText = ''
    key = int(random.random()*(len(message)-2))+2
    for i in range(key):
        j = i
        while j<len(message):
            cipherText += message[j]
            j+=key
    return cipherText

def transpositionDecoding(cipherText):
    for possibleKey in range(2,len(cipherText)):
        possibleMsg = ''
        reminder = len(cipherText)%possibleKey
        width = int(len(cipherText)/possibleKey)

        for a in range(width):
            i=a
            for b in range(possibleKey):
                possibleMsg+=cipherText[i]
                i += width
                if (b < reminder):i+=1

        i=width
        for a in range(reminder):
            possibleMsg+=cipherText[i]
            i+=width+1

        if(input(str(possibleMsg)+'\nIs it make sense?(y/n)').lower()=='y'):
            return str(possibleMsg)+"\nkey="+str(possibleKey)

def vigenereEncoding(msg,key):
    cipherText = ''
    spaces = 0
    for i in range(len(msg)):
        if(msg[i]==' '):spaces+=1
        cipherText+=caesarEncoding(msg[i],ord(key[(i-spaces)%len(key)])-97)
    return cipherText

#def vigenereDecoding(msg):


def multiplicationEncoding(msg,key):
    result = ''
    for i in msg:
        if(i!=' '):result += chr((ord(i) - 97) * key % 26 + 97)
        else: result+=' '
    return(result)

def multiplicationDecoding(cipherText):
    possibleKey=3
    while(possibleKey<26):
        possible=''
        for i in cipherText:
            if(i==' '):continue
            guess = ord(i)-97
            while(guess%possibleKey!=0):
                guess+=26
            possible+=chr(int(guess/possibleKey+97))
        print(possible+' key='+str(possibleKey))
        if(possibleKey==11):possibleKey+=2
        possibleKey+=2