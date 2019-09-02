# Lab 1 OS
# Author: Brian A. Cardiel
d = dict()
final = dict()
word2 = ""
word2Checker = 2
inputFile = input("Enter Input File name\n")
OutputFile = input("Enter Output File name\n")


def creator():
    global word2Checker
    global  word2
    text = open(inputFile, "r")

    for line in text:
        line = line.strip()
        line = line.lower()
        # Split into words
        words = line.split(" ")

        # Iterate over each word in line
        for word in words:
            # Check if the word is already in dictionary
            if len(word) > 0: # removes white space
                word = checkWord(word)
                #special case for word2
                if(word2Checker == 1):
                    word2Checker = 2
                    word2 = checkWord(word2)
                    if word2 in d:
                        # Increment count of word by 1
                        d[word2] = d[word2] + 1
                    else:
                        # Add the word to dictionary with count 1
                        d[word2] = 1
                 #normal
                if word in d:
                    # Increment count of word by 1
                    d[word] = d[word] + 1
                else:
                    # Add the word to dictionary with count 1
                    d[word] = 1
#cleans words
def checkWord(word):
    global word2Checker
    global word2
    count = 0
    for x in word:
        if x.isalpha() == False and len(word) > 1:
            word2 = word[count+1:len(word)]
            word = word[0:count]
            #filter word2
            if(len(word2)>0 and word2 != ' '):
                word2Checker = 1
            return word
        count+=1
    return word


def sorter():
    for key, value in sorted(d.items()):
        if key.isalpha():
            final[key] = d[key]

def fileWritter():
    f = open(OutputFile, "a")
    for x in final:
        f.write(str(x))
        f.write(' ')
        f.write(str(final[x]))
        f.write('\n')

def fileReader():
    f = open(OutputFile, "r")
    print(f.read())

creator()
sorter()
fileWritter()
fileReader()