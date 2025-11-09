# 💰 Finance Tracker

A clean and responsive **Flask + SQLAlchemy + Chart.js** web application to manage personal finances.  
Track income and expenses, view summaries, visualize financial data, and manage transactions — all in one elegant dashboard.

---

## 🖼️ Preview

The app provides:
- A **Dashboard** with summaries and income/expense visualizations  
- A **Transactions Manager** for adding, editing, and deleting entries  
- A **Modern, Responsive UI** built with Bootstrap 5 and custom CSS  
- A **Professional About Page** describing the project purpose and technologies  

---

## 🧩 Features

| Category | Description |
|-----------|--------------|
| 💸 **Transactions** | Add, edit, and delete transactions with type (income/expense), date, and category. |
| 📊 **Dashboard** | View totals for income, expenses, net balance, and a visual Chart.js bar chart comparison. |
| 📁 **Categories** | Predefined categories (Salary, Food, Rent, Utilities, etc.) stored in a relational database. |
| 💅 **Responsive Design** | Works on desktop, tablet, and mobile screens. |
| 🧠 **Database** | Uses SQLAlchemy ORM with SQLite for simplicity. |
| 🎨 **Custom Theme** | Professional Bootstrap-based layout with a custom CSS file for consistent branding. |

---

## 🏗️ Tech Stack

| Layer | Technology |
|--------|-------------|
| **Backend Framework** | Flask (Python 3) |
| **Database** | SQLite (via SQLAlchemy ORM) |
| **Frontend** | HTML5, Jinja2, Bootstrap 5, Chart.js |
| **Styling** | Custom CSS theme (`static/style.css`) |
| **Templating** | Flask’s built-in Jinja2 templates |

---

## 🗂️ Project Structure
```
Finance-Tracker/
│
├── app.py # Main Flask application
├── finance.db # SQLite database (auto-generated)
├── requirements.txt # Dependencies list
│
├── static/
│ └── style.css # Custom theme styles
│
└── templates/
├── base.html # Common layout + navbar + footer
├── index.html # Home page
├── dashboard.html # Dashboard with chart + metrics
├── transactions.html # Add / view / delete / edit transactions
├── edit_transaction.html # Edit transaction form
└── about.html # About project information
```
### Install dependencies
- pip install -r requirements.txt

### Run the Flask app
- python app.py


### Then open your browser and visit:
- http://127.0.0.1:5000/

### Default Categories
The app auto-generates categories on first launch:

- Category	Example Use
- Salary	Monthly income
- Food	Groceries, dining
- Rent	Apartment rent
- Utilities	Internet, electricity, water
- Entertainment	Movies, games, streaming
- Other	Miscellaneous

### Dashboard Overview
- Total Income — sum of all positive transactions
- Total Expenses — sum of all negative transactions (absolute values)
- Net Balance — difference between income and expenses
- Recent Transactions — last 5 entries displayed for quick review
- Chart.js Bar Graph — visual comparison of income vs expenses

### CRUD Functionality
#### Action	Description
- ➕ Add Transaction	Fill out the form and submit.
- ✏️ Edit Transaction	Modify date, amount, type, or category.
- 🗑 Delete Transaction	Permanently remove an entry with confirmation.
- 🎨 Styling & Responsiveness

### Uses Bootstrap 5 for grid layout and responsive utilities.
- Custom style.css ensures cohesive colors, padding, and typography.
- Fully responsive design across phones, tablets, and desktop browsers.

## 🔒 Database Schema

### 🗂️ Category Table

| Column | Type | Description |
|:--------|:------|:-------------|
| **id** | Integer (Primary Key) | Unique category ID |
| **name** | String | Category name |

---

### 💸 Transaction Table

| Column | Type | Description |
|:--------|:------|:-------------|
| **id** | Integer (Primary Key) | Unique transaction ID |
| **date** | Date | Date of transaction |
| **description** | String | Description of transaction |
| **amount** | Float | Positive for income, negative for expense |
| **category_id** | ForeignKey | Links to the related category |
