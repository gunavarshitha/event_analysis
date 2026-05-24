import psycopg2
import pandas as pd
import matplotlib.pyplot as plt

# Database Connection
conn = psycopg2.connect(
    host="db",
    database="eventsdb",
    user="postgres",
    password="postgres"
)

# =====================================================
# Chart 1: Number of Events by Event Type
# =====================================================

query1 = """
SELECT event_type, COUNT(*) AS total
FROM events
GROUP BY event_type
ORDER BY total DESC;
"""

df1 = pd.read_sql(query1, conn)

plt.figure(figsize=(8, 5))
plt.bar(df1["event_type"], df1["total"])
plt.title("Number of Events by Event Type")
plt.xlabel("Event Type")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("/app/charts/event_types.png")
plt.close()

print("Generated: event_types.png")

# =====================================================
# Chart 2: Total Events per User
# =====================================================

query2 = """
SELECT user_id, COUNT(*) AS total_events
FROM events
GROUP BY user_id
ORDER BY total_events DESC;
"""

df2 = pd.read_sql(query2, conn)

plt.figure(figsize=(8, 5))
plt.bar(df2["user_id"], df2["total_events"])
plt.title("Total Events Per User")
plt.xlabel("User")
plt.ylabel("Number of Events")
plt.tight_layout()
plt.savefig("/app/charts/user_events.png")
plt.close()

print("Generated: user_events.png")

# =====================================================
# Chart 3: Error Event Rate
# =====================================================

query3 = """
SELECT
    COUNT(*) AS total_events,
    SUM(
        CASE
            WHEN event_type = 'error'
            THEN 1
            ELSE 0
        END
    ) AS error_events
FROM events;
"""

df3 = pd.read_sql(query3, conn)

total_events = int(df3["total_events"][0])
error_events = int(df3["error_events"][0])

error_rate = round(
    (error_events / total_events) * 100,
    2
)

non_error_rate = round(
    100 - error_rate,
    2
)

plt.figure(figsize=(6, 6))
plt.pie(
    [error_rate, non_error_rate],
    labels=[
        f"Error ({error_rate}%)",
        f"Non-Error ({non_error_rate}%)"
    ],
    autopct="%1.1f%%"
)

plt.title("Error Event Rate")
plt.tight_layout()
plt.savefig("/app/charts/error_rate.png")
plt.close()

print("Generated: error_rate.png")

# =====================================================
# Close Connection
# =====================================================

conn.close()

print("\nAll charts generated successfully.")