# Day 2: Sponsored Posts Click Performance
# Tables:
# --> fct_ad_performance(ad_id, product_id, clicks, impressions, recorded_date)
# --> dim_product(product_id, product_category, product_name)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Q1:What is the average click-through rate (CTR) for sponsored product ads for each product category that contains the substring 'Electronics' in its name during October 2024? 
# This analysis will help determine which electronics-related categories are performing optimally.


merged_df = pd.merge(fct_ad_performance,dim_product, on = 'product_id')

merged_df['recorded_date'] = pd.to_datetime(merged_df['recorded_date'])

filtered_df = merged_df[
              (merged_df['product_category'].str.contains('Electronics'))&
              (merged_df['recorded_date'].dt.month == 10)&
              (merged_df['recorded_date'].dt.year == 2024)&
              (merged_df['impressions'] > 0)
]

filtered_df['CTR'] = filtered_df['clicks'] / filtered_df['impressions'] *100
# print(filtered_df)
avg_ctr_by_category = filtered_df.groupby('product_category')['CTR'].mean().reset_index()


print ('avg ctr per category: \n', avg_ctr_by_category)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Q2:Which product categories have a CTR greater than the aggregated overall average CTR for sponsored product ads during October 2024? 
# This analysis will identify high-performing categories for further optimization. For this question, we want to calculate CTR for each ad, then get the average across ads by product category & overall.

merged_df = pd.merge(fct_ad_performance, dim_product, on='product_id')

merged_df['recorded_date'] = pd.to_datetime(merged_df['recorded_date'])

filtered_df = merged_df[
    (merged_df['recorded_date'].dt.year == 2024) &
    (merged_df['recorded_date'].dt.month == 10) &
    (merged_df['impressions'] > 0)
]

filtered_df['CTR'] = (filtered_df['clicks'] / filtered_df['impressions']) * 100

avg_ctr_by_category = filtered_df.groupby('product_category')['CTR'].mean().reset_index()

overall_avg_ctr = filtered_df['CTR'].mean()

prod_cat_above_avg_ctr = avg_ctr_by_category[avg_ctr_by_category['CTR'] > overall_avg_ctr]

print("CTR per ad:\n", filtered_df[['product_category', 'CTR']])
print("\nAverage CTR by Category:\n", avg_ctr_by_category)
print("\nOverall Average CTR:\n", overall_avg_ctr)
print("\nProduct Categories with CTR > Overall Average:\n", prod_cat_above_avg_ctr)

# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Q3:For the product categories identified in the previous question, what is the percentage difference between their CTR and the overall average CTR for October 2024? 
# This analysis will quantify the performance gap to recommend specific categories for targeted advertising optimization.

merged_df = pd.merge(fct_ad_performance,dim_product, on = 'product_id')

merged_df['recorded_date'] = pd.to_datetime(merged_df['recorded_date'])

filtered_df = merged_df[
              (merged_df['recorded_date'].dt.month == 10)&
              (merged_df['recorded_date'].dt.year == 2024)&
              (merged_df['impressions'] > 0)
]

filtered_df['CTR'] = filtered_df['clicks'] / filtered_df['impressions'] *100

avg_ctr_by_category = filtered_df.groupby('product_category')['CTR'].mean().reset_index()

overall_avg_ctr = filtered_df['CTR'].mean()
print ('overall avg ctr: ',overall_avg_ctr)
prod_cat_above_avg_ctr = avg_ctr_by_category[avg_ctr_by_category['CTR'] > overall_avg_ctr]

# print(prod_cat_above_avg_ctr)
prod_cat_above_avg_ctr['ctr_%_diff'] = ((prod_cat_above_avg_ctr['CTR'] - overall_avg_ctr)/overall_avg_ctr) *100

print("\n",prod_cat_above_avg_ctr)
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
