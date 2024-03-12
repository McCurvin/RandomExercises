def countSmallNum(nums):
    smallerCounts = []
    for digit in range(len(nums)):
        count = sum(num < nums[digit] for j, num in enumerate(nums) if j != digit)
        smallerCounts.append(count)

    return smallerCounts

N = int(input("Enter the number of elements: "))
nums = []
print(f"Enter {N} integers:")
for _ in range(N):
    num = int(input(f""))
    nums.append(num)

smaller_counts = countSmallNum(nums)
print(f"Result: {smaller_counts}")

