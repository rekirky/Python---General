balance = 4061
annualInterestRate = 0.4

monthlyInterestRate  = annualInterestRate/12

payment = 0

months=11
while balance > 0: 
    balance = 4061
    while months>=0:
        annualInterestRate = 0.2

        balance  += balance *monthlyInterestRate 
        balance  -= payment 
        months -= 1
    payment  += 1
    months = 11

print("lowest Payment:", round(payment , 3)) 