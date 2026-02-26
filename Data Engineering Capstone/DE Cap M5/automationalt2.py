# Import libraries required for connecting to mysql
import mysql.connector

# Import libraries required for connecting to PostgreSql
import psycopg2


# ---------------------------------------------------------
# Task 1 - Get last rowid from PostgreSQL data warehouse
# ---------------------------------------------------------
def get_last_rowid():
    conn = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="9mVBaynFELqtrbUXBFfjljEs",
        host="172.21.28.152",
        port="5432"
    )

    cursor = conn.cursor()
    cursor.execute("SELECT COALESCE(MAX(rowid), 0) FROM sales_data;")
    last_rowid = cursor.fetchone()[0]

    conn.close()
    return last_rowid


last_row_id = get_last_rowid()
print("Last row id on production datawarehouse = ", last_row_id)


# ---------------------------------------------------------
# Task 2 - Get latest records from MySQL (incremental load)
# ---------------------------------------------------------
def get_latest_records(rowid):
    conn = mysql.connector.connect(
        user="root",
        password="tw6GeSHIRDtbkzjwL7cZ2mPT",
        host="172.21.235.64",
        database="sales"
    )

    cursor = conn.cursor()
    SQL = """
        SELECT rowid, product_id, customer_id, price, quantity, timestamp
        FROM sales_data
        WHERE rowid > %s
    """
    cursor.execute(SQL, (rowid,))
    records = cursor.fetchall()

    conn.close()
    return records


new_records = get_latest_records(last_row_id)
print("New rows on staging datawarehouse = ", len(new_records))


# ---------------------------------------------------------
# Task 3 - Insert new records into PostgreSQL warehouse
# ---------------------------------------------------------
def insert_records(records):
    conn = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="9mVBaynFELqtrbUXBFfjljEs",
        host="172.21.28.152",
        port="5432"
    )

    cursor = conn.cursor()

    SQL = """
        INSERT INTO sales_data (rowid, product_id, customer_id, price, quantity, "timestamp")
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    for row in records:
        cursor.execute(SQL, row)

    conn.commit()
    conn.close()


insert_records(new_records)
print("New rows inserted into production datawarehouse = ", len(new_records))


# ---------------------------------------------------------
# End of program
# ---------------------------------------------------------
# # Connector
# python3.11 -m pip install mysql-connector-python
