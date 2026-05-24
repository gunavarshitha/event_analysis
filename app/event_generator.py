import random
import uuid
import time
from datetime import datetime
import psycopg2

conn = psycopg2.connect(host="db", database="eventsdb", user="postgres", password="postgres")
cursor = conn.cursor()

users = ["user_101","user_102","user_103"]
pages = ["/home","/products","/cart","/checkout"]
products = ["Laptop","Phone","Keyboard"]

def generate_event():
    event_type = random.choice(["page_view","purchase","error"])
    event = {
        "event_id": str(uuid.uuid4()),
        "timestamp": datetime.now(),
        "user_id": random.choice(users),
        "event_type": event_type,
        "page": None,
        "product": None,
        "price": None,
        "error_code": None,
        "message": None
    }

    if event_type == "page_view":
        event["page"] = random.choice(pages)
    elif event_type == "purchase":
        event["product"] = random.choice(products)
        event["price"] = round(random.uniform(100, 2000), 2)
    else:
        event["error_code"] = random.choice([400,401,404,500])
        event["message"] = random.choice(["Unauthorized","Page Not Found","Internal Server Error"])

    return event

for _ in range(100):
    e = generate_event()
    cursor.execute("""
    INSERT INTO events(event_id,timestamp,user_id,event_type,page,product,price,error_code,message)
    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
    """, (
        e["event_id"], e["timestamp"], e["user_id"], e["event_type"],
        e["page"], e["product"], e["price"], e["error_code"], e["message"]
    ))
    conn.commit()
    print("Saved:", e)
    time.sleep(1)

cursor.close()
conn.close()
