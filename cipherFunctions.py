import random

#give a string message and return the converted cipherText
def caesarEncoding(message):
    result = ''
    password = int(random.random()*24+1)
    for i in message:
        if(ord(i)+password<123):
            result+=chr(ord(i)+password)
        else:
            result+=(chr(ord(i)+password-26))
    return result

#give a cipherText and return the hacked origin massage
def caesarDecoding(code):
    for i in range(1,25):
        possible = ""
        for c in code:
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