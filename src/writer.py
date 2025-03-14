import csv
from datetime import datetime

class Writer:
    def __init__(self, filename):
        self.filename = filename

    def write_from_array_obj(self, array_obj, encode_format = 'ISO-8859-1'):
        """
        Writes an array of objects to the csv
        """
        if not array_obj:
            return

        headers = array_obj[0].__dict__.keys()
        # Open the CSV file in write mode, create a CSV writer
        with open(self.filename, mode='w', newline='', encoding=encode_format) as file:
            writer = csv.DictWriter(file, fieldnames=headers)
            
            # Write the headers to the CSV
            writer.writeheader()
            
            # Write each Message object as a row in the CSV file
            for item in array_obj:
                writer.writerow(item.__dict__)
                
        print("Writing " + self.filename)

