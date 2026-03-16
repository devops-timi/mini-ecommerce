import psycopg2
from psycopg2.extras import RealDictCursor
import os

DB_HOST = os.getenv("POSTGRES_HOST", "your-rds-endpoint.amazonaws.com")
DB_NAME = os.getenv("POSTGRES_DB", "appdb")
DB_USER = os.getenv("POSTGRES_USER", "admin")
DB_PASS = os.getenv("POSTGRES_PASSWORD", "secret")

conn = psycopg2.connect(
    dbname=DB_NAME,
    user=DB_USER,
    password=DB_PASS,
    host=DB_HOST,
    port=5432,
    cursor_factory=RealDictCursor
)

def record_metric(endpoint):
    with conn.cursor() as cur:
        cur.execute(
            "INSERT INTO api_metrics (endpoint) VALUES (%s)",
            (endpoint,)
        )
        conn.commit()