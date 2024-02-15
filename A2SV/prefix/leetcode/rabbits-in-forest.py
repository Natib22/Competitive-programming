class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        mymap= {}
        rabbits = 0
        for rabbit in answers:
            mymap[rabbit] = 1 + mymap.get(rabbit,0)
   
        for key , value in mymap.items():
            key+=1
            if key  >= value :
                rabbits+= key
            else:
                rabbits+= (key) *(value // key)
                if value % key != 0:
                    rabbits+= key 
        return rabbits
        

        