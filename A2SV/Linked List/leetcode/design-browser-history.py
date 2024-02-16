class Node:
    def __init__(self ,link ):
        self.link = link
        self.next = None
        self.prev =None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.current = Node( homepage)



        

    def visit(self, url: str) -> None:
        newUrl = Node(url)
        newUrl.prev = self.current
        self.current.next = newUrl
        self.current = newUrl 
        

    def back(self, steps: int) -> str:
       
        while self.current.prev and steps > 0 :
            self.current = self.current.prev
            steps-=1
        if self.current:
            return self.current.link
        

    def forward(self, steps: int) -> str:
        while self.current.next and steps > 0 :
            self.current = self.current.next
            steps-=1
        if self.current:
            return self.current.link

        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)