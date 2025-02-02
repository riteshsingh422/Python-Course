#Types of operator

#1. Arithmetic Operator(+,-,*,/,%, **)

a = 5

b = 2

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b) #for finding the remainder

#2. Relational/Comparison Operators(==, !=, >,<,>=, <=)

a= 20

b=30

print(a == b) #False Output
print(a != b) #True Output
print(a >= b) #False Output
print(a <= b) #True Output
#3. Assignment Operators (=, +=, -=, *=, /=, %=)

num=10
num = num + 10 #10+10=20 Output
num += 10 #working as same it also give the same Output.
print(num)

#4. Logical Operator(not, and, or)
 
print(not True) #not operator always provide you the opposite value. Output will be False.
print(not False) #Output will be True.

val1 =True
val2 =False
print("And Operator: " ,val1 and val2) #In and Operator if both value will be true and output will be true other wise false.
print("OR Operator: " ,val1 or val2) #In or Operator if any value will be true and output will be true other wise false.