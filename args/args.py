def all_toatal(*args):
    total = 0
    for num in args:
        total += num
    return total


#n = int(input("enter the numbers: ")).split()
n = int(input("Enter number of elements : "))
nums = []
# iterating till the range
for i in range(0, n):
    ele = int(input())

    nums.append(ele)
print(all_toatal(*nums))
