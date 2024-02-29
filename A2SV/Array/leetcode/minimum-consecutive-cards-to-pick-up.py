class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        mymap = {}
        ans = len(cards)
        flag = False
        for ind, val in enumerate(cards):
            if val in mymap:
                flag = True
                ans = min(ans, ind - mymap[val] +1)
            mymap[val] = ind
        return ans if flag else -1

        