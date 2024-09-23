'''
num1=float(input(" enter first number is :-"))
num2=float(input(" enter second number is :-"))
num3=num1 or num2
print("press 1 for addition\n press 2 for substracion \n press 3 for division \4 for multiplicaiton")
count=int(input("enter the your choice in 1 to 4 :-"))
if count ==1:
   sum = num1 + num2
   print("the sum of num1 and num2 is :-",sum)
elif count ==2:
    sub = num1 - num2
    print("the sub of num1 and num2 is :-",sub)
elif count ==3:
    mul = num1 * num2
    print("the mul of num1 and num2 is :-",mul)
elif count ==4:
    div = num1 / num2
    print("the division of num1 and num2 is:-",div)
else :
    print("you wil write the wrong number please seleceted the write number in 1 to 4 :-")
'''

v=int(input("please enter your age :-"))
while v <=10:
  print(v)
  if (v == 8):
   	break
  v+=1
