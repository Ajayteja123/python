# syntax new_list=[expression for item in iteratable object if_statment]
# syntax if..else: new_list=[expr if_statment else expression for item in iterable object]
# nested for loop: new_list=[[expression for j in range(4,7) for i in range(6,8)]]
#                                        (inner loop)          (outer loop)
x = int(input())
y = int(input())
z = int(input())
n = int(input())
print([[a, b, c] for a in range(0, x+1) for b in range(0, y+1)
       for c in range(0, z+1) if a + b + c != n])

# output:
"""2
2
2
2
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1], [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2], [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2], [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1], [2, 2, 2]]"""
