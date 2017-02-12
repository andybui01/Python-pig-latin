#
# Author: github.com/andybui01
# Purpose: Pig latin program

def platin():

    word = input("What would you like to convert: ")
    word = word.split()

    for i in range(len(word)):
        k = word[i]

        if k[0] in ['a', 'e' , 'i', 'o' , 'u']:
            word[i] = k+'-way'

        elif k.isalpha() == False:
            word[i] = k
        
        elif k[0] not in ['a', 'e' , 'i', 'o' , 'u']:
            word[i] = k[1:] + '-' + k[0] + 'ay'

    return ' '.join(word)

    print(word)

