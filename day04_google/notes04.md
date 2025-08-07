# 📅 Day 4: Google Challenge – Search Results Interaction Analysis
Company: Google ◆ Difficulty: Easy

You are a Product Analyst on the Google Search team investigating user engagement with search result pages.  
The team wants to understand how different numbers of search results impact user interaction time.  
Your analysis will help optimize the current search results presentation strategy.

## ❓ Challenge Questions
1️⃣ Identify and remove any duplicate entries in the dataset to ensure data quality.  
2️⃣ After dropping duplicates, aggregate the data to find the average user interaction time for each number of search results displayed per page.  
3️⃣ Sort the aggregated results from Q2 to determine which number of search results per page has the highest average user interaction time.  

---

## ✅ What I Did
- Cleaned the dataset by identifying and removing duplicate rows to ensure data quality.
- Aggregated the average user interaction time based on the number of search results displayed per page.
- Sorted the results to determine the optimal number of search results that lead to maximum engagement.

## 💡 Key Learnings
- Even small amounts of duplicate data can skew averages — always check for and remove them before analysis.
- Grouping and aggregating data helps uncover patterns in user behavior.
- Sorting aggregated results helps to identify the most effective configuration (in this case, the ideal number of search results per page).

## ⚠️ What to Be Careful About
- Always perform data cleaning steps (like removing duplicates) before analysis.
- Watch out for sorting direction — descending vs. ascending matters.
- Be cautious with DataFrame chaining — better to assign to variables for clarity and debugging.
- Resetting index after sorting/grouping can help maintain clean, readable outputs.

---

🏁 **Day 4: Done!** On to the next challenge 🚀





