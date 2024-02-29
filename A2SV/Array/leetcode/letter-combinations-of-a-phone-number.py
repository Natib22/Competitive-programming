class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mymap = {
            "2" :['a', 'b' , 'c'],
            "3":[ 'd', 'e', 'f'] ,
            "4":['g' , 'h' , 'i'],
            "5":['j' , 'k' , 'l'],
            "6":['m' , 'n' , 'o'],
            "7":['p' ,'q' , 'r' , 's' ],
            "8":['t' , 'u' , 'v'],
            "9":['w', 'x' ,'y' , 'z' ],

        }
        if not digits:
            return []
        ans = []
        def my(j , path):
            if len(path) == len(digits):
                ans.append("".join(path[:]))
                return
            
            for i in range(len(mymap[digits[j]])):
                path.append(mymap[digits[j]][i])
                my(j+1,path)
                path.pop()
        my(0,[])
        return ans



        