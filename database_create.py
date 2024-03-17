import os
from dotenv import load_dotenv
import datetime
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from loger import logging
from models.report_example import CashIncome
from database_init import (
    Base,
    engine
)


load_dotenv()


pg_db_name = os.getenv("POSTGRES_DB")
pg_user = os.getenv("POSTGRES_USER")
pg_pass = os.getenv("POSTGRES_PASSWORD")
pg_host = os.getenv("POSTGRES_HOST")
pg_port = os.getenv("POSTGRES_PORT")


def create_db(db_host, database, db_port, user_name, user_password):
    
    try:
        con = psycopg2.connect(dbname='postgres', port=db_port,
                               user=user_name, host=db_host,
                               password=user_password)
    except Exception as e:
        print(e)
        exit(1)

    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = con.cursor()
    
    try:
        cur.execute(f"DROP DATABASE {database} ;")
    except Exception as e:
        print('DB does not exist, nothing to drop')
        
    cur.execute(f"CREATE DATABASE {database} ;")
    cur.execute(f"GRANT ALL PRIVILEGES ON DATABASE {database} TO {user_name} ;")
    
    return database


if __name__ == "__main__":
    var = create_db(
        db_host=pg_host,
        database="cash",
        db_port=pg_port,
        user_name=pg_user,
        user_password=pg_pass
        )
    
    print(var, "\n")
    print(type(var))

