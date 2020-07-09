# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here


# Plan:
# 1: read the text
# 2: create a single string containing every letter (a-z) in the text
# 3: 

def removethings(s):
    s = s.replace('"', "")
    s = s.replace(':', "")
    s = s.replace(";", "")
    s = s.replace(",", "")
    s = s.replace(".", "")
    s = s.replace("-", "")
    s = s.replace("+", "")
    s = s.replace("=", "")
    s = s.replace("/", "")
    s = s.replace("\\" , "")
    s = s.replace("|", "")
    s = s.replace("[", "")
    s = s.replace("]", "")
    s = s.replace("{", "")
    s = s.replace("}", "")
    s = s.replace("(", "")
    s = s.replace(")", "")
    s = s.replace("*", "")
    s = s.replace("^", "")
    s = s.replace("&", "")
    s = s.replace("?", "")
    s = s.replace("'", "")
    s = s.replace("!", "")
    return s

with open("ciphertext.txt") as f:
    data = f.read()
    longstr = ""
    cache = {}

    for i in data: 
        for x in i:
            longstr+= x
    longstr = removethings(longstr)
    for i in range(0, len(longstr)):
        if longstr[i] not in cache:
            cache[longstr[i]] = 1
        elif longstr[i] in cache:
            cache[longstr[i]] = cache[longstr[i]] + 1

    cache = {k: v for k, v in sorted(cache.items(), key=lambda item: item[1], reverse=True)}

    print(cache)
    freqArr = []
    for key in cache:
        freqArr.append(key)

    print(freqArr)
    
    eRep = freqArr[1]
    tRep = freqArr[2]
    aRep = freqArr[3]
    oRep = freqArr[4]
    hRep = freqArr[5]
    nRep = freqArr[6]
    rRep = freqArr[7]
    iRep = freqArr[8]
    sRep = freqArr[9]
    dRep = freqArr[10]
    lRep = freqArr[11]
    wRep = freqArr[12]
    uRep = freqArr[13]
    gRep = freqArr[14]
    fRep = freqArr[15]
    bRep = freqArr[16]
    mRep = freqArr[17]
    yRep = freqArr[18]
    cRep = freqArr[19]
    pRep = freqArr[20]
    kRep = freqArr[21]
    vRep = freqArr[23]
    qRep = freqArr[24]
    jRep = freqArr[25]
    xRep = freqArr[26]
    zRep = freqArr[27]

    finalStr = ""
    for x in data:
        for i in x:
            if i == aRep:
                longstr+= "A"
            elif i == bRep:
                longstr+= "B"
            elif i == cRep:
                longstr+= "C"
            elif i == dRep:
                longstr+= "D"
            elif i == eRep:
                longstr+= "E"
            elif i == fRep:
                longstr+= "F"
            elif i == gRep:
                longstr+= "G"
            elif i == hRep:
                longstr+= "H"
            elif i == iRep:
                longstr+= "I"
            elif i == jRep:
                longstr+= "J"
            elif i == kRep:
                longstr+= "K"
            elif i == lRep:
                longstr+= "L"
            elif i == mRep:
                longstr+= "M"
            elif i == nRep:
                longstr+= "N"
            elif i == oRep:
                longstr+= "O"
            elif i == pRep:
                longstr+= "P"
            elif i == qRep:
                longstr+= "Q"
            elif i == rRep:
                longstr+= "R"
            elif i == sRep:
                longstr+= "S"
            elif i == tRep:
                longstr+= "T"
            elif i == uRep:
                longstr+= "U"
            elif i == vRep:
                longstr+= "V"
            elif i == wRep:
                longstr+= "W"
            elif i == xRep:
                longstr+= "X"
            elif i == yRep:
                longstr+= "Y"
            elif i == zRep:
                longstr+= "Z"
            else:
                longstr+= i
    print(longstr)
            
    