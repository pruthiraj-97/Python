# f1=open('text.txt','w')
# f1.close()
# f1=open('text.txt','w')
# f1.write("hello i am a full stack and devlops engineer and i am learning python")
# f1.close()
# f2=open('text.txt','r')
# data=f2.read()
# print(type(data)) # str
# f2=open('text.txt','r')
# data=f2.readline()
# list=data.split(' ')
# print(list)
# print(f2.readline())
# print(f2.readline())
# f3=open('file.txt','w')
# with open('text.txt', 'r') as file: #itercate to extact all lines
#     lines = file.readlines()

# # Now lines contains all the lines from the file
# #total lines in the file
# print("Total lines are ",len(lines))
# for i in range(0,len(lines)):
#     if(i%2==0):
#         f3.write(lines[i])

# f3.close()
list=[]
class student:
  def __init__(self):
      self.student_list=[]
      
  def create_student(self,name,rollnumber,python,javascript):
      new_student={
          name:name,
          rollnumber:rollnumber,
          python:python,
          javascript:javascript
      }
      self.student_list.append(new_student)
      
  def show_student(self):
      list=self.student_list
      for i in range(0,len(list)):
         print(list)

