import pandas as pd
import numpy as np
from faker import Faker
import random

# Initialize faker
fake = Faker()

# -------------------------------
# PART 1: GENERATE USERS
# -------------------------------

num_users = 50000
users = []

for i in range(num_users):
    user = {
        "user_id": i + 1,
        "age": random.randint(13, 24),  # Gen-Z users
        "city": random.choice(["Mumbai", "Delhi", "Bangalore", "Pune", "Hyderabad"]),
        "signup_date": fake.date_between(start_date='-1y', end_date='today')
    }
    users.append(user)

users_df = pd.DataFrame(users)

# Save users
users_df.to_csv("users.csv", index=False)

print(f"Users generated: {len(users_df)}")


# -------------------------------
# PART 2: GENERATE TRANSACTIONS
# -------------------------------

transactions = []
txn_id = 1

for user in users:
    user_id = user["user_id"]

    # Assign user behavior type
    user_type = random.choices(
        ["heavy", "medium", "low"],
        weights=[0.2, 0.5, 0.3]
    )[0]

    # Assign number of transactions
    if user_type == "heavy":
        num_txns = random.randint(20, 50)
    elif user_type == "medium":
        num_txns = random.randint(5, 20)
    else:
        num_txns = random.randint(1, 5)

    for _ in range(num_txns):
        txn = {
            "txn_id": txn_id,
            "user_id": user_id,
            "amount": round(random.uniform(50, 2000), 2),
            "txn_date": fake.date_between(
                start_date=user["signup_date"], end_date='today'
            ),
            "txn_type": random.choice(["UPI", "Recharge", "Bill Payment", "P2P"])
        }

        transactions.append(txn)
        txn_id += 1

transactions_df = pd.DataFrame(transactions)

# Save transactions
transactions_df.to_csv("transactions.csv", index=False)

print(f"Transactions generated: {len(transactions_df)}")

# -------------------------------
# PART 3: GENERATE EVENTS
# -------------------------------

events = []
event_id = 1

for user in users:
    user_id = user["user_id"]
    
    # Simulate engagement level
    engagement_type = random.choices(
        ["high", "medium", "low"],
        weights=[0.3, 0.5, 0.2]
    )[0]

    # Number of app opens
    if engagement_type == "high":
        num_events = random.randint(30, 100)
    elif engagement_type == "medium":
        num_events = random.randint(10, 30)
    else:
        num_events = random.randint(1, 10)

    for _ in range(num_events):
        
        event_name = random.choice([
            "app_open",
            "wallet_add",
            "payment_success",
            "cashback_received"
        ])

        event = {
            "event_id": event_id,
            "user_id": user_id,
            "event_name": event_name,
            "event_time": fake.date_between(
                start_date=user["signup_date"], end_date='today'
            )
        }

        events.append(event)
        event_id += 1

events_df = pd.DataFrame(events)

# Save events
events_df.to_csv("events.csv", index=False)

print(f"Events generated: {len(events_df)}")