class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        fives , tens =  0,0
        for i in bills:
            if i == 5:
                fives+=1
            else:
                if i== 10:
                    tens+=1
                    fives-=1
                if i == 20:
                    if tens>0: 
                        tens -=1
                        fives-=1
                    else:
                        fives -=3
            if fives < 0 :
                return False
        return True

            

        