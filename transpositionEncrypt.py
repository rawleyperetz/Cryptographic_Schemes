# Transposition Cipher This cipher also uses the key and the message in string format as arguments. 
# Given the string to be 'hello world' with a key of 4, the cipher becomes 'hore llwdlo ' Explaining: after the first value, h, 
# count 4 value places to the right and the yields o and so on. Easy peasy, eh? I suck at explaining :) Apologies.

import numpy as np 
import math 
import pyperclip

def main():
    myMessage = 'Common sense is not so common.'
    myKey = 8
    cipherText = encryptMessage(myMessage, myKey)
    # Print the encrypted string in ciphertext to the screen, with
    # a | ("pipe" character) after it in case there are spaces at
    # the end of the encrypted message:
    print(cipherText + '|')
    # Copy the encrypted string in ciphertext to the clipboard:
    pyperclip.copy(cipherText)

def encryptMessage(message:str,key:int)->str:
    #this is the code for transposition cipher
    message = list(message)
    rows = int(len(message) % key)
    spaces = [' ' for i in range(((rows*key) - len(message)) % key) if (rows*key) != len(message)]
    #code lines 22 to 24 is the same as code line 20. 
    '''if (rows*key) != len(message):
        for i in range(((rows*key) - len(message)) % key):
            message.append(' ')'''
    message = message + spaces
    arr = np.array(message)  
    box = arr.reshape(math.ceil(len(message)/key),key)
    translatedMessage = ''.join(list(box.transpose().flatten()))
    return translatedMessage + '|'

if __name__=='__main__':
    main()





