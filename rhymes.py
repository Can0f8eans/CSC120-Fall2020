def compare_front(linear1, linear2):
    retVal = 0
    assert type(linear1) == type(linear2)
    if len(linear1) > len(linear2):
        for i in range(len(linear2)):
            if linear1[i] == linear2[i]:
                retVal += 1
            else:
                return retVal
        return retVal
    elif len(linear1) < len(linear2):
        for i in range(len(linear1)):
            if linear1[i] == linear2[i]:
                retVal += 1
            else:
                return retVal
        return retVal
    elif len(linear2) == 0 or len(linear1) == 0:
        return retVal
    else:
        for i in range(len(linear1)):
            if linear1[i] == linear2[i]:
                retVal += 1
            else:
                return retVal
        return retVal

def compare_back(linear1, linear2):
    retVal = 0
    stressVal = True
    assert type(linear1) == type(linear2)
    if len(linear1) > len(linear2):
        for i in reversed(range(len(linear2))):
            lenDiff = len(linear1) - len(linear2)
            if linear1[i + lenDiff] == linear2[i]:
                retVal += 1
            else:
                return retVal
        return retVal
    elif len(linear1) < len(linear2):
        for i in reversed(range(len(linear1))):
            lenDiff = len(linear2) - len(linear1)
            if linear1[i] == linear2[i+lenDiff]:
                retVal += 1
            else:
                return retVal
        return retVal
    elif len(linear2) == 0 or len(linear1) == 0:
        return retVal
    else:
        for i in reversed(range(len(linear1))):
            if linear1[i] == linear2[i]:
                retVal += 1
            else:
                return retVal
        return retVal

def primary_stress(phonemesList):
    assert type(phonemesList) == list
    assert len(phonemesList) != 0
    for i in phonemesList:
        assert type(i) == str
        assert len(i) != 0
    for i in phonemesList:
        for char in i:
            if char == '1':
                return i
    return None

import sys
wordDict = {}
fileName = input()
dictionary = open(fileName.strip())

for line in dictionary.readlines():
    splitLine = line.split()
    wordDict[splitLine[0]] = splitLine[1:]
for line in sys.stdin:
    wordString = line.strip()
    if wordString == "" or wordString == " " or wordString == "\n":
        print("No word given.")
    elif len(wordString.split()) > 1:
        print("Multiple words entered, please enter only one word at a time")
    else:
        wordString = wordString.upper()
        rhymeList = []
        if wordString in wordDict:
            for entry in wordDict:
                rhyme = True
                stressVal1 = primary_stress(wordDict[entry])
                stressVal2 = primary_stress(wordDict[wordString])
                compareValue = compare_back(wordDict[wordString],wordDict[entry])
                entryList = wordDict[entry]
                if stressVal1 != stressVal2:
                    rhyme = False
                counter = 0
                for phenome in entryList[-compareValue:]:
                    if phenome == stressVal2:
                        rhyme = True
                        break
                    else:
                        rhyme = False
                if compareValue > 1 and entry != wordString:
                    if rhyme:
                     #   if len(wordDict[wordString]) != compareValue or len(wordDict[entry]) != compareValue:
                        rhymeList.append(entry)
            if len(rhymeList) == 0:
                print("-- none found --")
            else:
                print("Rhymes for:", wordString)
                for i in rhymeList:
                    print("\t", i)
                print()
        else:
            print("-- word not found --")