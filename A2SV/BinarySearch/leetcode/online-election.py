class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.mymap = defaultdict(int)
        self.votes = []
        self.persons = persons
        self.times = times
        mymax = -1
        curr = self.persons[0]
        for i in self.persons:
            self.mymap[i]+=1
            if self.mymap[i]>= mymax:
                
                mymax = self.mymap[i]
                curr = i
            self.votes.append(curr)
  
            
            


        


    def q(self, t: int) -> int:
        
        def search(t):
            left , right = -1 , len(self.times)
            while right - left > 1:
                mid = (right + left)//2
                if   self.times[mid]<= t:
                    left = mid
                else:
                    right = mid
            return left
        index = search(t)
        return self.votes[index]



        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)