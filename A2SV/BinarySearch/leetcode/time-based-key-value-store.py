class TimeMap:

    def __init__(self):
        self.mymap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.mymap[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.mymap:
            return ""
        else:
            return self.search(self.mymap[key],timestamp)
            
    def search(self ,arr,time):
        left , right = -1 , len(arr)
        while right - left > 1:
            mid = (right + left) // 2
            if arr[mid][1] <= time:
                left = mid
            else:
                right = mid
        return "" if left == -1 or arr[left][1] > time else arr[left][0]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)