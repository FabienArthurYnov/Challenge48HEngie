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