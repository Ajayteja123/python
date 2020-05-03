# def average(l):
#     num = []
#     l1, l2, l3 = zip(*l)
#     # print(l1)
#     total = 0
#     for i in l1:
#         total = total+i
#     # print(int(total)/3)
#     ram = 0
#     for j in l2:
#         ram = ram+j
#     # print(int(ram)/3)
#     aj = 0
#     for k in l3:
#         aj = aj+k
#     # print(int(aj)/3)
#     num.append(int(aj)//3)
#     num.append(int(ram)//3)
#     num.append(int(total)//3)
#     print(num)
#     # for i in zip(args):


# average([[1, 2, 3], [1, 4, 5], [2, 3, 5]])
def average_finder(l1, l2):
    average = []
    for pair in zip(l1, l2):
        average.append(sum(pair)/len(pair))
    return average


print(average_finder([1, 2, 3], [1, 2, 3]))
