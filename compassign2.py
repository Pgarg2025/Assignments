#Question 1
line = "Python is a case sensitive language"
#part a
print(len(line))

#part b
line1=line[-1::-1]
print(line1)

#part c
line2=line[10:26]
print(line2)

#part d
line3=line.replace("a case sensitive", "object oriented")
print(line3)

#part e
line4=line.find("a")
print(line4)

#part f
line5=line.replace(" ", "")
print(line5)



#Question 2
letter = '''Hey,ABC Here!
My SID is XYZ
I am from PYQ department and my CGPA is JKL'''
name=input("Enter your name=")
roll_no=input("Enter your SID=")
branch=input("Enter your department=")
cgpa=input("Enter your CGPA=")
letter=letter.replace("ABC", name)
letter=letter.replace("XYZ", roll_no)
letter=letter.replace("PYQ", branch)
letter=letter.replace("JKL", cgpa)
print(letter)



#Question 3
a=56
b=10
#part a
c=a&b
print("Part a:", c)

#part b 
d=a|b
print("Part b:",  d)

#part c
e=a^b
print("Part c:", e)

#part d
x=a<<2
print("Part d, a:", x)
y=b<<2
print("Part d, b:", y)

#part e
p=a>>2
print("Part e, a:", p)
q=b>>4
print("Part e, b:", q)



#Question 4
a=float(input("Enter a="))
b=float(input("Enter b="))
c=float(input("Enter c="))
if a>=b and a>=c :
 print("a is greatest")
elif b>=a and b>=c :
 print("b is greatest")
else :
 print("c is greatest") 



#Question 5
str=input("Enter any line or paragraph : \n")
namecount=str.count("name")
# print(type(namecount)) 
#just finding the type of variable count and it comes int
if namecount>= 1 :
 print("Yes")
else:
 print("No")



#Question 6
a=int(input("Enter first side="))
b=int(input("Enter second side="))
c=int(input("Enter third side="))
if c>=a+b :
 print("NO")
elif b>=a+c :
 print("NO")
elif a>=b+c :
 print("NO")
else :
 print("YES")
