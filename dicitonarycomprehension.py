def dic(s):
    count = {i: ('even' if i % 2 == 0 else 'odd') for i in range(s)}
    return count


print(dic(int(input("enter the nunber"))))
