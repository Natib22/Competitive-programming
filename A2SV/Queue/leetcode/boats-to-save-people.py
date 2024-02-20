class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ans = 0 
        people.sort()
        left , right  =  0 , len(people) -1
        while left<=right:
            if people[right]  + people[left] <= limit :
                ans+=1
                right-=1
                left+=1
            elif people[right] <= limit:
                ans+=1
                right-=1
            else:
                if people[left] <= limit:
                    ans+=1
                    left+=1

        return ans
        