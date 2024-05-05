#Decorators
import time
def Timmer(func):
    def wrapper(*args, **kwargs):
       start = time.time()
       result = func(*args, **kwargs)
       end = time.time()
       print(f"{func.__name__} took {end - start} seconds")
       return result 
    return wrapper

@Timmer
def cheakFunction(n,m):
    return n+m

ans=cheakFunction(2,3)
print(ans)

#cacheing the arguments
