# Import libraries required for connecting to mysql
import mysql.connector

# Import libraries required for connecting to PostgreSql
import psycopg2

# ---------------------------------------------------------
# GLOBAL CONNECTIONS
# ---------------------------------------------------------

# Connect to MySQL (your real credentials)
mysql_conn = mysql.connector.connect(
    host="172.21.235.64",
    database="sales",
    user="root",
    password="tw6GeSHIRDtbkzjwL7cZ2mPT"
)
mysql_cursor = mysql_conn.cursor()

# Connect to PostgreSQL (your real credentials)
pg_conn = psycopg2.connect(
    host="172.21.28.152",
    database="postgres",
    user="postgres",
    password="9mVBaynFELqtrbUXBFfjljEs",
    port="5432"
)
pg_cursor = pg_conn.cursor()

# ---------------------------------------------------------
# Task 1: Get last rowid from PostgreSQL
# ---------------------------------------------------------

def get_last_rowid():
    pg_cursor.execute("SELECT COALESCE(MAX(rowid), 0) FROM sales_data")
    last_id = pg_cursor.fetchone()[0]
    return last_id

last_row_id = get_last_rowid()
print("Last row id on production datawarehouse = ", last_row_id)

# ---------------------------------------------------------
# Task 2: Get new records from MySQL
# ---------------------------------------------------------
# MySQL DOES NOT have price or timestamp — so extract only existing columns

def get_latest_records(rowid):
    query = """
        SELECT rowid, product_id, customer_id, quantity
        FROM sales_data
        WHERE rowid > %s
    """
    mysql_cursor.execute(query, (rowid,))
    records = mysql_cursor.fetchall()
    return records

new_records = get_latest_records(last_row_id)
print("New rows on staging datawarehouse = ", len(new_records))

# ---------------------------------------------------------
# Task 3: Insert new records into PostgreSQL
# ---------------------------------------------------------
# PostgreSQL WILL auto-fill:
#   price → DEFAULT 0.0
#   timestamp → DEFAULT CURRENT_TIMESTAMP

def insert_records(records):
    insert_sql = """
        INSERT INTO sales_data (rowid, product_id, customer_id, quantity)
        VALUES (%s, %s, %s, %s)
    """
    for row in records:
        pg_cursor.execute(insert_sql, row)
    pg_conn.commit()

insert_records(new_records)
print("New rows inserted into production datawarehouse = ", len(new_records))

# ---------------------------------------------------------
# Disconnect
# ---------------------------------------------------------

mysql_cursor.close()
mysql_conn.close()

pg_cursor.close()
pg_conn.close()

# End of program
