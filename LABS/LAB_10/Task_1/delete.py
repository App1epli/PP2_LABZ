import psycopg2

def delete_contact_by_name(name):
    conn = psycopg2.connect(
        dbname="PhoneBook",
        user="postgres",
        password="alis2007",  
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("DELETE FROM contacts WHERE first_name = %s OR second_name = %s", (name, name))
    conn.commit()
    cur.close()
    conn.close()

def delete_contact_by_phone(phone):
    conn = psycopg2.connect(
        dbname="PhoneBook",
        user="postgres",
        password="alis2007",  
        host="localhost",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("DELETE FROM contacts WHERE phone = %s", (phone,))
    conn.commit()
    cur.close()
    conn.close()


delete_contact_by_name("Ali")
