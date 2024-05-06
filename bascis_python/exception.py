
try:
    def division(a,b):
       return (a+b)/(a-b)
    
    print(division(2))
except ZeroDivisionError:
    print("Error due to division by zero",ZeroDivisionError)
    
except ArithmeticError:
    print("Error due to division by zero",ArithmeticError)
    
except NameError:
    print("Error due to variable not defined",NameError)
    
finally:
    print('This is always executed')