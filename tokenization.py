
vowels =["a","e","i","o","u"]
punctuation = [",",":",";",'"',')','(',"/",'_',"-",'?','!','*',"[","]","#","@","`","~","$","%","^","&","â","€",'”',"ï","»","¿","˜"]
def tokenization(file):
    readFile = open(file,'r')
    tokenTxt = readFile.read().lower()
    readFile.close()

    #replaces punctuation with spaces. Removes special case periods. Allows for proper tokenization.
    for character in enumerate(tokenTxt):
        if character[0] > 1:
            if character[1] == '.' and tokenTxt[character[0]-2] != ' ' and tokenTxt[character[0]-2] != '.' and tokenTxt[character[0]-2] != '"':
                if not ((tokenTxt[character[0]-2] == 'm' and tokenTxt[character[0]-1] == 'r') or (tokenTxt[character[0]-3] == 'm' and tokenTxt[character[0]-2] == 'r' and tokenTxt[character[0]-1] == 's')):
                    tokenTxt = tokenTxt[:character[0]] + ' ' + tokenTxt[character[0] +1:] 
            if character[1] == "'":
                tokenTxt = tokenTxt[:character[0]] + tokenTxt[character[0] +1] + ' ' + tokenTxt[character[0] +2:]
        for punct in punctuation:
            if character[1] == punct:
                tokenTxt = tokenTxt[:character[0]] + ' ' + tokenTxt[character[0] +1:] 

    #handles "mr" and "mrs" titles and tokenizes string
    tokenTxt = tokenTxt.replace(".","").split()  

    readFile = open('stopwords.txt','r')
    stopwords = readFile.read().split()
    readFile.close()
    #removes stop words from list of tokens
    for stopword in stopwords:
        while stopword in tokenTxt:
            tokenTxt.remove(stopword)
    newTokenTxt = []
    #porter stemmer method
    for word in tokenTxt:
        length = len(word)
        check = False
        if word.endswith("sses"):
            word = word[:length - 2 ]
            newTokenTxt.append(word)
            continue
        elif word.endswith("ied") or word.endswith("ies"):
            if length > 4:
                word = word[:length - 3] + "i"
            else:
                word = word[:length - 3] + "ie"
            newTokenTxt.append(word)
            continue
        elif word.endswith("us") or word.endswith("ss"):
            newTokenTxt.append(word)
            continue
        for vowel in vowels:
            if (word.endswith("s")) and (vowel in word[:length - 1]) and (check == False):
                word = word[:length -1]
                check = True
        newTokenTxt.append(word)

    tokenTxt = []
    for word in newTokenTxt:
        nonVowelTracker = False
        vowelTracker = False
        if ("eedly" in word):
            location = word.find("eedly")
            subword = word[:location]
            for character in subword:
                for vowel in vowels:
                    if character != vowel and vowelTracker == True:
                        nonVowelTracker = True
                    if character == vowel:
                        vowelTracker = True
            
            if nonVowelTracker and vowelTracker:
                word = word[:location] + "ee" + word[location: +3]
                tokenTxt.append(word)
                continue
        if ("eed" in word):
            location = word.find("eed")
            subword = word[:location]
            for character in subword:
                for vowel in vowels:
                    if character != vowel and vowelTracker == True: 
                        nonVowelTracker = True
                    if character == vowel:
                        vowelTracker = True
            
            if nonVowelTracker and vowelTracker:
                word = word[:location] + "ee" + word[location: +3]
                tokenTxt.append(word)
                continue
        
        if"ingly" in word:
            location = word.find("ingly")
            subWord = word[:location]
            for character in subWord:
                for vowel in vowels:
                    if character == vowel:
                        vowelTracker = True
            if vowelTracker == True:
                word = subWord
                if (subWord[len(subWord) - 2:] == 'at' or subWord[len(subWord) - 2:] == 'bl' or subWord[len(subWord) - 2:] == 'iz'):
                    word = word + 'e'
                elif ((subWord[len(subWord)-1] + subWord[len(subWord)-2]) != "ll" and (subWord[len(subWord)-1] + subWord[len(subWord)-2]) and "ss"
                and (subWord[len(subWord)-1] + subWord[len(subWord)-2]) != "zz") and  (subWord[len(subWord)-1] == subWord[len(subWord)-2]) :
                    word = word[:location - 1]
                elif isShort(word):
                    word = word + 'e'
            tokenTxt.append(word)
            continue
        if"edly" in word:
            location = word.find("edly")
            subWord = word[:location]
            for character in subWord:
                for vowel in vowels:
                    if character == vowel:
                        vowelTracker = True
            if vowelTracker == True:
                word = subWord
                if subWord[len(subWord) - 2:] == 'at' or subWord[len(subWord) - 2:] == 'bl' or subWord[len(subWord) - 2:] == 'iz': 
                    word = word + 'e'
                elif ((subWord[len(subWord)-1] + subWord[len(subWord)-2]) != "ll" and (subWord[len(subWord)-1] + subWord[len(subWord)-2]) and "ss"
                and (subWord[len(subWord)-1] + subWord[len(subWord)-2]) != "zz") and  (subWord[len(subWord)-1] == subWord[len(subWord)-2]) :
                    word = word[:location - 1]
                elif isShort(word):
                    word = word + 'e'
            tokenTxt.append(word)
            continue

        if"ing" in word:
            location = word.find("ing")
            subWord = word[:location]
            for character in subWord:
                for vowel in vowels:
                    if character == vowel:
                        vowelTracker = True
            if vowelTracker == True:
                word = subWord
                if (subWord[len(subWord) - 2:] == 'at' or subWord[len(subWord) - 2:] == 'bl' or subWord[len(subWord) - 2:] == 'iz') : 
                    word = word +'e'
                elif ((subWord[len(subWord)-1] + subWord[len(subWord)-2]) != "ll" and (subWord[len(subWord)-1] + subWord[len(subWord)-2]) and "ss"
                and (subWord[len(subWord)-1] + subWord[len(subWord)-2]) != "zz") and  (subWord[len(subWord)-1] == subWord[len(subWord)-2]) :
                    word = word[:location - 1]
                elif isShort(word):
                    word = word + 'e'
            tokenTxt.append(word)
            continue
        if "ed" in word:
            location = word.find("ed")
            subWord = word[:location]
            for character in subWord:
                for vowel in vowels:
                    if character == vowel:
                        vowelTracker = True
            if vowelTracker == True:
                word = subWord
                if subWord[len(subWord) - 2:] == 'at' or subWord[len(subWord) - 2:] == 'bl' or subWord[len(subWord) - 2:] == 'iz':
                    word = word + 'e'
                elif ((subWord[len(subWord)-1] + subWord[len(subWord)-2]) != "ll" and (subWord[len(subWord)-1] + subWord[len(subWord)-2]) and "ss"
                and (subWord[len(subWord)-1] + subWord[len(subWord)-2]) != "zz") and  (subWord[len(subWord)-1] == subWord[len(subWord)-2]) :
                    word = word[:location - 1]
                elif isShort(word):
                    word = word + 'e'
            tokenTxt.append(word)
            continue
        tokenTxt.append(word)

    if(file == 'tokenization-input-part-A.txt' ):
        writeFile = open('tokenized-A.txt','w+')
        for token in tokenTxt:
            writeFile.write(token + "\n")
            writeFile.close()
    elif(file == 'tokenization-input-part-B.txt'):
        termCounter(tokenTxt)
              

#helper function for Porter-stemmer           
def isShort(word):
    combos = ["cvcv","cvc","vcv","vc"]
    tracker = ''
    for letter in word:
        if letter not in vowels and not tracker:
            tracker += 'c'
        elif letter not in vowels and tracker[len(tracker) - 1] != 'c':
            tracker += 'c'
        if letter in vowels and not tracker:
            tracker += 'v'
        elif letter in vowels and tracker[len(tracker) - 1] != 'v':
            tracker += 'v'
    if tracker in combos:
        return True
    else:
        return False

def termCounter(tokens):
    writeFile = open('terms-B.txt','w+')
    tempStr = ""
    countDict ={}
    tkns = list(set(tokens))
    for term in tkns:
        count = 0
        for token in tokens:
            if term == token:
                count += 1
        countDict[term] = count
    sortedList = sorted(countDict, key = countDict.get, reverse=True)
    i = 0
    for token in sortedList:
        if i < 300:
            count = countDict[token]
            tempStr += token + " " + str(count) + '\n'
            i += 1
        else:
            continue
    writeFile.write(tempStr)
    writeFile.close()


tokenization('tokenization-input-part-B.txt')