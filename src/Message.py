class Message:
    def __init__(self, msg_id, screen_name, name, created_at, full_text):
        self.id = msg_id
        self.screen_name = screen_name
        self.name = name
        self.created_at = created_at
        self.full_text = full_text

    def __repr__(self):
        return f"Message(id={self.id}, screen_name='{self.screen_name}', name='{self.name}', created_at='{self.created_at}', full_text='{self.full_text[:30]}...')"
