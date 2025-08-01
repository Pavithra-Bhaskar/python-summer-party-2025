# 📝 Day 1: WhatsApp Group Size Engagement Analysis
Company: WhatsApp ◆ Difficulty: Easy

---

## 📘 Challenge Context

You are a Product Analyst on the WhatsApp team investigating group messaging dynamics.  
Your team wants to understand how large groups are being used and their messaging patterns.  
You'll leverage data to uncover insights about group participation and communication behaviors.

## ❓ Challenge Questions

1. **What is the maximum number of participants among WhatsApp groups that were created in October 2024?**  
   → This helps understand the largest group size created during that time.

2. **What is the average number of participants in WhatsApp groups created in October 2024?**  
   → This gives a sense of typical group size.

3. **For WhatsApp groups with more than 50 participants created in October 2024, what is the average number of messages sent?**  
   → This reveals engagement levels in large groups.

---

## 🧠 What I Learned

- Using `pd.to_datetime()` to convert date columns for easier filtering.
- Extracting date parts with `.dt.month` and `.dt.year`.
- Filtering rows with conditions instead of groupby or regex.
- Applying `.max()` and `.mean()` on filtered DataFrames.
- Keeping logic clean and readable with method chaining.

---

## 📊 Key Takeaways

- **Group size trends** can indicate how users form communities.
- **Participation averages** help benchmark typical behavior.
- **Messaging activity in large groups** shows where high engagement happens.

---

## 🌟 Reflections

I started off trying regex and groupby, but learned that simple datetime filtering with `.dt` is more efficient and readable. Loved the real-world angle of the challenge — it made the task more meaningful and fun.

Day 1: ✅ Complete. Ready for the next one!
