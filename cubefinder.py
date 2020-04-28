def cubefinder(n):
    dic = {}
    for i in range(1, n+1):
        dic[i] = i**3
    return dic


print(cubefinder(int(input("enter the number"))))
