# syntax: x, y=[xforxininput("Enter two value: ").split()]


x, y = [x for x in input("Enter your name and age: ").split(",")]
print("Your name is: ", x)
print("Your age is: ", y)


"""output:
Enter your name and age: ajay,19
Your name is:  ajay
Your age is:  19"""
