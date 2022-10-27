/* Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums.
If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity. 
Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
*/


int search(int* nums, int numsSize, int target){
    int first = 0; 
    int last = numsSize-1;
    int result = -1;
    while(first<=last){
        int middle=first + (last-first)/2;
        if (nums[middle]==target)
            return result=middle;
        if (nums[middle]<target)
            first=middle+1;
        else
            last=middle-1;
    }
    return result;
}
