# Google

#You are a Product Analyst on the Google Search team investigating user engagement with search result pages. The team wants to understand how different numbers of search results impact user interaction time. 
# Your analysis will help optimize the current search results presentation strategy.

# Tables
# user_engagement_data(user_id, interaction_time, search_results_displayed, interaction_date)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Q1:Identify and remove any duplicate entries in the dataset to ensure data quality. How many duplicates were found and removed?

initial = user_engagement_data.shape[0]

duplicate_removed = user_engagement_data.drop_duplicates()

final = duplicate_removed.shape[0]

print('Duplicates found and removed',initial-final )

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Q2:After dropping duplicates, aggregate the data to find the average user interaction time for each number of search results displayed per page. What are the average interaction times?

non_duplicate_df = user_engagement_data.drop_duplicates()

result = non_duplicate_df.groupby('search_results_displayed')['interaction_time'].mean().reset_index()
print(result)

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Q3:Sort the aggregated results from Q2 to determine which number of search results per page has the highest average user interaction time. What is the optimal number of search results per page?

non_duplicate_df = user_engagement_data.drop_duplicates()

result = non_duplicate_df.groupby('search_results_displayed')['interaction_time'].mean().reset_index()

sorted_result = result.sort_values(by='interaction_time', ascending=False).reset_index(drop=True)

print(sorted_result)
print('\nhighest:\n',sorted_result.iloc[0])

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
