# 💰 Finance Tracker

A clean and responsive **Flask + SQLAlchemy + Chart.js** web application to manage personal finances.  
Track income and expenses, view summaries, visualize financial data, and manage transactions — all in one elegant dashboard.

---

## 🖼️ Preview

The app provides:
- A **Dashboard** with summaries, filters, and income/expense visualizations  
- A **Transactions Manager** for adding, editing, deleting, and exporting data  
- A **Modern, Responsive UI** with Dark Mode support  
- A **Professional About Page** describing the project and technologies  

---

## 🧩 Features

| Category | Description |
|-----------|--------------|
| 💸 **Transactions** | Add, edit, and delete transactions with type (income/expense), date, and category. |
| 📊 **Dashboard** | View totals for income, expenses, and net balance, with bar & trend charts. |
| 🧮 **Filters** | Filter dashboard data by date range or category for focused analysis. |
| 📈 **Monthly Trend Chart** | Visualize income and expenses over time using Chart.js. |
| 💾 **CSV Export** | Download all transactions as a CSV file with one click. |
| 🌙 **Dark Mode** | Switch between light and dark themes — your choice is remembered. |
| 💅 **Responsive Design** | Works beautifully on desktop, tablet, and mobile screens. |
| 🧠 **Database** | Uses SQLAlchemy ORM with SQLite for simplicity and performance. |
| 🎨 **Custom Theme** | Bootstrap-based layout with additional CSS for branding and polish. |

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
  Action	  Description
- Add Transaction	Fill out the form and submit.
- Edit Transaction	Modify date, amount, type, or category.
- Delete Transaction	Permanently remove an entry with confirmation.
- Export CSV         Download all transaction data as a CSV file.

### Uses Bootstrap 5 for grid layout and responsive utilities.
- Custom style.css ensures cohesive colors, padding, and typography.
- Fully responsive design across phones, tablets, and desktop browsers.
- Includes Dark Mode toggle with persistent theme memory.

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
