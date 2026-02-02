class Solution:
    def lengthOfLastWord(self, s):
        s = s.rstrip()
        return len(s.split()[-1]) if s else 0
