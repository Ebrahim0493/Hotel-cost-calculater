import math


print('''Choose either 'Investment' or 'bond' from the menu below to proceed:

-----|Investment|-----  to calculate the amount of interest you'll earn in interest

-------|Bond|-------    to calculate the amount you'll have to pay on a home loan''')

#Input from user starts conditional statements

invest_or_bond = input(str("Please enter Investment or Bond\n" )).lower()

if invest_or_bond  == "investment":
        p = float(input("How much are you depositing?\nR")) 
        r = float(input("At which interest rate percentage?\n" )) 
        r = (r/100) / 12
        t = float(input("How many years are you planning to invest for? \n"))  
        simp_comp = str(input("Choose 'Simple' or 'Compound' interest. \n")).lower().upper()
        
        if simp_comp == "simple":
            "simple" == simp_comp
            simp_comp = p*(1 + r * t) 
            total = simp_comp
            print (f"Your interest earned over {t} years will be R{total}".format())
        elif simp_comp:
            simp_comp = p*math.pow((1+r),t) 
            total = simp_comp
            print (f"Your interest earned over {t} years will be R{total}".format()) 

#Bond is another conditional
elif invest_or_bond == "bond":
        p = float(input("What is the current value of the house?\nR")) 
        i = float(input("At which interest rate percentage?\n" )) 
        i = ((i/100)/12)/12 
        n = float(input("How many months you plan to repay? \n")) 
        monthly = float(math.floor((i*p)/(1 - (1+i)**(-n)))) 
        print(f"Your monthly repayment will be {monthly}".format())
else:
 print("Please select either bond or invesment ONLY thnak you.") 
