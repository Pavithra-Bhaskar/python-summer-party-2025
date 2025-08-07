# 🎢 Disney Parks Guest Spending Behavior
Company: Disney ◆ Difficulty: Hard

You are a data analyst working with the Disney Parks revenue team to understand nuanced guest spending patterns across different park experiences. The team wants to develop a comprehensive view of visitor purchasing behaviors. Your goal is to uncover meaningful insights that can drive personalized marketing strategies.

---

## 📌 Challenge Questions

1️⃣ **Identify and remove any duplicate entries in the dataset to ensure data quality.**  
How many duplicates were found and removed?

2️⃣ **After dropping duplicates, aggregate the data to find the average user interaction time for each number of search results displayed per page.**  
What are the average interaction times?

3️⃣ **Sort the aggregated results from Q2 to determine which number of search results per page has the highest average user interaction time.**  
What is the optimal number of search results per page?

---

## ✅ What I Did

- Used `datetime` filtering to isolate data by month and year.
- Applied `groupby()`, `.agg()`, and `.merge()` to compute average spend and visit-based comparisons.
- Performed sequential analysis to compare first vs last visits using `.sort_values()` and `.groupby().first()` / `.last()`.
- Created a spending segmentation function and used `.apply()` to categorize guests.

---

## 💡 What I Learned

- The importance of date handling and `.dt` accessor in pandas for time-based filtering.
- How to perform row-level comparisons (first vs last) within grouped data.
- Using `groupby()` + `agg()` effectively for multi-metric summaries.
- Building and applying custom logic functions using `.apply()` for segmentation tasks.

---

## ⚠️ Things to Be Cautious About

- Always convert date columns to `datetime` before filtering or comparing.
- Be careful with `groupby().first()` and `.last()` — sort the data beforehand to avoid incorrect assumptions.
- Always check for missing or zero-spending rows before summarizing or segmenting.
- When segmenting with thresholds, double-check your inequality signs (`<`, `<=`, etc.) to prevent misclassification.

---

## 🏁 Day 03: Done & Dusted!  
On to the next challenge! 🚀
