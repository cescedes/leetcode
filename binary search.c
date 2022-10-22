/* Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums.
If target exists, then return its index. Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity. */


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
