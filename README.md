# Event Analysis Assignment

## Project Overview

This project simulates web service events, stores them in a PostgreSQL database, performs data analysis, and generates visualizations.

The entire stack runs using Docker Compose.

---

# Architecture

Event Generator (Python)
        ↓
PostgreSQL Database
        ↓
SQL Analysis Queries
        ↓
Visualization Charts (PNG)

---

# Event Types

## 1. Page View Event

Represents a user visiting a page in the web application.

Example fields:

- event_id
- timestamp
- user_id
- page

Reason:

Page views are one of the most common web analytics events and help track user activity.

---

## 2. Purchase Event

Represents a successful purchase.

Example fields:

- event_id
- timestamp
- user_id
- product
- price

Reason:

Purchase events are critical for business analytics and revenue tracking.

---

## 3. Error Event

Represents an application or server error.

Example fields:

- event_id
- timestamp
- user_id
- error_code
- message

Reason:

Error events help monitor application health and reliability.

---

# Why PostgreSQL?

PostgreSQL was selected because:

- Structured relational storage
- Strong SQL support
- Easy aggregation and reporting
- Industry-standard database
- Integrates well with Docker Compose

---

# Database Schema

Table: events

| Column | Type |
|----------|----------|
| event_id | UUID |
| timestamp | TIMESTAMP |
| user_id | VARCHAR(50) |
| event_type | VARCHAR(50) |
| page | VARCHAR(100) |
| product | VARCHAR(100) |
| price | DECIMAL |
| error_code | INTEGER |
| message | TEXT |

Events are stored as separate fields instead of storing the entire JSON object.

---

# Analysis Queries

## Query 1: Number of Events by Type

```sql
SELECT event_type, COUNT(*)
FROM events
GROUP BY event_type;
```

Purpose:

Shows distribution of generated events.

---

## Query 2: Total Events per User

```sql
SELECT user_id, COUNT(*)
FROM events
GROUP BY user_id;
```

Purpose:

Shows user activity levels.

---

## Query 3: Error Event Rate

```sql
SELECT
ROUND(
100.0 * SUM(
CASE
WHEN event_type='error'
THEN 1
ELSE 0
END
)/COUNT(*),
2
)
AS error_rate
FROM events;
```

Purpose:

Measures application reliability.

---

# Visualizations

The following charts are automatically generated:

1. event_types.png
2. user_events.png
3. error_rate.png

Generated inside:

charts/

---

# Project Structure

event-analysis-assignment

├── app
│   ├── event_generator.py
│   ├── analysis.py
│   ├── visualize.py
│   ├── requirements.txt
│
├── charts
│   ├── event_types.png
│   ├── user_events.png
│   └── error_rate.png
│
├── Dockerfile
├── docker-compose.yml
├── init.sql
└── README.md

---

# How To Run

Build:

```bash
docker compose build
```

Run:

```bash
docker compose up
```

The workflow is:

1. PostgreSQL starts
2. Database table is created
3. Events are generated automatically
4. Events are saved to PostgreSQL
5. Analysis queries are executed
6. Visualization charts are generated

---

# Results

Example generated results:

Total Events: 100

Event Distribution:

- page_view
- purchase
- error

Visualizations are saved as image files in the charts directory.

---

# Technologies Used

- Python 3.11
- PostgreSQL 16
- Docker
- Docker Compose
- Pandas
- Matplotlib
- Psycopg2