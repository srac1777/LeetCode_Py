class Solution:
    def twoSum_n2(self, nums, target): #n^2 complexity
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def twoSum(self, nums, target): # O(n)
        hash = {}
        for i in range(0, len(nums)):
            diff = target - nums[i]
            if diff in hash:
                return [i, hash[diff][1]]
            hash[nums[i]] = (target - nums[i], i)

sol = Solution().twoSum([3,3,5],8)
print(sol)

