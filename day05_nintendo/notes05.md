# 🧠 Day 5: Pre-sale Data Cleaning & Aggregation
Company: Nintendo ◆ Difficulty: Hard ◆

You are a Product Analyst working with the Nintendo Switch 2 pre-sales team to analyze regional pre-order patterns and customer segmentation. Your team needs to understand how different demographics influence pre-sale volumes across regions. 
You will leverage historical pre-sale transaction data to extract meaningful insights that can guide marketing strategies.
  
## ✅ What I Learned

- **Missing Value Handling**:
  - Used `.isnull().any(axis=1)` to detect rows with missing values.
  - Calculated the **percentage of missing data**:
    ```python
    missing_pct = (rows_with_missing / total_rows) * 100
    ```
  - Cleaned the data:
    - Filled missing `region` with `'unknown'`
    - Dropped rows missing essential fields like `customer_id` and `pre_order_date`
    - (Optional) Filled missing `demographic_group` with `'Not specified'`
    - (Optional) Filled missing `pre_order_quantity` with its mean or median

- **Datetime Transformation**:
  - Converted `pre_order_date` to month using:
    ```python
    pre_sale_data['Month'] = pre_sale_data['pre_order_date'].dt.to_period('M')
    ```

- **Data Aggregation**:
  - Grouped by `Month`, `region`, and `demographic_group` to calculate monthly total pre-orders.
  - Used `.groupby().sum().reset_index()` for final output.

---

## ❌ Mistakes I Made & How I Corrected Them

| Mistake | Correction |
|--------|------------|
| Used incorrect variable (`orginal_df`) in percentage formula | Replaced with `total_rows` |
| Didn’t handle missing `demographic_group`, causing groupby issues | Used `.fillna('Not specified')` |
| Confused by forecast logic | Broke down logic by calculating growth rate |
| Forgot to convert dates to month format | Used `.dt.to_period('M')` correctly |

---

## 🧭 How I Thought Through the Problem

1. Checked for missing values and quantified them
2. Chose appropriate handling (fill/drop)
3. Extracted month from `pre_order_date`
4. Used `groupby` to aggregate totals
5. Tackled growth-based prediction by:
   - Calculating total pre-order per region for July and August
   - Calculating growth rate = Aug / July
   - Predicting September = August total * growth rate

---

## 📌 Summary

- Learned how to clean and reshape data effectively
- Understood group-wise aggregations
- Applied forecasting using logical progression
- Built confidence with pandas operations:
  - `.isnull()`, `.fillna()`, `.dropna()`
  - `.groupby()`, `.sum()`, `.reset_index()`
  - `.dt.to_period('M')`

---
🏁 Day 5: Done! On to the next challenge 🚀
