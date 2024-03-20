class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        arr = []
        for i in range(len(weights)-1):
            arr.append(weights[i] + weights[i+1])
        arr.sort()
        mymax = mymin = weights[0] + weights[-1]
        for i in range(k-1):
            mymax+= arr[len(arr)-1-i]
            mymin+= arr[i]
        return mymax - mymin


        