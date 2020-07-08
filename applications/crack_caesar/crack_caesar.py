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

with open("ciphertext.txt") as inp:
    data = set(inp.read().split())
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
    
    eRep = freqArr[0]
    tRep = freqArr[1]
    aRep = freqArr[2]
    oRep = freqArr[3]
    hRep = freqArr[4]
    nRep = freqArr[5]
    rRep = freqArr[6]
    iRep = freqArr[7]
    sRep = freqArr[8]
    dRep = freqArr[9]
    lRep = freqArr[10]
    wRep = freqArr[11]
    uRep = freqArr[12]
    gRep = freqArr[13]
    fRep = freqArr[14]
    bRep = freqArr[15]
    mRep = freqArr[16]
    yRep = freqArr[17]
    cRep = freqArr[18]
    pRep = freqArr[19]
    kRep = freqArr[20]
    vRep = freqArr[21]
    qRep = freqArr[22]
    jRep = freqArr[23]
    xRep = freqArr[24]
    zRep = freqArr[25]

    finalStr = ""
    for x in data:
        finalStr+= x + " "
    finalStr.replace(aRep, "A")
    finalStr.replace(eRep, "E")
    finalStr.replace(iRep, "I")
    finalStr.replace(oRep, "O")
    finalStr.replace(uRep, "U")
    finalStr.replace(yRep, "Y")
    
    print(finalStr)