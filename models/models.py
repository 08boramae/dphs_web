import email
import imaplib
import base64
import random
import jwt
import requests
from datetime import datetime, timedelta
from database import handle_database

def continue_verify(phone_number):
    row = handle_database.db_query('SELECT code, timestamp FROM codes WHERE phone = ?', (phone_number))
    now = datetime.now()

    if row:
        existing_code, timestamp = row
        timestamp = datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S')
        if now - timestamp < timedelta(minutes=10): # 10분 이내에 이미 발급된 코드가 있을 경우
            return {'code': "ZHBoc192ZXJpZnlfaGVhZGVy ---DPHS_HEADER>BODY--- " + existing_code}
        else: # 10분 이내에 발급된 코드가 있으나 만료되었을 경우
            handle_database.db_query('DELETE FROM codes WHERE phone = ?', (phone_number))

    code_plaintext = ''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for i in range(100))
    code_encoded = base64.b64encode(code_plaintext.encode('utf-8')).decode('utf-8')
    handle_database.db_query('INSERT INTO codes (phone, code, timestamp, status) VALUES (?, ?, ?, ?)', (phone_number, code_encoded, now.strftime('%Y-%m-%d %H:%M:%S'), 0))
    return jsonify({'code': "ZHBoc192ZXJpZnlfaGVhZGVy ---DPHS_HEADER>BODY--- " + code_encoded})

