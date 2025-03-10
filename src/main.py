from reader import Reader
from plots import length_msg_frequency_graph
import sys

# Ensure the standard output uses ISO-8859-1 encoding
sys.stdout.reconfigure(encoding='ISO-8859-1')

reader = Reader('filtered_tweets_engie.csv')
messages = reader.load_messages()
reader.close()


all_length = []
for message in messages:
    all_length.append(message.length)

length_msg_frequency_graph(all_length)
