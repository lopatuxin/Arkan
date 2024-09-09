import sqlite3


class VocabularyDatabase:
    def __init__(self, db_name='vocab.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self._create_table()

    def _create_table(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS vocabulary (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word TEXT UNIQUE
        )
        ''')
        self.connection.commit()

    def add_word(self, word):
        try:
            self.cursor.execute('INSERT INTO vocabulary (word) VALUES (?)', (word,))
            self.connection.commit()
        except sqlite3.IntegrityError:
            pass  # Слово уже существует

    def get_word_id(self, word):
        self.cursor.execute('SELECT id FROM vocabulary WHERE word = ?', (word,))
        result = self.cursor.fetchone()
        return result[0] if result else None

    def get_word_by_id(self, word_id):
        self.cursor.execute('SELECT word FROM vocabulary WHERE id = ?', (word_id,))
        result = self.cursor.fetchone()
        return result[0] if result else None

    def close(self):
        self.connection.close()
