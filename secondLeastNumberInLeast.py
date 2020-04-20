def asort(arr,n):
    j= 0
    for i in range(0,n-1):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                temp=arr[j]
                arr[j]=arr[j+1]
                arr[j+1]=temp
#main
n = int(input("enter th number of elements"))
arr = [ ]
for i in range(n):
   temp = input()
   arr.append(temp)
asort(arr,n)
print(arr[1])