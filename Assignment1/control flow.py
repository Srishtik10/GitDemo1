#program 5: Control flow statements
while True:
    a=input("Enter a number(or type 'exit' to quit):")
    if a=='exit':
        break
    try:
        num=float(a)
        if num>0:
            print("The number is positive")
        elif num<0:
            print("the number is negative")
        else:
            print("the number is zero")
    except error:
        print("Invalid input!!!!")
