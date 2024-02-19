class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        iceCreams = 0
        i = 0
        while coins > 0 and i  <len(costs):
            if costs[i] <= coins:
                iceCreams+=1
                coins-=costs[i]
            i+=1
        return iceCreams

        