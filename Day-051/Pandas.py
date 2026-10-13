import pandas as pd

events = pd.DataFrame({
    "visitor_id": [        "V01", "V01", "V01",        "V02", "V02",        "V03", "V03", "V03",        "V04", "V04", "V04",        "V05", "V05",        "V06", "V06", "V06", "V06"    ],
    "event_time": [        "2026-09-01 09:00", "2026-09-02 10:00", "2026-09-03 14:00",        "2026-09-01 11:00", "2026-09-04 16:00",        "2026-09-02 08:00", "2026-09-03 12:00", "2026-09-05 15:00",        "2026-09-03 09:00", "2026-09-03 18:00", "2026-09-06 13:00",        "2026-09-04 10:00", "2026-09-07 17:00",        "2026-09-02 07:00", "2026-09-03 11:00",        "2026-09-05 14:00", "2026-09-08 16:00"    ],
    "channel": [        "Social", "Search", "Direct",        "Email", "Search",        "Search", "Social", "Email",        "Social", "Search", "Direct",        "Email", "Direct",        "Social", "Email", "Search", "Direct"    ],
    "event_type": [        "Visit", "Visit", "Purchase",        "Visit", "Purchase",        "Visit", "Visit", "Purchase",        "Visit", "Visit", "Purchase",        "Visit", "Visit",        "Visit", "Visit", "Visit", "Purchase"    ]
})

# 1. Convert event_time to datetime, check duplicates, and sort chronologically per visitor
events['event_time'] = pd.to_datetime(events['event_time'])
events = events.sort_values(by=['visitor_id', 'event_time']).reset_index(drop=True)
duplicates_count = events.duplicated().sum()
print("--- 1. Data Preparation ---")
print(f"Duplicate event records found: {duplicates_count}\n")

# 2. Calculate unique visitors, purchasing visitors, and overall conversion rate
unique_visitors = events['visitor_id'].nunique()
purchasing_visitors = events[events['event_type'] == 'Purchase']['visitor_id'].nunique()
conversion_rate = (purchasing_visitors / unique_visitors) * 100

print("--- 2. Conversion Metrics ---")
print(f"Unique visitors: {unique_visitors}")
print(f"Purchasing visitors: {purchasing_visitors}")
print(f"Overall conversion rate: {conversion_rate:.2f}%\n")

# Identify purchasers and their journeys
purchasers = events[events['visitor_id'].isin(events[events['event_type'] == 'Purchase']['visitor_id'])]

# 3. First-Touch Attribution
first_touch_channels = {}
for vid, group in purchasers.groupby('visitor_id'):
    first_touch_channels[vid] = group.iloc[0]['channel']

first_touch_series = pd.Series(first_touch_channels).value_counts()
print("--- 3. First-Touch Attribution (Purchases per Channel) ---")
print(first_touch_series, "\n")

# 4. Last-Touch Attribution (Last non-purchase channel before conversion)
last_touch_channels = {}
for vid, group in purchasers.groupby('visitor_id'):
    purchase_row = group[group['event_type'] == 'Purchase']
    prior_events = group[group['event_time'] < purchase_row['event_time'].values[0]]
    if not prior_events.empty:
        last_touch_channels[vid] = prior_events.iloc[-1]['channel']

last_touch_series = pd.Series(last_touch_channels).value_counts()
print("--- 4. Last-Touch Attribution (Purchases per Channel) ---")
print(last_touch_series, "\n")