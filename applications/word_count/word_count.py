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

def word_count(s):
    # Your code here
    cache = {}
    arr = s.split()
    for i in range(0, len(arr)):
        arr[i] = removethings(arr[i])
        if len(arr[i]) > 0:
            if arr[i] not in cache:
                cache[arr[i]] = 1
            elif arr[i] in cache:
                cache[arr[i]] = cache[arr[i]] + 1
    return cache



if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
    print(word_count('":;,.-+=/\\|[]{}()*^&'))