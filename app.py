import streamlit as st
import pandas as pd
from pathlib import Path

st.set_page_config(
    page_title="Expense Tracker Dashboard",
    page_icon="💰",
    layout="wide"
)

st.title("💰 Expense Tracker Dashboard")
st.caption("Manage your income and expenses in one place.")

FILE = Path(__file__).with_name("transactions.csv")

if FILE.exists():
    df = pd.read_csv(FILE)
else:
    df = pd.DataFrame(
        columns=["id", "date", "type", "category", "amount", "description"]
    )

if not df.empty:
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce").fillna(0)
    df["type"] = df["type"].astype(str).str.lower()

income = df.loc[df["type"] == "income", "amount"].sum()
expenses = df.loc[df["type"] == "expense", "amount"].sum()
balance = income - expenses

st.subheader("📊 Financial Overview")

c1, c2, c3 = st.columns(3)
c1.metric("💵 Total Income", f"Rs. {income:,.2f}")
c2.metric("💸 Total Expenses", f"Rs. {expenses:,.2f}")
c3.metric("💰 Net Balance", f"Rs. {balance:,.2f}")

st.divider()

left, right = st.columns(2)

with left:
    st.subheader("📋 Recent Transactions")
    if df.empty:
        st.info("No transactions yet. Add one using your Python Expense Tracker.")
    else:
        st.dataframe(df, use_container_width=True, hide_index=True)

with right:
    st.subheader("📈 Expenses by Category")
    if not df.empty:
        expense_df = df[df["type"] == "expense"]
        if not expense_df.empty:
            category_totals = expense_df.groupby("category")["amount"].sum()
            st.bar_chart(category_totals)
        else:
            st.info("No expenses recorded yet.")
    else:
        st.info("Your category chart will appear here.")

st.caption("Expense Tracker | Built with Python and Streamlit")