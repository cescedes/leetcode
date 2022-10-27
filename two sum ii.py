#Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
#find two numbers such that they add up to a specific target number.
#Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
#Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.
#The tests are generated such that there is exactly one solution. You may not use the same element twice.
#Your solution must use only constant extra space.
#Input: numbers = [2,7,11,15], target = 9
#Output: [1,2]
#Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        first_index = 0
        second_index = n-1

        while first_index < second_index:
            first_value = numbers[first_index]
            second_value = numbers[second_index]
            the_sum = first_value + second_value
            if the_sum == target:
                return [first_index + 1, second_index + 1]
            elif the_sum < target:
                first_index += 1
            else:
                second_index -= 1
