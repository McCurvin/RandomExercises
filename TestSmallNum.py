#How Many Numbers Are Smaller Than the Current Number
def smallerNums(nums):
    smaller_digits = []
    for i in range(len(nums)):
        count = sum(num < nums[i] for j, num in enumerate(nums) if j != i) #j is index, num is value, then nums[i] goes over every iterable in the list nums
        smaller_digits.append(count)

    return  smaller_digits



N = int(input("Enter the number of elements: "))
nums = []

print(f"Enter {N} integers:")
for ii in range(N):
    num = int(input(f"{ii}"))
    nums.append(num)

result = smallerNums(nums)
print(f"Result: {nums}")




