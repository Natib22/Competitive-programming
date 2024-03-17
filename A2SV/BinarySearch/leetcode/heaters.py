class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        minPos = min(houses)
        maxPos = max(houses)
        noHeat = len(heaters)
        noHouse = len(houses)
        houses.sort()
        heaters.sort()
        left ,right = -1 , max(maxPos - minPos + 1 ,  max(heaters)- minPos + 1 )
        def cover(radius):
            index1 , index2 = 0 , 0
            while index1 < noHouse:
                if index2 >= noHeat:
                    return False
                backward,forward = heaters[index2] - radius , heaters[index2] + radius

                if houses[index1] < backward:
                    return False
                if houses[index1] > forward:
                    index2+=1
                else:
                    index1+=1
            return True


        while right - left > 1:
            mid = (right + left) // 2
            if cover(mid):
                right = mid
            else:
                left = mid
        return right

        