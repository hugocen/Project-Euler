result = 2
nums = [1, 2]
while nums[1] < 4000000:
    new_fib = nums[0] + nums[1]
    nums[0], nums[1] = nums[1], new_fib
    if new_fib % 2 == 0:
        result += new_fib
print(result)
