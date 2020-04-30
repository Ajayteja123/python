def to_power(val, *nums):
    if len(nums) == 0:
        print("hey you didn't pass nums")
    else:
        li = [k**val for k in nums]
        print(li)


nums = [1, 3, 4]
to_power(3, *nums)
