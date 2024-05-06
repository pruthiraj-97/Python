#Transpose
def Transponse(list):
    for i in range(0,len(list)):
      for j in range(i,len(list[0])):
        temp=list[i][j]
        list[i][j]=list[j][i]
        list[j][i]=temp
    
list=[[1,2,3],[4,5,6],[7,8,9]]
print(list)
Transponse(list)
print(list)


