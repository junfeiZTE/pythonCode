class Calculator:
    name="Good Calculator!!"
    price=18
    def __init__(self,hight,width,weight,length=30):
        self.hight=hight
        self.width=width
        self.weight=weight
        self.length=length
    def add(self,x,y):
        print(self.name)
        print(x+y)
    def info(self):
        print(self.hight,self.width,self.weight)
