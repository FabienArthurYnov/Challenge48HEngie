from reader import Reader
from plots import *
from writer import Writer
from agent import ask_agent

reader = Reader('./ressources/input/filtered_tweets_engie.csv')
messages = reader.load_messages()
reader.close()


all_length = []
all_datetime = []
# word_occurence = {"engie": 0, "delai": 0, "panne": 0, "urgence": 0, "scandale": 0}
for message in messages:
    all_length.append(message.length)
    # all_datetime.append(message.created_at)
    # word_occurence["engie"] += 1 if message.engieMention else 0
    # word_occurence["delai"] += 1 if message.delaiMention else 0
    # word_occurence["panne"] += 1 if message.panneMention else 0
    # word_occurence["urgence"] += 1 if message.urgenceMention else 0
    # word_occurence["scandale"] += 1 if message.scandaleMention else 0


length_msg_frequency_graph(all_length)
msg_per_weekday([dt.weekday()+1 for dt in all_datetime])
msg_per_date([dt.date() for dt in all_datetime])
# word_occurence_graph(word_occurence)
writer = Writer("./ressources/generated/full_cleaned_msg.csv")
writer.write_from_array_obj(messages, 'ISO-8859-1')

# ask_agent(messages)

# make a graph with all key words apparitions
readerResponse = Reader('./ressources/generated/response.csv')
answers = readerResponse.load_answers()
readerResponse.close()
all_words = []
for answer in answers:
    for word in answer.key_words:
        all_words.append(word)


word_count = dict(Counter(all_words))
sorted_word_count = dict(sorted(word_count.items(), key=lambda item: item[1], reverse=True))

word_occurence_graph(sorted_word_count)
word_cloud(sorted_word_count)

