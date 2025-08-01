# Note: pandas and numpy are already imported as pd and np
# The following tables are loaded as pandas DataFrames with the same names: dim_groups
# Please print your final result or dataframe

#----------------Tables-----------------------------------
#dim_groups(group_id, created_date, participant_count, total_messages)

#Q1:What is the maximum number of participants among WhatsApp groups that were created in October 2024? This metric will help us understand the largest group size available.

df.created_date = pd.to_datetime(df.created_date)

filtered_df = df[(df.created_date.dt.year== 2024) & (df.created_date.dt.month== 10)]

max_no_of_participate_created_in_oct_2024 = filtered_df.participant_count.max()

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Q2: What is the average number of participants in WhatsApp groups that were created in October 2024? This number will indicate the typical group size and inform our group messaging feature considerations.

df.created_date = pd.to_datetime(df.created_date)

filtered_df = df[(df.created_date.dt.year == 2024) & (df.created_date.dt.month == 10)]

avg = filtered_df.participant_count.mean()

print(avg)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Q3: For WhatsApp groups with more than 50 participants that were created in October 2024, what is the average number of messages sent? This insight will help assess engagement in larger groups and support recommendations for group messaging features.

df.created_date = pd.to_datetime(df.created_date)

filtered_df = df[(df.created_date.dt.month==10) & (df.created_date.dt.year == 2024) & (df.participant_count > 50)]

mean = filtered_df.total_messages.mean()

print(mean)

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
