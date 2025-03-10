from reader import Reader
import sys

# Ensure the standard output uses ISO-8859-1 encoding
sys.stdout.reconfigure(encoding='ISO-8859-1')

reader = Reader('filtered_tweets_engie.csv')
messages = reader.load_messages()
reader.close()

for message in messages:
    if (not message.engieMention):
        print(message.full_text)