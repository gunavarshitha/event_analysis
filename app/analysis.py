import psycopg2

conn = psycopg2.connect(host="db", database="eventsdb", user="postgres", password="postgres")
cursor = conn.cursor()

print("Event counts")
cursor.execute("SELECT event_type, COUNT(*) FROM events GROUP BY event_type")
print(cursor.fetchall())

print("User counts")
cursor.execute("SELECT user_id, COUNT(*) FROM events GROUP BY user_id")
print(cursor.fetchall())

cursor.close()
conn.close()
