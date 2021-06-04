class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashTable = {}

        for i in range(len(nums)):
            complement = target - nums[i]
            if (complement in hashTable) and hashTable[complement] != i:
                return[i,hashTable[complement]]

            hashTable[nums[i]]=i
