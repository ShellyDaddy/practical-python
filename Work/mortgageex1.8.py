# exercise 1.8
principle=500000.0      # here we have made the required variables . 
rate=0.05
payment=2684.11
extra_payment=1000
total_paid=0.0
month=0

while principle>0:
  if month<12:
    monthly_payment = payment + extra_payment   # we have made a new variable here named monthly_payment which stores the final payment made at the end of the month in both conditions i.e. before 12 month and after 12 month.
  else:
    monthly_payment = payment
    
  principle = principle*(1+rate/12)-monthly_payment   # herer we have done the same thing as in the last exercise but replaced payment with monthly payment as we have a condition to pay extra 1000 in the initial 12 months.
  total_paid = total_paid+monthly_payment
  month+=1                                        # 1 is added to the month after all this process is done bcoz when the next monthly payment is done we need it to be added in the next month's payment.

print("Total payment",total_paid)
print("Total months",month)
