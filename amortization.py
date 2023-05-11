loan = float(input("Loan amount: "))
interest = (float(input("Interest rate: "))/100)
years = int(input("Years: "))

start_balance = loan
pvaf = round((1 - (1 + interest)**(-years))/interest, 4)
ANNUAL_PAYMENT = round(loan / pvaf, 2)


for i in range(1, 21):
    year_end_interest = round(start_balance * interest, 2)
    print(i, start_balance, year_end_interest, ANNUAL_PAYMENT, \
        round(ANNUAL_PAYMENT - year_end_interest,2), start_balance - (ANNUAL_PAYMENT - year_end_interest), sep="  |  ")
    start_balance = round(start_balance - (ANNUAL_PAYMENT - year_end_interest),2)