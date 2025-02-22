# SQL INJECTION, POSTGRESQL INJECTION, AND eXecution

# ---------------- Import Libraries ----------------
from psycopg2 import sql
from psycopg2 import pool
import requests
from urllib.parse import urlparse
import re
import os
from bs4 import BeautifulSoup

print("Everything Proggressed ...")
print("--------------------------------")
print("Bismillah Jalan")

ans = input("Please enter for execution: ")

# ---------------- Parsing URL ----------------
parsed_url = urlparse(ans)


# ----- User Input --------------------------------
host = 'localhost'
port = '8000'
database = ''
user = ''
password = ''


# ---------------- Connection ----------------
def create_connection():
    connection = {
        "host": host,
        "port": port,
        "database": database,
        "user": user,
        "password": password
    }
    return connection
# ---------------- Connection Pool ----------------
def create_connection_pool(connection):
    pool = psycopg2.pool.SimpleConnectionPool(1, 5, **connection)  # minconn, maxconn, **kwlist
    return pool

# ---------------- SQL Injection ----------------
print ("Creating SQL Injection ....")
def execute_sql_injection(connection_pool, query, params):
    conn = connection_pool.getconn()
    cursor = conn.cursor()
    try:
        cursor.execute(query, params)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection_pool.putconn(conn)

# ---------------- POSTGRESQL Injection ----------------
print("\n PostgreSQL Injection Progress ....")
def execute_postgresql_injection(connection_pool, query, params):
    conn = connection_pool.getconn()
    cursor = conn.cursor()
    try:
        cursor.execute(query, params)
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except psycopg2.errors.ProgrammingError as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        connection_pool.putconn(conn)
    return

# ---------------- eXecution ----------------
print("\nExecution Progress ....")
def execute_code(code):
    try:
        print(f"Executing: {code}")
        exec(code)
        print("Executed successfully")
        execute_code(f"print('Result: {ans}')")
    except NameError:
        print("NameError: Variable 'ans' is not defined")
    except Exception as e:
        print(f"Error: {e}")
    return

# ---------------- Main Function ----------------
def main():
    connection_pool = create_connection_pool(create_connection())

    if parsed_url.scheme == 'postgresql':
        execute_postgresql_injection(connection_pool, "SELECT * FROM users WHERE username = %s;", (ans,))
    elif parsed_url.scheme == 'http' or parsed_url.scheme == 'https':
        html_content = requests.get(ans).text
        soup = BeautifulSoup(html_content, 'html.parser')
        for link in soup.find_all('a'):
            href = link.get('href')
            if href:
                execute_code(f"print('{href}')")
    else:
        print("Unsupported scheme")

    connection_pool.closeall()
    return

# ---------------- Run Main Function ----------------
main()

print("\n--------------------------------")
print("Selamat Jalan")
print("--------------------------------")
print("Bismillah Jalan")