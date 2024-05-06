class employ:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def showData(self):
        print(self.name,self.age,self.salary)
        

e1=employ("sunny",23,20000)
#e1.showData()

class owner(employ):
    def __init__(self,name,age,salary,networth):
        super().__init__(name,age,salary)
        self.networth=networth
        
    def showData(self):
        print(self.name,self.age,self.salary,self.networth)
        

o1=owner("sunny",23,20000,50000)
o1.showData()