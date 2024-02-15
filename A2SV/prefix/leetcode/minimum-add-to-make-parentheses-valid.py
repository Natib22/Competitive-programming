class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        myarray = []
        for i in s:
            if i == ")" and myarray and myarray[-1] == "(":
                myarray.pop()
            else:
                myarray.append(i)
        return len(myarray)

        