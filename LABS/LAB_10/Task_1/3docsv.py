import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(
    host="localhost",
    dbname="PhoneBook",
    user="postgres",
    password=os.getenv("DB_PASSWORD"),
    port=5432
)

cur = conn.cursor()

with open('C:/Users/Admin/Documents/PP_2_labs/LABS/LAB_10/Task_1/data.csv', 'r') as f:
    next(f) 
    cur.copy_from(f, 'contacts', sep=',', columns=('first_name', 'second_name', 'phone'))

conn.commit()
conn.close()