import pandas as pd
import os

# since this dummy data was generated using an LLM, we need to make sure that no event was done by a user before the user was even signed up 

PARENT_DIR = os.path.dirname(os.path.abspath(__file__))

EVENTS_PATH = os.path.join(PARENT_DIR, "events.csv")
USERS_PATH = os.path.join(PARENT_DIR, "users.csv")

events = pd.read_csv(EVENTS_PATH)
users = pd.read_csv(USERS_PATH)

events['timestamp'] = pd.to_datetime(events['timestamp'], format='ISO8601').dt.date
users['signup_date'] = pd.to_datetime(users['signup_date'], format='ISO8601')

join = pd.merge(left=events, right=users, on="user_id", how="left")

print(join.head())

impossible_events = join[join["signup_date"] > join["timestamp"]]

print("Number of impossible events:", len(impossible_events))

if len(impossible_events) > 0:
    print(f"Removing {len(impossible_events)} impossible events ...")
    join[join["signup_date"] < join["timestamp"]][events.columns].to_csv(EVENTS_PATH, index=False)
    print("Update events.csv file")
