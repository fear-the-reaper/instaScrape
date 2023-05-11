from psycopg2 import pool, Error
import os


def createDbPool():
    try:
        print("Connecting to database")
        host=os.environ.get("DB_HOST")
        database=os.environ.get("DATABASE")
        user=os.environ.get("DB_USER")
        password=os.environ.get("DB_PASSWORD")
        port=os.environ.get("DB_PORT")
        credentials = dict(host=host, database=database, user=user, password=password, port=port)
        db_pool = pool.ThreadedConnectionPool(minconn=1, maxconn=10, **credentials)
        print(f"DB connected successfully. Credentails={credentials}")
        return db_pool
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None



def insert_db(conn, query, value):
    try:
        if conn:
            ps_cursor = conn.cursor()
            ps_cursor.execute(query, value)
            conn.commit()
            ps_cursor.close()
            return True
    except (Exception, Error) as error:
        print(f"Could not execute insert query error {error}")
        return False