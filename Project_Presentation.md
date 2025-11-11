# 🎯 Project Title: Personal Finance Tracker (Web Application)

---

## 🧩 1. Overview

This project is a **web-based personal finance management system** that allows users to **record, view, and analyze** their income and expenses.  
It provides an easy way to **track spending habits**, **categorize transactions**, and **monitor financial trends** over time — all from an intuitive dashboard.

---

## ⚙️ 2. Technologies Used

- **Flask** – the web framework that powers the application.  
- **SQLite** – used as the database to store financial data.  
- **SQLAlchemy** – the ORM (Object Relational Mapper) that connects the Flask app with the database.  
- **HTML Templates (Jinja2)** – for rendering the pages dynamically.  
- **CSV module** – for exporting transaction data.  

---

## 🧱 3. Core Components

There are two main entities in the system:

### 🏷️ Category

- Represents a type of expense or income (like Food, Salary, Rent, etc.).  
- Each category can have multiple transactions linked to it.  

### 💰 Transaction

Each transaction records:

- **Date** – when it occurred  
- **Description** – what it was for  
- **Amount** – positive for income, negative for expense  
- **Category** – which it belongs to  

---

## 💡 4. How It Works (Step-by-Step)

### Step 1: Home Page
The user starts on the main page, which provides navigation to all sections of the app — the **Dashboard**, **Transactions**, and **About** pages.

### Step 2: Adding Transactions
Users can enter new transactions by specifying:

- Date  
- Description  
- Type (Income/Expense)  
- Amount  
- Category  

The system automatically adjusts income and expense values accordingly.

### Step 3: Viewing and Editing Transactions
- All transactions are listed in **reverse chronological order**.  
- Each entry can be **edited** or **deleted** directly from the interface, making it easy to maintain accurate records.

### Step 4: Dashboard Analytics
The dashboard gives a **summary and visualization** of financial data:

- Total income and expenses  
- Net balance (difference between income and expenses)  
- Recent transactions list  
- Monthly trend graph showing how income and expenses change over time  
- Filters to narrow results by date range or category  

### Step 5: Export Feature
The system includes an **Export to CSV** option.  
This lets users download all their transaction data as a spreadsheet for backup or further analysis.

---

## 🔍 5. Logic Behind It

### 🗄️ Data Management
- Transactions are stored in a structured database where each entry links to a category.  
- SQLAlchemy manages all database operations, translating Python objects into SQL queries automatically.

### 🔢 Filtering and Analysis
- The app allows filtering transactions by **date** or **category**.  
- It computes totals for **income**, **expenses**, and **net balance** dynamically.  
- Monthly aggregation groups all transactions by month and year to visualize financial trends.

### 📊 Dynamic Visualization
- The dashboard templates receive computed data (like totals and charts) from Flask.  
- The data is displayed interactively using HTML and optional charting libraries.

---

## 🧭 6. Navigation and User Flow

| Section | Purpose |
|----------|----------|
| **Home** | Entry point and overview |
| **Dashboard** | Visual summary and analytics |
| **Transactions** | Add, edit, or delete records |
| **Export** | Download data in CSV format |
| **About** | Information about the app |

---

## 🛡️ 7. Additional Features

- Automatically creates **default categories** on first run (like Salary, Food, Rent, etc.).  
- Ensures **consistent data validation** (e.g., expenses are stored as negative values).  
- Uses a **simple and clean web interface** suitable for personal or small-scale use.

---

## 🌟 8. Conclusion

This project demonstrates how a **Flask application** can combine:

- Database management  
- Dynamic data visualization  
- User-friendly interfaces  

to build a **complete finance management solution**.

It’s a great example of integrating **backend logic** with **frontend presentation** to deliver meaningful insights into personal financial behavior.
