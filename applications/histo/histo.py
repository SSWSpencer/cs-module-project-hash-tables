# Your code here
def removethings(s):
    s = s.strip('"')
    s = s.strip(':')
    s = s.strip(";")
    s = s.strip(",")
    s = s.strip(".")
    s = s.strip("-")
    s = s.strip("+")
    s = s.strip("=")
    s = s.strip("/")
    s = s.strip("\\")
    s = s.strip("|")
    s = s.strip("[")
    s = s.strip("]")
    s = s.strip("{")
    s = s.strip("}")
    s = s.strip("(")
    s = s.strip(")")
    s = s.strip("*")
    s = s.strip("^")
    s = s.strip("&")
    s = s.lower()
    return s

with open("robin.txt") as f:
    cache = {}
    words = f.read()
    words = words.split()
    for i in range(0, len(words)):
        words[i] = removethings(words[i])
        if words[i] not in cache:
            cache[words[i]] = "#"
        elif words[i] in cache:
            cache[words[i]] += "#"
    
    cache = {k: v for k, v in sorted(cache.items(), key=lambda item: item[1], reverse=True)}
    for key in cache:
        print(key, cache[key])
    