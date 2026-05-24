CREATE TABLE IF NOT EXISTS events (
    event_id UUID PRIMARY KEY,
    timestamp TIMESTAMP,
    user_id VARCHAR(50),
    event_type VARCHAR(50),
    page VARCHAR(100),
    product VARCHAR(100),
    price DECIMAL,
    error_code INTEGER,
    message TEXT
);