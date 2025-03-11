class Message:
    def __init__(self, screen_name, name, created_at, full_text):
        self.screen_name = screen_name
        self.name = name
        self.created_at = created_at
        self.full_text = full_text


        self.length = len(full_text)
        
        self.engieMention = ("@ENGIE" in self.full_text) or ("@EDF" in self.full_text)
        self.delaiMention = (" délai " in self.full_text) or (" délais " in self.full_text)
        self.panneMention = (" panne " in self.full_text) or (" pannes " in self.full_text)
        self.urgenceMention = (" urgence " in self.full_text) or (" urgences " in self.full_text)
        self.scandaleMention = (" scandale " in self.full_text) or (" scandales " in self.full_text)

    def __repr__(self):
        return f"Message(id={self.id}, screen_name='{self.screen_name}', name='{self.name}', created_at='{self.created_at}', full_text='{self.full_text[:30]}...')"
