/* Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity. 
Input: nums = [1,3,5,6], target = 5
Output: 2
*/

int searchInsert(int nums[], int numsSize, int target){
    for (int i=0;i<numsSize;i++)
        if(nums[i]==target)
            return i;
        else if (nums[i]>target)
            return i;
    return numsSize;
}
