x, y, z = [int(x) for x in input("Enter your date of birth: ").split('-')]
# print(f"{x}-{y}-{z}")input
# x = int(input("enter the number"))
total = 0
while (x != 0):
    total += int((x % 10))
    x = int(x/10)
print(total)
while (y != 0):
    total += int((y % 10))
    y = int(y/10)
# print(total)
while (z != 0):
    total += int((z % 10))
    z = int(z/10)
print(total)
