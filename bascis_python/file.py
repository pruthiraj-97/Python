# f1=open('text.txt','w')
# f1.close()
f1=open('text.txt','w')
f1.write("hello i am a full stack and devlops engineer and i am learning python")
f1.close()
f2=open('text.txt','r')
data=f2.read()
print(type(data)) # str