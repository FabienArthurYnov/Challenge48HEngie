
class Response:
    def __init__(self, classification , priority,  category , key_words, days_elapsed):
       
        
        self.days_elapsed = days_elapsed
        self.key_words = key_words
        self.classification = classification
        self.priority = priority
        self.category = category
        
    def __repr__(self):
        return f"classification='{self.classification}', priority='{self.priority}',category='{self.category}', key_words ='{self.key_words}', days_elapsed = '{self.days_elapsed}')"

