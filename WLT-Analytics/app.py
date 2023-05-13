import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Data Loading
data = pd.read_csv('loan_data.csv')

# Step 2: Data Cleaning and Preprocessing
# Example: Check for missing values
missing_values = data.isnull().sum()
print('Missing Values:')
print(missing_values)

# Example: Handle missing values by dropping rows with missing values
data.dropna(inplace=True)

# Step 3: Data Analysis
# Example: Calculate summary statistics
loan_stats = data.describe()
print('Summary Statistics:')
print(loan_stats)

# Example: Aggregate data based on loan type and calculate average loan amount
avg_loan_amount_by_type = data.groupby('Loan Type')['Loan Amount'].mean()
print('Average Loan Amount by Loan Type:')
print(avg_loan_amount_by_type)

# Example: Perform exploratory data analysis (EDA)
# Visualize the distribution of loan amounts using a histogram
plt.hist(data['Loan Amount'], bins=10)
plt.xlabel('Loan Amount')
plt.ylabel('Frequency')
plt.title('Distribution of Loan Amounts')
plt.show()

# Step 4: Visualization
# Example: Create a scatter plot of loan amount vs. interest rate
plt.scatter(data['Loan Amount'], data['Interest Rate'])
plt.xlabel('Loan Amount')
plt.ylabel('Interest Rate')
plt.title('Loan Amount vs. Interest Rate')
plt.show()

# Example: Create a bar chart of average loan amount by loan type
avg_loan_amount_by_type.plot(kind='bar')
plt.xlabel('Loan Type')
plt.ylabel('Average Loan Amount')
plt.title('Average Loan Amount by Loan Type')
plt.show()
