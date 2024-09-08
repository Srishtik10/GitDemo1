#program 7:for loop and bitwise operator
num=int(input("enter an integer:"))
print("binary representation:",end=" ")
for i in range(31,-1,-1):#iterate over 32 bits
    if num &(1 << i):#check if the bit at position i is set
        print("1", end="")
    else:
        print("0",end="")
print()#new line after binary representation
print("octal representation:",oct(num))
print("Hexadecimal representation:",hex(num))
