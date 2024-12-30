# import streamlit as st
# import pandas as pd
# from datetime import datetime
# import os

# # Define the file path to save transaction data
# FILE_PATH = 'data/transactions.csv'

# # Ensure the data folder exists
# if not os.path.exists('data'):
#     os.makedirs('data')

# # Load transaction data
# import os

# def load_data():
#     # Check if the file exists and is not empty
#     if os.path.exists(FILE_PATH) and os.path.getsize(FILE_PATH) > 0:
#         try:
#             # Try to load the CSV file
#             data = pd.read_csv(FILE_PATH)
#             return data
#         except pd.errors.EmptyDataError:
#             # If the file is empty (no columns), return an empty DataFrame with column names
#             return pd.DataFrame(columns=["Date", "Transaction Type", "Amount", "Mode", "Description"])
#     else:
#         # If the file doesn't exist or is empty, create an empty DataFrame with column names
#         return pd.DataFrame(columns=["Date", "Transaction Type", "Amount", "Mode", "Description"])

# # Save transaction data to CSV
# def save_data(data):
#     data.to_csv(FILE_PATH, index=False)

# # Display balance and total spending summary
# def display_balance_and_spending(data):
#     # Cash and online balance
#     cash_in_hand = data[data['Mode'] == 'Cash']['Amount'].sum()
#     online_balance = data[data['Mode'] == 'Online']['Amount'].sum()
#     total_balance = cash_in_hand + online_balance
    
#     # Deposited amounts
#     deposited_cash = data[(data['Mode'] == 'Cash') & (data['Transaction Type'] == 'IN')]['Amount'].sum()
#     deposited_online = data[(data['Mode'] == 'Online') & (data['Transaction Type'] == 'IN')]['Amount'].sum()
    
#     # Total spending (OUT transactions)
#     total_spending = data[data['Transaction Type'] == 'OUT']['Amount'].sum()

#     st.header("Balance and Spending Summary")
#     st.write(f"**Cash in Hand:** ₹{cash_in_hand}")
#     st.write(f"**Online Balance:** ₹{online_balance}")
#     st.write(f"**Total Balance:** ₹{total_balance}")
#     st.write(f"**Deposited Cash:** ₹{deposited_cash}")
#     st.write(f"**Deposited Online Money:** ₹{deposited_online}")
#     st.write(f"**Total Spending:** ₹{total_spending}")

# # Main app layout
# st.title("Transaction Manager")

# # Load existing data
# data = load_data()

# # Display balance and total spending on top
# display_balance_and_spending(data)

# # Transaction input section
# transaction_type = st.radio("Select Transaction Type", ("IN", "OUT"))

# # Define inputs for IN and OUT
# if transaction_type == "IN":
#     amount = st.number_input("Enter Amount to Deposit", min_value=0)
#     mode = st.selectbox("Select Mode", ("Cash", "Online"))
#     description = st.text_area("Add Description", "")
#     if st.button("Add Transaction"):
#         if amount > 0:
#             new_entry = pd.DataFrame([{
#                 "Date": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
#                 "Transaction Type": "IN",
#                 "Amount": amount,
#                 "Mode": mode,
#                 "Description": description
#             }])
#             # Append the new entry to the existing data and save
#             data = pd.concat([data, new_entry], ignore_index=True)
#             save_data(data)
#             st.success(f"Deposited ₹{amount} as {mode}.")
#         else:
#             st.error("Please enter a valid amount.")

# elif transaction_type == "OUT":
#     amount = st.number_input("Enter Amount to Deduct", min_value=0)
#     mode = st.selectbox("Select Mode", ("Cash", "Online"))
#     description = st.text_area("Add Description", "")
#     if st.button("Deduct Transaction"):
#         if amount > 0:
#             new_entry = pd.DataFrame([{
#                 "Date": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
#                 "Transaction Type": "OUT",
#                 "Amount": -amount,
#                 "Mode": mode,
#                 "Description": description
#             }])
#             # Append the new entry to the existing data and save
#             data = pd.concat([data, new_entry], ignore_index=True)
#             save_data(data)
#             st.success(f"Deducted ₹{amount} from {mode}.")
#         else:
#             st.error("Please enter a valid amount.")

# # Display transaction history
# st.header("Transaction History")
# if not data.empty:
#     data['Date'] = pd.to_datetime(data['Date'])
#     st.dataframe(data.style.applymap(
#         lambda x: 'color: green' if x == 'IN' else 'color: red', subset=['Transaction Type']
#     ).applymap(
#         lambda x: 'color: green' if 'IN' in str(x) else 'color: red', subset=['Mode']
#     ))
import os
import pandas as pd
import streamlit as st
from datetime import datetime

