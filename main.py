str = [0]

def rec(depth):
    if depth == 5:
        return
    for i in range(len(str)):
        if(str[i] == 0):
            del str[i]
            str.insert(i, 0)
            str.insert(i, 3)#]
            str.insert(i, 0)
            str.insert(i, 2)#[
            str.insert(i, 1)
            i+=4
        elif(str[i] == 1):
            del str[i]
            str.insert(i, 1)
            str.insert(i, 1)
            i+=1
    print(str)
    rec(depth+1)

rec(0)