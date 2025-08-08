 
###Nike : Celebrity Product Drops Sales Performance Analysis

You are a Product Analyst working on Nike's marketing performance team. Your team wants to evaluate the effectiveness of celebrity product collaborations by analyzing sales data. 
You will investigate the performance of celebrity product drops to inform future marketing strategies.
---

## ✅ What I Learned

- Learned how to identify and handle **missing data**, especially in key metrics like `sale_amount`.
- Understood the importance of converting string dates to **datetime format** for accurate filtering.
- Practiced filtering records based on multiple conditions (e.g., quarter, null values, collaborations).
- Realized that not all null values are equally important – missing values in key fields can affect the integrity of analysis more significantly.
- Learned how to **identify unique combinations** (celebrity + product) without duplication.
- Understood how to rank performance by **aggregating data**, such as calculating total sales per collaboration.

## ❌ Mistakes I Made & Fixed

- Overwrote the entire DataFrame by mistake while converting `sale_date` to datetime format.
- Initially forgot to check for non-null `celebrity_id` while filtering for collaboration records.
- Missed dropping rows with null `sale_amount` before calculating top sales.

## 📌 Key Insights

- Always **inspect and clean data first** before analysis.
- Use `.notnull()` and `.dropna()` wisely based on the context of the analysis.
- Use **grouping and sorting** to extract meaningful performance metrics.
- For real-world tasks like sales analysis, ensure the data range (like Q1 2025) is correct and consistent.
- Accurate data filtering and aggregation are crucial for **performance ranking**.

🏁 Day 7: Done! On to the next challenge 🚀