# Define the file path to save transaction data
FILE_PATH = 'data/transactions.csv'

# Load transaction data
def load_data():
    if os.path.exists(FILE_PATH) and os.path.getsize(FILE_PATH) > 0:
        try:
            data = pd.read_csv(FILE_PATH)
            return data
        except pd.errors.EmptyDataError:
            return pd.DataFrame(columns=["Date", "Transaction Type", "Amount", "Mode", "Description"])
    else:
        return pd.DataFrame(columns=["Date", "Transaction Type", "Amount", "Mode", "Description"])

# Save transaction data to CSV
def save_data(data):
    data.to_csv(FILE_PATH, index=False)

# Delete a transaction entry
def delete_entry(data, index):
    return data.drop(index)

# Display balance and total spending summary
def display_balance_and_spending(data):
    cash_in_hand = data[data['Mode'] == 'Cash']['Amount'].sum()
    online_balance = data[data['Mode'] == 'Online']['Amount'].sum()
    total_balance = cash_in_hand + online_balance
    
    deposited_cash = data[(data['Mode'] == 'Cash') & (data['Transaction Type'] == 'IN')]['Amount'].sum()
    deposited_online = data[(data['Mode'] == 'Online') & (data['Transaction Type'] == 'IN')]['Amount'].sum()
    
    total_spending = data[data['Transaction Type'] == 'OUT']['Amount'].sum()

    st.header("Balance and Spending Summary")
    st.write(f"**Cash in Hand:** ₹{cash_in_hand}")
    st.write(f"**Online Balance:** ₹{online_balance}")
    st.write(f"**Total Balance:** ₹{total_balance}")
    st.write(f"**Deposited Cash:** ₹{deposited_cash}")
    st.write(f"**Deposited Online Money:** ₹{deposited_online}")
    st.write(f"**Total Spending:** ₹{total_spending}")

# Main app layout
st.title("Transaction Manager")

# Load existing data
data = load_data()

# Display balance and total spending on top
display_balance_and_spending(data)

# Transaction input section
transaction_type = st.radio("Select Transaction Type", ("IN", "OUT"))

# Define inputs for IN and OUT
if transaction_type == "IN":
    amount = st.number_input("Enter Amount to Deposit", min_value=0)
    mode = st.selectbox("Select Mode", ("Cash", "Online"))
    description = st.text_area("Add Description", "")
    if st.button("Add Transaction"):
        if amount > 0:
            new_entry = pd.DataFrame([{
                "Date": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                "Transaction Type": "IN",
                "Amount": amount,
                "Mode": mode,
                "Description": description
            }])
            # Append the new entry to the existing data and save
            data = pd.concat([data, new_entry], ignore_index=True)
            save_data(data)
            st.success(f"Deposited ₹{amount} as {mode}.")
        else:
            st.error("Please enter a valid amount.")

elif transaction_type == "OUT":
    amount = st.number_input("Enter Amount to Deduct", min_value=0)
    mode = st.selectbox("Select Mode", ("Cash", "Online"))
    description = st.text_area("Add Description", "")
    if st.button("Deduct Transaction"):
        if amount > 0:
            new_entry = pd.DataFrame([{
                "Date": datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                "Transaction Type": "OUT",
                "Amount": -amount,
                "Mode": mode,
                "Description": description
            }])
            # Append the new entry to the existing data and save
            data = pd.concat([data, new_entry], ignore_index=True)
            save_data(data)
            st.success(f"Deducted ₹{amount} from {mode}.")
        else:
            st.error("Please enter a valid amount.")

# Display transaction history with delete option
st.header("Transaction History")
if not data.empty:
    data['Date'] = pd.to_datetime(data['Date'])
    # Display transactions in a table
    data_display = st.dataframe(data)

    # Create a delete button for each row
    delete_index = st.number_input("Enter the row number to delete (0-based index)", min_value=0, max_value=len(data)-1, step=1)
    
    if st.button("Delete Selected Entry"):
        # Ensure the row exists
        if delete_index < len(data):
            data = delete_entry(data, delete_index)
            save_data(data)
            st.success("Transaction deleted successfully!")
        else:
            st.error("Invalid index. Please select a valid row number.")
else:
    st.write("No transactions found.")
