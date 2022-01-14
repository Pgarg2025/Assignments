#Piyush Garg
#21103103
#CSE
# Ques 1
a = int(input("Enter value of a ="))
b = int(input("Enter value of b ="))
c = int(input("Enter value of c ="))
d = (a+b+c)/3
print("Average is =",d)



#Ques 2
standard_deduction = 10000
depend_deduction = 3000
gross=int(input("Enter your gross income ="))
no_of_dependents=int(input("Enter your no of dependents ="))
taxable_income= float(gross-standard_deduction-(depend_deduction*no_of_dependents))
tax = float(taxable_income*0.2)
print("Your income tax is =" , tax)



#Ques 3
SID = int(input("Enter your SID ="))
Name = input("Enter your name =")
Gender = input("Enter your gender =")
Course_name = input("Enter your course name =")
CGPA = float(input("Enter your CGPA ="))
STUDENT = [SID, Name, Gender, Course_name, CGPA] #creating a list
print(STUDENT) #printing the list



#Ques 4
st1=int(input("Enter marks of first student="))
st2=int(input("Enter marks of second student="))
st3=int(input("Enter marks of third student="))
st4=int(input("Enter marks of fourth student="))
st5=int(input("Enter marks of fifth student="))
marks=[st1, st2, st3, st4, st5]
marks.sort()
print(marks)



#Ques 5
colour =['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
#part a
colour.remove('Black')
print("Part a :", colour)

#part a another method
#colour.pop(3)
#print("Part a :", colour)

#part b
clr=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
clr[3:5]=['Purple']
print("Part b :", clr)  








