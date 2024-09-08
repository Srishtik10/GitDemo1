#program 6: relational and logical operators
num1=int(input("Enter the 1st number:"))
num2=int(input("Enter the 2nd number:"))
if num1 % 2==0 and num2 %2 ==0:
    print("both numbers are even")
elif num1 %2 !=0 and num2 %2 != 0:
    print("both numbers are odd")
else:
    print("one number is even and other is odd")
