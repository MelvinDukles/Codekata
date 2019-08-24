str = input()
l = len(str)
p = l-1
index = 0
while index < p:
    if str[index] == str[p]:
        index = index + 1
        p = p-1
        if index == p or index + 1 == p:
            print("YES")
            break
    else:
        print("NO")
        break
