import csv

from Message import Message

class Response(Message):
    def __init__(self, msg_id, screen_name, name, created_at, full_text , classification , priority,  category , key_words, days_elapsed):
        super().__init__(msg_id, screen_name, name,created_at, full_text)
        
        self.days_elapsed = days_elapsed
        self.key_words = key_words
        self.classification = classification
        self.priority = priority
        self.category = category
        
    def __repr__(self):
        return f"Message(id={self.id}, screen_name='{self.screen_name}', name='{self.name}', created_at='{self.created_at}', full_text='{self.full_text[:30]}...', classification='{self.classification}', priority='{self.priority}',category='{self.category}', key_words ='{self.key_words}', days_elapsed = '{self.days_elapsed}')"

