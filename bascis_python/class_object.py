class Car:
     # set the data to private __ attribute
   
    def __init__(self,brand,model):
      self.__brand=brand
      self.__model=brand
      
    def data(self):
        print(self.__brand,self.__model)
my_car=Car("BMW","X5")
my_car.data()
# using constructor
class Bike:
    def __init__(self,brand,model):
       self.brand=brand
       self.model=model
       
    def show_data(self):
        print(self.brand,self.model)
        
B1=Bike("Boolet","X4")
B1.show_data()

# inharitance

class Electric_car(Car):
    total_call=0
    __name=None
    def __init__(self,brand,model,name):
        super().__init__(brand,model)
        self.__name=name
        Electric_car.total_call+=1
        
    def show_data2(self):
        print(self.name,self.brand,self.model)
        
    @staticmethod 
    def description():
        return "This is description method"
        
tesla=Electric_car("Tata","X5","Nexon")
Nexon=Electric_car("Tata","X5","Nexon")
# print(Electric_car.total_call)
print(Nexon.description())  # static method do not take self reference

# isintance method to cheak which instance onject is
print(isinstance(tesla,Electric_car))
print(isinstance(Nexon,Car))

# multiple inharitance
class Bettery:
    def show_bettery(self):
        return "This is Bettery class"
    
class Engine:
    def show_engine(self):
        return "This is Engine class"
    
class MyCar(Engine,Bettery):
    def __init__(self,name):
        self.__name=name
    def show_name(self):
        return f"My car name is {self.__name}"
    
c=MyCar("Thar")
print(c.show_engine())
print(c.show_bettery())
print(c.show_name())