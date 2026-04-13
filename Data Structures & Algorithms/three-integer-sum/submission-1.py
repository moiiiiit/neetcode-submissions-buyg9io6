class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        solutions=set()
        for index, number in enumerate(nums):
            target = number
            hash_map = {}
            for idx, num in enumerate(nums[:index]+nums[index+1:]):
                if -(target + num) in hash_map:
                    solutions.add(tuple(sorted([-(target+num), num, number])))
                hash_map[num] = idx
        return list(solutions)