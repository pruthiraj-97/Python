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
def cacheing(func):
    cache={}
    def wrapper(*args):
        if(args in cache):
            return cache[args]
        result=func(*args)
        cache[args]=result
        return cache[args]
        
    return wrapper

@cacheing
def cacheingCheak(a,b):
    time.sleep(3)
    return a+b

print(cacheingCheak(3,4))
print(cacheingCheak(3,4))

