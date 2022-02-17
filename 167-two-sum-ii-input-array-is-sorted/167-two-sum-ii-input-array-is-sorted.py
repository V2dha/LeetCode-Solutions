"""
1. Maintain two pointers one for left and one for right
2. Calculate the temp_sum = left + right
    2.1 if temp_sum == target -> return [left+1, right+1]
    2.2 elif temp_sum > target -> right -= 1
    2.3 elif temp_sum < target -> left += 1
Time Complexity = O(N)
Space Compleixty = O(1)
"""
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        while left < right:
            temp_sum = numbers[left] + numbers[right] 
            if temp_sum < target:
                left += 1
            elif temp_sum > target:
                right -= 1
            else:
                return [left+1, right+1]
        