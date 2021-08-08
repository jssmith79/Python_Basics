# 401k contribution calculator#

sal = int(input("Enter current annual salary:"))
YTD = int(input("Enter your contributions to date:"))
PP = int(input("How many pay periods are left in the year?"))
YTDSAL = int(input("Enter Year to Date Gross Pay:"))
Age = int(input("Enter your age this year:"))

#Includes Catchup#

if Age > 50:
    Cont = (26000 - YTD)
    YTDSAL = (sal - YTDSAL)
    New = ((Cont / YTDSAL) * 100)
    CheckAmt = (sal / 24) * (New / 100)

#normal under 50 Catchup#

else:
    Cont = (19500 - YTD)
    YTDSAL = (sal - YTDSAL)
    New = ((Cont / YTDSAL) * 100)
    CheckAmt = (sal / 24) * (New / 100)


print("To maximize your contribution the percentage you need to contribute: ")
print(New)
print("The amount per paycheck will be: ")
print(CheckAmt)
