# 🧼 Simple Data Cleaning Script

## 📌 Executive Summary

This project contains a straightforward Python script for data cleaning. The script performs the following tasks:

- Loads a raw dataset from a CSV file
- Removes duplicate columns and rows
- Fills or flags missing values
- Standardizes inconsistent date formats
- Exports a cleaned version of the dataset to a specified location

To ensure usability by others, the code is **fully commented** and logically structured for easy adaptation.

---

## 💼 Business Impact

Dirty data prevents accurate, reliable, and complete reporting. If data quality issues are not addressed early (as far upstream as possible), they:
- Shift the burden to analysts and end users
- Delay reporting and decision-making
- Risk generating inaccurate insights
- Lead to duplicated effort and inefficiencies when cleaning is repeated later in the pipeline

This script helps eliminate these pain points by creating a **repeatable and automated cleaning process**.

---

## ⚙️ Methodology

The script follows a clean and modular process:
1. **Import Required Libraries** – `pandas`, `os`, `datetime`, and `dateutil`
2. **Load Raw Data** – Uses `pandas.read_csv()`
3. **Clean the Data**:
   - Remove duplicate rows and/or columns
   - Standardize and parse mixed-format date fields
   - Fill or flag missing values
4. **Export the Cleaned File** – Saves the output to a user-defined location with confirmation

---

## 🛠️ Skills Demonstrated

- Python
  - `pandas` for data manipulation
  - `datetime` and `dateutil` for parsing and formatting date values
  - `os` for file path handling and saving confirmation
- Data cleaning best practices
- Reusable, readable code design with comments

---

## ✅ Results & Business Recommendation

By automating early-stage data cleaning, this script:
- Reduces manual effort and rework
- Speeds up the time from raw data to actionable insights
- Helps ensure consistency and trust in downstream reporting

> 📈 **Recommendation:** Integrate this script into your data pipeline to address common issues before the data reaches reporting or analysis stages.

---

## 🖼️ Screenshot

![Screenshot 2025-07-07 at 11 46 38 AM](https://github.com/user-attachments/assets/7baa85cd-a99b-4775-8348-2fead848c9fe)




