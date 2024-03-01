class Solution:
    def decodeString(self, s: str) -> str:
        ans = []

        def my(idx):
            num = 0
            temp = []
            while idx < len(s):
                if s[idx].isdigit():
                    num = num * 10 + int(s[idx])
                elif s[idx] == "[":
                    idx , decode = my(idx+1)
                    temp.append (num * decode)
                    num = 0
                elif s[idx] == "]":
                    return idx ,"".join(temp)
                else:
                    temp.append(s[idx])
                idx+=1
            return idx, "".join(temp)

        return my(0)[1]
                
        