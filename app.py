from datetime import date
import csv
from io import StringIO

from flask import Flask, render_template, request, redirect, url_for, make_response
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# ---------- Database config ----------
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///finance.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


# ---------- Models ----------

class Category(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

    transactions = db.relationship("Transaction", back_populates="category", lazy=True)

    def __repr__(self):
        return f"<Category {self.name}>"


class Transaction(db.Model):
    __tablename__ = "transactions"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False, default=date.today)
    description = db.Column(db.String(200), nullable=False)
    amount = db.Column(db.Float, nullable=False)  # + income, - expense
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"), nullable=False)

    category = db.relationship("Category", back_populates="transactions")

    def __repr__(self):
        return f"<Transaction {self.description} {self.amount}>"


# ---------- Routes ----------

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():
    # For category dropdown
    categories = Category.query.order_by(Category.name.asc()).all()

    # Read filters from query parameters (GET)
    start_date_str = request.args.get("start_date", "").strip()
    end_date_str = request.args.get("end_date", "").strip()
    selected_category_id = request.args.get("category_id", "").strip()

    # Base query
    query = Transaction.query.order_by(Transaction.date.desc())

    # Apply date filters if present
    start_date = None
    end_date = None

    if start_date_str:
        try:
            start_date = date.fromisoformat(start_date_str)
            query = query.filter(Transaction.date >= start_date)
        except ValueError:
            start_date = None  # ignore invalid format

    if end_date_str:
        try:
            end_date = date.fromisoformat(end_date_str)
            query = query.filter(Transaction.date <= end_date)
        except ValueError:
            end_date = None

    # Apply category filter if present
    category_id_int = None
    if selected_category_id:
        try:
            category_id_int = int(selected_category_id)
            query = query.filter(Transaction.category_id == category_id_int)
        except ValueError:
            category_id_int = None

    # Get filtered transactions
    transactions = query.all()

    total_categories = len(categories)
    total_transactions = len(transactions)

    total_income = sum(t.amount for t in transactions if t.amount > 0)
    total_expenses = sum(-t.amount for t in transactions if t.amount < 0)  # expenses stored negative
    net_balance = total_income - total_expenses

    recent_transactions = transactions[:5]  # last 5 of the filtered set

    # ---------- Monthly trend aggregation ----------
    # Group by (year, month)
    monthly = {}
    for t in transactions:
        ym = (t.date.year, t.date.month)
        if ym not in monthly:
            monthly[ym] = {"income": 0.0, "expenses": 0.0}
        if t.amount > 0:
            monthly[ym]["income"] += t.amount
        else:
            monthly[ym]["expenses"] += -t.amount  # store as positive

    # Sort by year, month
    sorted_months = sorted(monthly.keys())

    trend_labels = []
    trend_income = []
    trend_expenses = []

    for year, month in sorted_months:
        # Format label like "Jan 2025"
        label_date = date(year, month, 1)
        trend_labels.append(label_date.strftime("%b %Y"))
        trend_income.append(round(monthly[(year, month)]["income"], 2))
        trend_expenses.append(round(monthly[(year, month)]["expenses"], 2))

    return render_template(
        "dashboard.html",
        categories=categories,
        total_categories=total_categories,
        total_transactions=total_transactions,
        total_income=total_income,
        total_expenses=total_expenses,
        net_balance=net_balance,
        recent_transactions=recent_transactions,
        # filters so the form keeps current values
        start_date_str=start_date_str,
        end_date_str=end_date_str,
        selected_category_id=category_id_int,
        # trend data
        trend_labels=trend_labels,
        trend_income=trend_income,
        trend_expenses=trend_expenses,
    )


@app.route("/transactions", methods=["GET", "POST"])
def transactions():
    categories = Category.query.order_by(Category.name.asc()).all()

    if request.method == "POST":
        # Create new transaction
        date_str = request.form.get("date")
        description = request.form.get("description")
        amount = float(request.form.get("amount") or 0)
        tx_type = request.form.get("type")  # "income" or "expense"
        category_id = int(request.form.get("category_id"))

        if tx_type == "expense" and amount > 0:
            amount = -amount

        tx_date = date.fromisoformat(date_str) if date_str else date.today()

        tx = Transaction(
            date=tx_date,
            description=description,
            amount=amount,
            category_id=category_id,
        )
        db.session.add(tx)
        db.session.commit()

        return redirect(url_for("transactions"))

    all_transactions = Transaction.query.order_by(Transaction.date.desc()).all()

    return render_template(
        "transactions.html",
        categories=categories,
        transactions=all_transactions,
    )


@app.route("/transactions/<int:tx_id>/edit", methods=["GET", "POST"])
def edit_transaction(tx_id):
    tx = Transaction.query.get_or_404(tx_id)
    categories = Category.query.order_by(Category.name.asc()).all()

    if request.method == "POST":
        date_str = request.form.get("date")
        description = request.form.get("description")
        amount = float(request.form.get("amount") or 0)
        tx_type = request.form.get("type")
        category_id = int(request.form.get("category_id"))

        if tx_type == "expense" and amount > 0:
            amount = -amount

        tx.date = date.fromisoformat(date_str) if date_str else tx.date
        tx.description = description
        tx.amount = amount
        tx.category_id = category_id

        db.session.commit()
        return redirect(url_for("transactions"))

    # Figure out whether it’s income or expense for the select
    tx_type = "income" if tx.amount >= 0 else "expense"
    return render_template(
        "edit_transaction.html",
        tx=tx,
        categories=categories,
        tx_type=tx_type,
    )


@app.route("/transactions/<int:tx_id>/delete", methods=["POST"])
def delete_transaction(tx_id):
    tx = Transaction.query.get_or_404(tx_id)
    db.session.delete(tx)
    db.session.commit()
    return redirect(url_for("transactions"))

@app.route("/export/csv")
def export_csv():
    transactions = Transaction.query.order_by(Transaction.date.asc()).all()

    # Create a CSV in memory
    output = StringIO()
    writer = csv.writer(output)

    # Header row
    writer.writerow(["id", "date", "description", "amount", "category"])

    # Data rows
    for tx in transactions:
        writer.writerow([
            tx.id,
            tx.date.isoformat(),
            tx.description,
            f"{tx.amount:.2f}",
            tx.category.name if tx.category else "",
        ])

    # Build Flask response
    csv_data = output.getvalue()
    response = make_response(csv_data)
    response.headers["Content-Disposition"] = "attachment; filename=transactions.csv"
    response.headers["Content-Type"] = "text/csv; charset=utf-8"

    return response


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        if Category.query.count() == 0:
            default_categories = ["Salary", "Food", "Rent", "Utilities", "Entertainment", "Other"]
            for name in default_categories:
                db.session.add(Category(name=name))
            db.session.commit()

    app.run(debug=True)
