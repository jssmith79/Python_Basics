# 401k contribution calculator#

#variables_in_snake_case#
salary = int(input("Enter current annual base salary:"))
ytd_contributions = int(input("Enter your contributions to date:"))
remaining_pay_periods = int(input("How many semi-monthly pay periods are left in the year?"))
age = int(input("Enter your age this year:"))

CURRENT_YEAR_MAXIMUM_CONTRIBUTION_UNDER_50 = 22500.0
CURRENT_YEAR_MAXIMUM_CONTRIBUTION_OVER_50 = 29000.0

if age < 50:
    remaining_contributions = (CURRENT_YEAR_MAXIMUM_CONTRIBUTION_UNDER_50 - ytd_contributions)

if age >= 50:
    remaining_contributions = (CURRENT_YEAR_MAXIMUM_CONTRIBUTION_OVER_50 - ytd_contributions)

new_pay_period_dollar_amount = "${:,.2f}".format(remaining_contributions / remaining_pay_periods)
new_pay_period_percent_amount = "{:,.2f}".format(100 * int(remaining_contributions / remaining_pay_periods) / (salary / 24)) + "%"
# calculating the output#

print("The amount per paycheck will be: ")
print(new_pay_period_dollar_amount)
print("The deferral percentage will be: ")
print(new_pay_period_percent_amount)
