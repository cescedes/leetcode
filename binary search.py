#Given an array of integers nums which is sorted in ascending order, and an integer target, 
#write a function to search target in nums. If target exists, then return its index.
#Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        first=0
        last=len(nums)-1
        middle=0
        
        while first <=last:
            middle=(first+last)//2
            
            if nums[middle]<target:
                first=middle+1
            elif nums[middle]>target:
                last=middle-1
            else:
                return middle
        return -1
