class PhraseProcessor:
    def __init__(self, vocabulary_db):
        self.vocabulary_db = vocabulary_db

    def process_phrase(self, phrase):
        indices = []
        words = phrase.lower().split()
        for word in words:
            word_id = self.vocabulary_db.get_word_id(word)
            if word_id is None:
                self.vocabulary_db.add_word(word)
                word_id = self.vocabulary_db.get_word_id(word)
            indices.append(word_id)
        return indices

    def decode_vector(self, vector):
        # Примерный метод для декодирования вектора в текст
        words = []
        for index in vector:
            self.vocabulary_db.get_word_by_id(int(index))
            result = self.vocabulary_db.cursor.fetchone()
            if result:
                words.append(result[0])
        return ' '.join(words)
