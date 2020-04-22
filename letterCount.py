x = input("enter the name: ")
print("user's name", len(x))
x = x.lower()
#new_list = list(set(x))
# print(new_list)
for c in x:
    print(f"{c}is{x.count(c)}")
