from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''nums.sort()
        result = 1
        tmp = 1
        for index in range (len(nums)-1):
            if nums[index] == nums[index + 1]:
                continue
            if nums[index] == nums[index + 1]-1:
                tmp += 1
            else:
                if tmp > result:
                    result = tmp
                    tmp = 1
        if tmp > result:
            result = tmp
        return result'''
        if len(nums) == 0:
            return 0
        numsSet = set(nums)
        result = 0
        for num in numsSet:
            if num - 1 not in numsSet:
                current_num = num
                sequence = 1
                while current_num + 1 in numsSet:
                    current_num = current_num + 1
                    sequence +=1
                result = max (result,sequence)
        return result
            




def test_longuestConsecutiveSequence():
    sol = Solution()

    assert sol.longestConsecutive([100,4,200,1,3,2]) == 4
    assert sol.longestConsecutive([0,0,1,2,3,4,7,400]) == 5
    assert sol.longestConsecutive([0,2,1,0]) == 3

if __name__ == "__main__":
    test_longuestConsecutiveSequence()
