import psycopg2
from psycopg2.extras import RealDictCursor
import os

conn = psycopg2.connect(
    dbname=os.getenv("POSTGRES_DB", "appdb"),
    user=os.getenv("POSTGRES_USER", "admin"),
    password=os.getenv("POSTGRES_PASSWORD", "secret"),
    host=os.getenv("POSTGRES_HOST", "your-rds-endpoint"),
    port=5432,
    cursor_factory=RealDictCursor
)