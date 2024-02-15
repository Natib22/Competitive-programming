from typing import List

class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        myarray = []
        for i in range(len(names)):
            myarray.append([heights[i], names[i]])
        myarray.sort(reverse=True)
        people = []
        for i in myarray:
            people.append(i[1])
        return people


        