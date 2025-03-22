class packages():
    def OddorEven():
        num=int(input("Enter the number"))
        if (num%2==1):
            print(num,"is a odd number")
            oddeven="Odd Number"      
        else:
            print(num,"is a Even number")
            oddeven="Even Number"
            return oddeven
    def Subfields():
        itemlist=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        print("Sub-fields in AI are:")
        for i in itemlist:
            print(i)
    def Eligible():
            gender=(input("Enter your Gender"))
            age=int(input("Enter the age"))
            if age>=21 and gender=="Male":
                print(" Your Gender is:",gender)
                print("your Age is:",age)
                print("ELIGIBLE")
                YesNo="ELIGIBLE"      
            elif age<=18 and gender=="Female" :
                print(" Your Gender is:",gender)
                print("your Age is:",age)
                print("ELIGIBLE")
                YesNo ="ELIGIBLE"
            else:
                YesNo ="NOT ELIGIBLE"
                return YesNo
    def percentage(s1,s2,s3,s4,s5):
            print("Subject 1=",s1)
            print("Subject 2=",s2)
            print("Subject 3=",s3)
            print("Subject 4=",s4)
            print("Subject 5=",s5)
            tot=s1+s2+s3+s4+s5
            print("Total=",tot)
            print("Percentage=",tot/5)
    def triangle(th,tb,ph1,ph2,pb):
        areaoftriangle=(th*tb)/2
        print("Height:", th)
        print("Breadth:", tb)
        print("Area formula: (Height * Breadth) / 2")
        print("Area of Triangle:", areaoftriangle)
        perimeter = ph1 + ph2 + pb
        print("Height1:", ph1)
        print("Height2:", ph2)
        print("Breadth:", pb)
        print("Perimeter formula: Height1 + Height2 + Breadth")
        print("Perimeter of Triangle:", perimeter)