import math

print("choose either 'investment' or 'bond' from the menu below to proceed: \n")
print("investment   - to calculate the amount of interest you'll earn on interest.")
print("bond         - to calculate the amount you'll have to pay on a home loan.\n")

validwords = ('BOND, Bond, bond, INVESTMENT, Investment, investment')
validNumbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

name = input("Please Type either Investment or Bond: ")
while name == "" or name in validNumbers:
        name = input("Please Type either Investment or Bond: ")
strinput0 = name
char_only0 = ''
for char in strinput0:
    if char in validwords:
        char_only0 += char
    name = char_only0

interest = input("Compound or Simple interest: ")
if interest.lower() == "compound":
        print("You have chosen compound interest")
        p=float(input("Please enter the amount of money you depositing: "))
        r=float(input("Please enter the interest rate: "))
        t=int(input("Please enter the number of years you planning on investing: "))
        compound = p*math.pow((1+r),t)
        print("Compound interest: R",round(compound,2))

if interest.lower() == "simple":
        print("You have chosen simple interes")
        p=float(input("Please enter the amount of money you depositing: "))
        r=float(input("Please enter the interest rate: "))
        t=int(input("Please enter the number of years you planning on investing: "))
        simple = p*(1+r*t)
        print("Simple interest: R",round(simple,2))

print("\n")
if name.lower() == 'bond':
        pv=float(input("Please enter the present value of the house: "))
        rr=float(input("Please enter the interest rate per period: "))
        n=int(input("Please enter the number of months over which the bond will be repaid: "))
        repayment = float(pv*((rr*((rr+1)**n))/(((rr+1)**n)-1)))
        print("Your monthly payment is: R",round(repayment,2))

      

    
    
