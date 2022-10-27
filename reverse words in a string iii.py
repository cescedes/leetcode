#Given a string s, reverse the order of characters in each word within
#a sentence while still preserving whitespace and initial word order.
#Input: s = "Let's take LeetCode contest"
#Output: "s'teL ekat edoCteeL tsetnoc"

class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.split(" ")
        new_words=[word[::-1] for word in words]
        new_s=" ".join(new_words)
        return new_s
