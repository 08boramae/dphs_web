import sqlite3

def init_db():
    conn = sqlite3.connect('dongpyeong-hs.db')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS users (name TEXT, phone_number TEXT, id PRIMARY KEY)')
    cur.execute('CREATE TABLE IF NOT EXISTS codes (phone TEXT UNIQUE, code TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP, status INTEGER DEFAULT 0)')
    # cur.execute('DELETE FROM users')
    # cur.execute('DELETE FROM codes')
    conn.commit()
    conn.close()

def db_query(query):
    conn = sqlite3.connect('dongpyeong-hs.db')
    cur = conn.cursor()
    cur.execute(query)
    result = cur.fetchall()
    conn.commit()
    conn.close()
    return result

def new_user(name, phone_number):
    db_query(f'INSERT INTO users (name, phone_number) VALUES ("{name}", "{phone_number}")')

def is_verified(name, phone_number):
    row = db_query(f'SELECT code, status FROM codes WHERE phone = "{phone_number}"')
    if row:
        existing_code, status = row
        if status:
            print("이미 인증된 번호입니다.")
            return(1)

def new_code(name, phone_number):
    db_query(f'INSERT INTO users (name, phone_number, id) VALUES ("{name}", "{phone_number}", 0)')