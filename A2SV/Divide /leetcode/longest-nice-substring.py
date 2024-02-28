class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        arr = []
        
        def my(str):
            if not str :
                return ""
            myset =  set(str)
            for i, ch in enumerate(str):
                if ch.swapcase() not in str:
                    first = my(str[:i])
                    second = my(str[i+1:])
                    return first if len(first) >= len(second) else second
            return str
        return my(s)
        