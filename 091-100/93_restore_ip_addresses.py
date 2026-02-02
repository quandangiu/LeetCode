class Solution:
    def restoreIpAddresses(self, s):
        result = []
        
        def backtrack(start, path):
            if len(path) == 4:
                if start == len(s):
                    result.append('.'.join(path))
                return
            
            for i in range(start, min(start + 3, len(s))):
                segment = s[start:i+1]
                if (segment[0] != '0' or len(segment) == 1) and int(segment) <= 255:
                    backtrack(i + 1, path + [segment])
        
        backtrack(0, [])
        return result
