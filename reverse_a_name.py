"""number = int(input("enter the number: "))
rev = 0
r = len(number)
digit = 1
for i in range(r):
    digit = number % 10
    rev = rev*10 + digit
    number = number//10
print("reverse of name is:", rev)"""


"""def rev_str(str):
    return str[-1::-1]


n = input("enter the name: ")
print("reverse of name is :", rev_str(n))"""

# using forloop:


def reverse_for_loop(str):
    s1 = ''
    for c in str:
        s1 = c+s1
    return s1


n = input("enter the name: ")
print("reverse of name is :", reverse_for_loop(n))
