# Ben & Jerry's Ice Cream Sales Seasonal Performance Assessment

# You are a Product Insights Analyst working with the Ben & Jerry's sales strategy team to investigate seasonal sales patterns through comprehensive data analysis. 
# The team wants to understand how temperature variations and unique transaction characteristics impact ice cream sales volume. Your goal is to perform detailed data cleaning and exploratory analysis to uncover meaningful insights about seasonal sales performance.

# table: ice_cream_sales_data(transaction_id, product_name, sale_date, sales_volume, temperature)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Q1: Identify and remove any duplicate sales transactions from the dataset to ensure accurate analysis of seasonal patterns.

sales_data = ice_cream_sales_data.drop_duplicates()
print(sales_data)

print("Original rows:", len(ice_cream_sales_data))
print("After removing duplicates:", len(sales_data))
print("Duplicates removed:", len(ice_cream_sales_data) - len(sales_data))

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Q2: Create a pivot table to summarize the total sales volume of ice cream products by month and temperature range.
# Use the following temperature bins where each bin excludes the upper bound but includes the lower bound:
# - Less than 60 degrees
# - 60 to less than 70 degrees
# - 70 to less than 80 degrees
# - 80 to less than 90 degrees
# - 90 to less than 100 degrees
# - 100 degrees or more

sales_data = ice_cream_sales_data.drop_duplicates()

sales_data['sale_date'] = pd.to_datetime(sales_data['sale_date'])

sales_data['month'] = sales_data['sale_date'].dt.to_period('M')

temp_bins = [float('-inf'),60,70,80,90,100,float('inf')]
temp_labels = ['<60','60-69','70-79','80-89','90-99','100+']

sales_data['temp_range'] = pd.cut(sales_data['temperature'], bins = temp_bins, labels = temp_labels, right = False)
# print(sales_data)

pivot_table_data = pd.pivot_table( sales_data,
                                    values = 'sales_volume',
                                    index = 'month',
                                    columns = 'temp_range',
                                    aggfunc = 'sum',
                                    fill_value = 0)

print(pivot_table_data)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Q3: Can you detect any outliers in the monthly sales volume using the Inter Quartile Range (IQR) method? A month is considered an outlier if falls below Q1 minus 1.5 times the IQR or above Q3 plus 1.5 times the IQR.

ice_cream_sales_data['sale_date'] = pd.to_datetime(ice_cream_sales_data['sale_date'])

ice_cream_sales_data['month'] = ice_cream_sales_data['sale_date'].dt.to_period('M')

monthly_sales = ice_cream_sales_data.groupby('month')['sales_volume'].sum().reset_index()

q1 = monthly_sales['sales_volume'].quantile(0.25)
q3 = monthly_sales['sales_volume'].quantile(0.75)
iqr = q3 - q1
# print(iqr)

# outliers
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr

outliers = monthly_sales[(monthly_sales['sales_volume'] < lower_bound) | (monthly_sales['sales_volume'] > upper_bound)]
print('Outlier months:\n',outliers)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


---
