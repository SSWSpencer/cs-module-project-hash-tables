import random

# Read in all the words in one go
with open("input.txt") as f:
    startWords = {}
    stopWords = {}
    otherWords = {}
    words = f.read()
    words = words.split()
    # TODO: analyze which words can follow other words
# Your code here
    for i in words:
        if "(" not in i and ")" not in i and ":" not in i and '"' not in i and i[0] != "'" and i[len(i)-1] != "'":
            if i[0].isupper():
                if i not in startWords and i[len(i)-1] != "." and i[len(i)-1] != "!" and i[len(i)-1] != "?":
                    startWords[i] = 1
                elif i in startWords:
                    startWords[i] += 1
            elif i[len(i)-1] == "." or i[len(i)-1] == "!" or i[len(i)-1] == "?":
                if i not in stopWords:
                    stopWords[i] = 1
                elif i in stopWords:
                    stopWords[i] += 1
            else:
                if i not in otherWords:
                    otherWords[i] = 1
                elif i in otherWords:
                    otherWords[i] += 1

    print(f"------ START WORDS -------" ) 
    print(startWords)
    print(f"------ STOP WORDS -------")
    print(stopWords)
    print(f"------ OTHER WORDS -------")
    print(otherWords)



# TODO: construct 5 random sentences
# Your code here
print("----------------------------RANDOM SENTENCES----------------------------")
counter = 1
while counter < 6:
    print(f"Sentence #{counter}:")
    sentence = ""

    # adds the beginning word to the sentence
    startList = list(startWords.keys())
    startWord = random.choice(startList)
    sentence+= startWord + " "
    
    # generates a random length for the sentence and adds the middle words
    wordCount = random.randint(4, 10)
    for x in range(0, wordCount):
        midList = list(otherWords.keys())
        midWord = random.choice(midList)
        sentence+= midWord + " "
    
    stopList = list(stopWords.keys())
    stopWord = random.choice(stopList)
    sentence+= stopWord

    print(sentence) 
    print()
    counter+= 1