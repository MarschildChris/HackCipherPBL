import cipherFunctions
cipherText = cipherFunctions.transpositionEncoding('today is a nice day')
print('\n'+cipherText)
print('\n'+cipherFunctions.transpositionDecoding(cipherText))