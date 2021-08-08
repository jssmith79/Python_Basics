#income tax calculator with user inputs#

sal = int(input("Enter annual salary:"))
pre = int(input("Enter Pretax Deductions Annually:"))
total = sal - pre

taxpayable = 0

if total <= 9950:
    taxpayable = total * 0.10

elif total <= 40525:
    taxpayable = (total - 9950) * 0.12

elif total <= 86375:
    taxpayable = (total - 40525) * 0.22 or (total <= 86375, 0)

elif total <= 164925:
    taxpayable = (total - 86375) * 0.24 or (total <= 164925, 0)

elif total <= 209425:
    taxpayable = (total - 164925) * 0.32 or (total <= 209425, 0)

else:
    taxpayable = 0
    taxpayable += 9950 * 0.10
    taxpayable += (total - 40525) * 0.12
    taxpayable += (total - 86375) * 0.22
    taxpayable += (total - 164925) * 0.24
    taxpayable += (total - 209425) * 0.32

print("total tax to pay is:", taxpayable)
