n= int(input("enter the number:"))
for i in range(n):
  print(' '*(n-i-1)+(str(i+1)+' ')*(i+1))
for i in range(n):
  print(' '*(i)+(str(n-i)+' ')*(n-i))