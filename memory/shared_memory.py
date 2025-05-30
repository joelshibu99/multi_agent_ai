import sqlite3
import os
import time

class SharedMemory:
    def __init__(self, db_path='shared_memory.db'):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path, check_same_thread=False)
        self._init_db()

    def _init_db(self):
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                filepath TEXT,
                format TEXT,
                intent TEXT,
                content_excerpt TEXT
            )
        ''')
        self.conn.commit()

    def log_entry(self, data):
        self.conn.execute('''
            INSERT INTO logs (timestamp, filepath, format, intent, content_excerpt)
            VALUES (?, ?, ?, ?, ?)
        ''', (time.strftime('%Y-%m-%d %H:%M:%S'), data.get('filepath'), data.get('format'),
              data.get('intent'), data.get('content_excerpt')))
        self.conn.commit()
