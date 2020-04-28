def dic(s):
    count = {}
    s = s.lower()
    for char in s:
        count[char] = s.count(char)
    return count


print(dic(input("enter the name")))
