from reader import Reader
import sys

# Ensure the standard output uses UTF-8 encoding
sys.stdout.reconfigure(encoding='utf-8')

reader = Reader('filtered_tweets_engie.csv')
messages = reader.load_messages()
reader.close()

print(messages)