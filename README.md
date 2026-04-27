# Gen-Z Fintech Product Analytics & Growth Strategy

## Problem Statement

Fintech products targeting Gen-Z users often lack structured behavioural segmentation, leading to inefficient targeting, poor retention, and suboptimal monetisation.

This project simulates a real-world fintech scenario and builds an end-to-end product analytics system to:

- Understand user behaviour  
- Identify high-value cohorts  
- Improve retention and engagement  
- Drive data-backed product decisions  

---

## Dataset

- 50,000 simulated Gen-Z users  
- 700,000+ transactions  
- Event-level behavioural data  

Data generated using Python and analysed using SQLite (DB Browser for SQLite).

---

## Approach

### 1. Event-Driven Analytics

Designed event schema similar to product analytics tools (Mixpanel/Amplitude):

- app_open  
- wallet_add  
- payment_success  

This enabled funnel analysis and behavioural tracking.

---

### 2. RFM Segmentation (SQLite + SQL)

Used SQLite with advanced SQL (CTEs, window functions) to classify users into lifecycle cohorts:

- Champions  
- Loyal Users  
- Potential Loyalists  
- At Risk  
- Lost  

---

### 3. Revenue Analysis (Pareto Insight)

Using SQL window functions:

- Identified that top 20% users contribute ~50–65% of total revenue  
- Highlighted strong revenue concentration, critical for retention strategy  

#### SQL Outputs

![Segment Distribution](dashboard/Segment Distribution Analysis (RFM Segmentation Output).png)

![Revenue by Segment](dashboard/Revenue by Segment Analysis.png)

![Top 20 Percent Revenue](dashboard/top_20_percent_revenue_sql.png)

![RFM Segment Distribution](dashboard/rfm_segment_distribution_sql.png)

---

### 4. Dashboard (Tableau-style)

Built an interactive dashboard to visualise:

- Segment distribution  
- Revenue by segment  
- Average revenue per user  
- Pareto (Top 20% revenue contribution)  
- Recency vs Frequency behaviour  

---

## Dashboard Preview

![Main Dashboard](dashboard/dashboard.png)
https://github.com/RitulKumari65/Gen-Z-User-Segmentation-Growth-Analytics-Loyalty-Design/blob/main/dashboard/Screenshot%202026-04-27%20091258.png

---

## Key Insights

### 1. Revenue Concentration

- Top 20% users contribute ~50%+ of total revenue  
- Indicates strong dependency on high-value users  

---

### 2. Champions Drive Revenue

- Champions (~23% users) generate ~47% of revenue  
- Highest average revenue per user  

---

### 3. At Risk = Biggest Opportunity

- Largest segment (~13K users)  
- Low revenue contribution  

This represents a major retention opportunity.

---

### 4. User Behaviour Pattern

- High recency and high frequency users are Champions  
- Low recency users show high churn risk  

---

## Product Recommendations

### Retention Strategy

- Target At Risk users with:
  - Time-limited cashback nudges  
  - Re-engagement notifications  

---

### Gamification (Gen-Z Focus)

- Streak-based rewards  
- Cashback spin wheels  
- Coins and milestone-based incentives  

---

### High-Value User Focus

- VIP perks for Champions  
- Early feature access  
- Personalised offers  

---

## Tech Stack

- SQL (SQLite) – CTEs, Window Functions  
- Python – Pandas, NumPy (data generation)  
- Tableau / Looker Studio – Dashboarding  
- Mixpanel / Amplitude (conceptual) – Event tracking  

---

## Outcome

This project demonstrates how product analytics can:

- Identify revenue-driving users  
- Improve retention strategies  
- Enable data-driven decision making  
- Design growth systems for fintech products  

---

## Author

Ritul Kumari
