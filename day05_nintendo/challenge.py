# Switch 2 Pre-sales Demand Forecasting

# Tables : pre_sale_data(customer_id, region, demographic_group, pre_order_date, pre_order_quantity)

# You are a Product Analyst working with the Nintendo Switch 2 pre-sales team to analyze regional pre-order patterns and customer segmentation.Your team needs to understand how different demographics influence pre-sale volumes across regions. 
# You will leverage historical pre-sale transaction data to extract meaningful insights that can guide marketing strategies.

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Q1:What percentage of records have missing values in at least one column? Handle the missing values, so that we have a cleaned dataset to work with.


value_missing_rows = pre_sale_data.isnull().any(axis=1)
# print(value_missing_rows)

no_missingValue = value_missing_rows.sum()
# print(no_missingValue)

total_rows = len(pre_sale_data)

percentage = (no_missingValue /total_rows ) * 100

print(percentage)

pre_sale_data['region'] = pre_sale_data['region'].fillna('unknown')

pre_sale_data= pre_sale_data.dropna(subset = ['customer_id','pre_order_date'])

median_quantity = pre_sale_data['pre_order_quantity'].mean()

pre_sale_data['pre_order_quantity'] = pre_sale_data['pre_order_quantity'].fillna(median_quantity)

pre_sale_data['demographic_group'] = pre_sale_data['demographic_group'].fillna('Not specified')

print(pre_sale_data)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Q2:Using the cleaned data, calculate the total pre-sale orders per month for each region and demographic group.

pre_sale_data['region'] = pre_sale_data['region'].fillna('unknown') 

pre_sale_data= pre_sale_data.dropna(subset = ['customer_id','pre_order_date']) 

# median_quantity = pre_sale_data['pre_order_quantity'].mean() 
# pre_sale_data['pre_order_quantity'] = pre_sale_data['pre_order_quantity'].fillna(median_quantity)

# pre_sale_data['demographic_group'] = pre_sale_data['demographic_group'].fillna('Not specified')

pre_sale_data['Month'] = pre_sale_data['pre_order_date'].dt.to_period('M')
# print(pre_sale_data)

total_presales_ord = pre_sale_data.groupby(['Month','region','demographic_group'])['pre_order_quantity'].sum().reset_index()
print(total_presales_ord)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Q3:Predict the total pre-sales quantity for each region for September 2024. Assume that growth rate from August to September, is the same as the growth rate from July to August in each region.

pre_sale_data['region'] = pre_sale_data['region'].fillna('unknown') 

pre_sale_data= pre_sale_data.dropna(subset = ['customer_id','pre_order_date']) 

pre_sale_data['month'] = pre_sale_data['pre_order_date'].dt.to_period('M')
# print(pre_sale_data)

monthly_sales_quantity = pre_sale_data.groupby(['month','region'])['pre_order_quantity'].sum().reset_index()

july_data = monthly_sales_quantity[monthly_sales_quantity['month'] == '2024-07']
# print(july_data)

aug_data = monthly_sales_quantity[monthly_sales_quantity['month'] == '2024-08']

combined_data = pd.merge(july_data,aug_data, on = 'region', suffixes = ['_july','_aug'])

combined_data['growth'] = combined_data['pre_order_quantity_aug'] / combined_data['pre_order_quantity_july']

combined_data['sept'] = combined_data['pre_order_quantity_aug'] * combined_data['growth']

print(combined_data)

# ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
