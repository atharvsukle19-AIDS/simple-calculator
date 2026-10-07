num1=int(input("Enter your First Number : "))
num2=int(input("Enter your second number : "))
operator=input("Enter your operator : ") 

if operator=="+":
    print("Addition is :",num1+num2)
elif operator=="-":
    print("Subtraction is : ",num1-num2)
elif operator =="*":
    print("Multiplication is : ",num1*num2)
elif operator =="/":
    print("Division is : ",num1/num2)
elif operator =="//":
    print("Floor Division is : ",num1//num2)
else :
    print("Invalid Data")