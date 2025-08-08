# Day 2: Amazon Ad Performance by Product Category  
**Company:** Amazon ◆ **Difficulty:** Medium  

---

## 📘 Challenge Context  
You’re part of the Amazon Ads team analyzing ad performance data.  
Your task is to evaluate product categories that outperform average click-through rates (CTR), helping to guide advertising strategy.  

---

## ❓ Challenge Questions  

### Q1:  
**What is the average click-through rate (CTR) for sponsored product ads for each product category that contains the substring 'Electronics' in its name during October 2024?**  
→ This analysis helps determine which electronics-related categories are performing optimally.  

### Q2:  
**Which product categories have a higher-than-average CTR in October 2024?**  
→ Identifying high-performing categories helps prioritize ad budgets.  

### Q3:  
**What is the percentage difference between their CTR and the overall average CTR?**  
→ Quantifies how much better they perform than average.  

---
## 🧠 What I Learned  
- Convert `recorded_date` to datetime using `pd.to_datetime()` for accurate date filtering.  
- Use `.dt.month` and `.dt.year` for date-based filtering like October 2024.  
- Apply `.str.contains("Electronics")` to filter relevant product categories.  
- Calculate CTR using:  
  `CTR = (clicks / impressions) * 100`  
- Use `groupby('product_category')` to summarize performance.  
- Compare each category’s CTR against the overall average CTR.  
- Calculate percentage difference with:  
  `((category_CTR - overall_avg_CTR) / overall_avg_CTR) * 100`

---

## 🐛 Mistakes I Made  
- Forgot to convert the date column before filtering — caused incorrect data subset.  
- Tried filtering before calculating CTR — broke the logic.  
- Didn’t filter out `impressions == 0` — led to division errors.  
- Misused `.mean()` on grouped data instead of raw CTR values.  
- Missed proper `.str.contains("Electronics")` filtering at first.

---

## 🌟 Reflections  
This challenge reminded me how important step-by-step transformation is in data analysis.  
Realizing how CTR connects to business outcomes like ad performance made it engaging.  
Combining text-based filtering and metric analysis felt like solving a real-world product problem.

---

**Day 2: ✅ Complete and learned tons!**
