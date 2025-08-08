# Nike : Celebrity Product Drops Sales Performance Analysis

# You are a Product Analyst working on Nike's marketing performance team. Your team wants to evaluate the effectiveness of celebrity product collaborations by analyzing sales data. You will investigate the performance of celebrity product drops to inform future marketing strategies.
# Table:fct_sales(sale_id, celebrity_id, product_id, sale_date, sale_amount)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Q1: For Q1 2025 (January 1st through March 31st, 2025), can you identify all records of celebrity collaborations from the sales data where the sale_amount is missing? This will help us flag incomplete records that could impact the analysis of Nike's product performance.

fct_sales['sale_date'] = pd.to_datetime(fct_sales['sale_date'])

month_filtered_sales = fct_sales[
                        (fct_sales['sale_date'] >= '2025-01-01') &
                        (fct_sales['sale_date'] < '2025-04-01')]

missing_data = month_filtered_sales[month_filtered_sales['sale_amount'].isnull()]

print(missing_data)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Q2: For Q1 2025 (January 1st through March 31st, 2025), can you list the unique combinations of celebrity_id and product_id from the sales table? This will ensure that each collaboration is accurately accounted for in the analysis of Nike's marketing performance.

fct_sales['sale_date'] = pd.to_datetime(fct_sales['sale_date'])

month_filtered_sales = fct_sales[
                        (fct_sales['sale_date'] >= '2025-01-01') &
                        (fct_sales['sale_date'] < '2025-04-01')]

unique = month_filtered_sales[['celebrity_id','product_id']].drop_duplicates()
print(unique)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Q3: For Q1 2025 (January 1st through March 31st, 2025), can you rank the unique celebrity collaborations based on their total sales amounts and list the top 3 collaborations in descending order? This will help recommend the most successful partnerships for Nike's future product drop strategies.

fct_sales['sale_date'] = pd.to_datetime(fct_sales['sale_date'])

fct_sales = fct_sales[(fct_sales['sale_date'] >= '2025-01-01')&
                      (fct_sales['sale_date'] < '2025-04-01')]

fct_sales = fct_sales.dropna(subset = 'sale_amount')
# print(fct_sales)

collaboration_data = fct_sales.groupby(['celebrity_id','product_id'])['sale_amount'].sum().reset_index()

collaboration_data = collaboration_data.rename(columns = {'sale_amount': 'total_sale_amt'})
# print(collaboration_data )

top_collab = collaboration_data.sort_values(by = ['total_sale_amt'], ascending =False)
print(top_collab.head(3))

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
