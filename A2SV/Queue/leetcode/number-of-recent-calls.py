class RecentCounter:

    def __init__(self):
        self.head= 0
        self.requests=[]
        

    def ping(self, t: int) -> int:
        self.requests.append(t)
        ans = 0
        while t -  self.requests[self.head] > 3000:
            self.head+=1
        return len(self.requests) - self.head
        

        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)