import csv
import random

# Define loan attributes
loan_amounts = [100000, 200000, 300000, 400000, 500000]
interest_rates = [0.05, 0.06, 0.07, 0.08, 0.09]
loan_types = ['Mortgage', 'Auto', 'Personal']
credit_ratings = ['AAA', 'AA', 'A', 'BBB', 'BB']
borrower_names = ['John Doe', 'Jane Smith', 'David Johnson', 'Sarah Davis']
transaction_details = ['Buy', 'Sell']

# Generate loan-level data
loans_data = []
for _ in range(100):  # Simulate 100 loans
    loan_amount = random.choice(loan_amounts)
    interest_rate = random.choice(interest_rates)
    loan_type = random.choice(loan_types)
    credit_rating = random.choice(credit_ratings)
    borrower_name = random.choice(borrower_names)
    transaction_detail = random.choice(transaction_details)
    
    loan_data = [loan_amount, interest_rate, loan_type, credit_rating, borrower_name, transaction_detail]
    loans_data.append(loan_data)

# Save loan-level data to a CSV file
field_names = ['Loan Amount', 'Interest Rate', 'Loan Type', 'Credit Rating', 'Borrower Name', 'Transaction Detail']

with open('loan_data.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(field_names)
    writer.writerows(loans_data)
