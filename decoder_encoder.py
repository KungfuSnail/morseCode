# THIS FILE IS STILL BEING DEVELOPED BUT EVERYTHING SHOULD WORK OK

import warnings
from pathlib import Path

morse = {
    "01": 'a', "1000": 'b', "1010": 'c',
    "100": 'd', "0": 'e', "0010": 'f',
    "110": 'g', "0000": 'h', "00": 'i',
    "0111": 'j', "101": 'k', "0100": 'l',
    "11": 'm', "10": 'n', "111": 'o',
    "0110": 'p', "1101": 'q', "010": 'r',
    "000": 's', "1": 't', "001": 'u',
    "0001": 'v', "011": 'w', "1001": 'x',
    "1011": 'y', "1100": 'z',
}

letterToMorse = {v: k for k, v in morse.items()} #Reverse of the morse dict, used for encoding


def determineDotDash(str):
    position = str.find("\n")
    if(position == -1): #In case we are at the end of the file and there is no newline, we add it so the code works
        str = str + "\n"

    if (len(str) >= 3 and str[-2] == ' ' and str[-3] == ' '):
        return '0'
    elif (len(str) >= 2 and str[-2] == ' '):
        return '1'
    elif (len(str) == 1 or str[-2] != ' '):
        return ' '
    else: 
        warnings.warn("Something went wrong in the encoding, unknown situation")


def stringToLetter(string):
    """Turns a string that looks like 01 111 010 into letters like e x p"""
    rawList = string.split()
    lettersList = []

    for x in rawList:
        lettersList.append(morse.get(x))

    messageTxt = ""
    for item in lettersList:
        messageTxt = messageTxt + item
    return messageTxt

def turnLetterToMorse(string):
    output = ""
    for c in string:
        c = str.lower(c)
        output = output + letterToMorse.get(c) + " "
    return output.strip()

def generateCodedString(all_the_file, dotDash):
    """This function is used in creating an encoded version of a raw text file. The function gets a raw text
       with no spaces, and return a text with spaces encoded in them.
       It loops to the end of the line and adds spaces based on the code (dotdash)"""

    i = 0 # Tracker of the second argument, dotDash. It's the string files with 0s and 1s in it.
    codedStr = ""

    for c in all_the_file:
        if (i >= len(dotDash)): #If no more code to encode, finish off the rest of the string
            codedStr = codedStr + c
            continue
        if (c != "\n"):
            codedStr = codedStr + c

        if (c == "\n"): # So if we were going to go to the next line, encode by putting 1 or 2 space(s)
            if (dotDash[i] == '0'):
                codedStr = codedStr + "  \n"
                i += 1
            elif (dotDash[i] == '1'): #Make sure it stays elif, wasted a lot of time debugging this because it was if
                codedStr = codedStr + " \n"
                i += 1
            elif (dotDash[i] == ' '):
                codedStr = codedStr + "\n"
                i += 1
            else:
                warnings.warn("Something went wrong in the encoding")
    return codedStr

def encodeMessage(secret_message, file_path, finalFileName):
    file_path = Path(file_path)
    morsedLetters = turnLetterToMorse(secret_message) #turns text into morse code in 0-1 format

    # Gets the file that contains the raw text
    with open(file_path, 'r') as raw_message:
        the_whole_file = raw_message.readlines()
        the_whole_file = str.join('', the_whole_file)
        #print("The whole file = ", the_whole_file +"\n The end -------")

    encoded = generateCodedString(the_whole_file, morsedLetters)
    #print(encoded)

    if (finalFileName == ''): # If the user didn't fill the filename box, just overwrite the original file
        finalFileName = file_path.name
        #add a clean function
    finalFileName = finalFileName + ".txt" #This can be changed later so the program saves this as another format
    with open(file_path.parent / finalFileName, 'w') as coded_msg:
        coded_msg.write(encoded)

def decode_message(file_path):

    fileDest = Path(file_path)

    with open(fileDest, 'r') as msg:
        zeString = ""
        for line in msg:
            zeString = zeString + determineDotDash(line)
        stringToLetter(zeString)
    return stringToLetter(zeString)





