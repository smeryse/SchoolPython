def count_price(nums):
    result = []
    for i in range(len(nums) // 2):
        result.extend([nums[i] * i, nums[-i] * i])
    result.append((len(nums) // 2 * nums[len(nums) // 2]))
    return sum(result)

nums = [int(i) for i in open('27-99a.txt')][1:]
prices = []
for i in range(len(nums)):
    prices.append(count_price(nums[i:i] + nums[i:]))

print(prices)