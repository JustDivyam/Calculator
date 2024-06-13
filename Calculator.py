num=int(input("Enter a number"))
num2=int(input("Enter a number"))
choice=input("1.Add\n2.Subtract\n3.Multiply\n4.Divide\nEnter your choice")
if choice.lower()=="1" or choice.lower()=="add":
    print(num+num2)
elif choice.lower()=="2" or choice.lower()=="subtract":
    print(num-num2)
elif choice.lower()=="3" or choice.lower()=="multiply":
    print(num*num2)
elif choice.lower()=="4" or choice.lower()=="divide":
    print(num/num2)
else:
    print("Enter from the given choice")

