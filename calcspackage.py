from calcs import*
while True:
    print("select option")
    print("1.addition")
    print("2.subtraction")
    print("3.multiply")
    print("4.divide")
    choice = input("enter your choice:")
    num1=int(input("enter the first number:"))
    num2=int(input("enter the second number:"))
    if choice=="1":
        print(num1,"+",num2,"=",addition(num1,num2))
    elif choice=="2":
        print(num1,"-",num2,"=",subtraction(num1,num2))
    elif choice=="3":
        print(num1,"*",num2,"=",multiplication(num1,num2))
    elif choice=="4":
        print(num1,"/",num2,"=",division(num1,num2))
    else:
        print("invalid choice")
    break
