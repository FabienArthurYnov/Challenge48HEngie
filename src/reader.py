import pandas as pd
from Message import Message

class Reader:
    def __init__(self, file_name):
        """
        Initializes the Reader class with a file name and opens the file.
        """
        self.file_name = file_name
        try:
            self.file = open(file_name, 'r')
        except FileNotFoundError:
            print(f"Error: File '{file_name}' not found.")
            self.file = None

    def load_messages(self):
        """
        Return all messages objects from the csv.
        """
        column_names = ['id', 'screen_name', 'name', 'created_at', 'full_text']
        df = pd.read_csv(self.file_name, sep=';', encoding="ISO-8859-1", on_bad_lines="warn", names=column_names, header=0)

        messages = [
            Message(
                msg_id=row['id'],
                screen_name=row['screen_name'],
                name=row['name'],
                created_at=row['created_at'],
                full_text=row['full_text']
            )
            for _, row in df.iterrows()
        ]
        return messages

    def read_all(self):
        """
        Reads the entire content of the file.
        """
        if self.file:
            return self.file.read()
        return None
    
    def read_lines(self):
        """
        Reads the file line by line and returns a list of lines.
        """
        if self.file:
            return self.file.readlines()
        return None
    
    def close(self):
        """
        Closes the file.
        """
        if self.file:
            self.file.close()
            self.file = None