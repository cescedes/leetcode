# Given an array, rotate the array to the right by k steps, where k is non-negative. 
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        if k>n:
            k=int(k%n)
        nums[:]=nums[-k:]+nums[:-k]
