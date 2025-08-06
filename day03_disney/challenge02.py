# Disney Parks Guest Spending Behavior
# pov:You are a data analyst working with the Disney Parks revenue team to understand nuanced guest spending patterns across different park experiences. 
# The team wants to develop a comprehensive view of visitor purchasing behaviors. Your goal is to uncover meaningful insights that can drive personalized marketing strategies.

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Q1: What is the average spending per guest per visit for each park experience type during July 2024? Ensure that park experience types with no recorded transactions are shown with an average spending of 0.0. 
# This analysis helps establish baseline spending differences essential for later segmentation.

fct_guest_spending['visit_date'] = pd.to_datetime(fct_guest_spending['visit_date'])

july_data = fct_guest_spending[ (fct_guest_spending['visit_date'].dt.year == 2024) &
                                (fct_guest_spending['visit_date'].dt.month == 7)]

avg_amount_spent = july_data.groupby('park_experience_type')['amount_spent'].mean().reset_index()

all_park_types = fct_guest_spending['park_experience_type'].unique()

all_park_df = pd.DataFrame({'park_experience_type': all_park_types})

result = all_park_df.merge(avg_amount_spent, on = 'park_experience_type' , how = 'left').fillna(0.0)

result.rename(columns = {'amount_spent':'avg_amt_spent'}, inplace = True)
print(result)


# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Q2:For guests who visited our parks more than once in August 2024, what is the difference in spending between their first and their last visit? 
# This investigation, using sequential analysis, will reveal any shifts in guest spending behavior over multiple visits.

fct_guest_spending['visit_date'] = pd.to_datetime(fct_guest_spending['visit_date'])

august_visits  = fct_guest_spending[
                                     (fct_guest_spending['visit_date'].dt.month == 8) &
                                     (fct_guest_spending['visit_date'].dt.year == 2024)
]

guest_counts = august_visits.groupby('guest_id').size().reset_index( name = 'visit_count')

multi_visit_guest = guest_counts[guest_counts['visit_count'] > 1]['guest_id']

aug_multi_visit = august_visits[august_visits['guest_id'].isin(multi_visit_guest)]

aug_multi_visit_sorted = aug_multi_visit.sort_values(['guest_id', 'visit_date'])

# print(aug_multi_visit_sorted)

first_visit = aug_multi_visit_sorted.groupby('guest_id').first().reset_index()

# print(first_visit)

last_visit = aug_multi_visit_sorted.groupby('guest_id').last().reset_index()

# print(last_visit)

visit_compare = first_visit[['guest_id','amount_spent']].merge(last_visit[['guest_id','amount_spent']], on = ['guest_id'], how = 'left', suffixes = ('_first','_last'))
# print(visit_compare)

visit_compare['Diff'] = (visit_compare['amount_spent_last'] - visit_compare['amount_spent_first'])

print(visit_compare)

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#Q3:In September 2024, how can guests be categorized into distinct spending segments such as Low, Medium, and High based on their total spending? Use the following thresholds for categorization:
# -Low: Includes values from $0 up to, but not including, $50.
# -Medium: Includes values from $50 up to, but not including, $100.
# -High: Includes values from $100 and above.
# Exclude guests who did not make any purchases in the period.

fct_guest_spending['visit_date'] = pd.to_datetime(fct_guest_spending['visit_date'])

sept_visit_guest = fct_guest_spending[(fct_guest_spending['visit_date'].dt.month == 9)&
                                     ( fct_guest_spending['visit_date'].dt.year == 2024)]
# print(sept_visit_guest)

total_spending = sept_visit_guest.groupby('guest_id')['amount_spent'].sum().reset_index()

total_spending = total_spending[total_spending['amount_spent'] > 0]
# print(total_spending)

def spending_segments(amount_spent):
  if amount_spent < 50:
     return 'Low'
  elif amount_spent < 100:
    return 'Medium'
  else:
      return 'High'

total_spending['Segment'] = total_spending['amount_spent'].apply(spending_segments)

print(total_spending)
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                          

