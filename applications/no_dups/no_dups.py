def no_dups(s):
    # Your code here
    arr= s.split(" ")
    newarr = list(dict.fromkeys(arr))
    output = ""
    for i in range(0, len(newarr)-1):
        output+=newarr[i] + " "
    output+=newarr[len(newarr)-1]
    return output

if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))