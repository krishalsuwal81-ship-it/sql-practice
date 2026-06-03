print("=====Hello welcome to expectation marks room=====")
krishal = {
    "english": "A",
    "nepali" : "B+",
    "B MATHS":"B+",
    "account":"A+",
    "COMPUTER":"A+",
    "samajik":"A"
}
grade= (3.6*5+3.2*3+3.2*5+4*5+4*4+3.6*5)/27
krisha={
    "english": "A+",
    "nepali" : "A+",
    " MATHS":"B",
    "Chemistry":"B+",
    "PHYSIC":"B",
    "biology":"c+"
}
grade2=(4*5+4*3+2.8*5+3.2*5+2.8*5+2.4*5)/27
suyog={
    "english": "A",
    "nepali" : "A",
    " MATHS":"A",
    "Chemistry":"B+",
    "PHYSIC":"B+",
    "computer":"A"
}
grade5=(3.6*5+3.6*3+3.6*5+3.2*5+3.2*5+3.6*5)/27
print("which grade u want too see :")
y=(input("enter yess or no to see the name of user that enter there expeced marks of boards 2083:"))
if y=="yes":
    print("1:krishal");
    print("2.krisha");
    print("3:vibek");
    print("4.krijan");
    print("5:suyog");
    n=int(input("enter which one u want to select"))
    if n == 1:
        print(krishal )
        print("your total grade is :",grade)
    elif n==2:
        print(krisha)
        print("your total grade is:",grade2)
    elif n==5 :
           print("your subject grade is :",suyog)
           print("your gpa is :",grade5)
    c=input("Do you want to see more data of any user?ans in yes or no.") 
    if c == "yess":
        d=input("which one do u want to see")  
        if d== 1:
            print("your grade is :",krishal)
            print("your total gpa is",grade)  
        elif d==2:
            print(krisha)
            print("your total grade is:",grade2)
        elif d==5 :
           print("your subject grade is :",suyog)
           print("your gpa is :",grade5)
elif y=="no":
    print("thank you for your time")





