#Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        test = ""
        maxLength = -1
        if (len(s)==0):
            return 0
        elif (len(s)==1):
            return 1
        for i in list(s):
            current = "".join(i)

            if (current in test):
                test = test[test.index(current) + 1:]

            test = test + "".join(i)

            maxLength = max(len(test), maxLength)

        return maxLength
