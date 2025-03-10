import os
from mistralai import Mistral
from datetime import datetime
import json
import sys
from reader import Reader
# Ensure the standard output uses ISO-8859-1 encoding
sys.stdout.reconfigure(encoding='ISO-8859-1')

reader = Reader('filtered_tweets_engie.csv')
messages = reader.load_messages()
reader.close()
def ask_agent(messages) :
    for message in messages :
        name = message.name
        content = message.full_text
        creates_at = message.creates_at

        now = datetime.now().astimezone()

        formatted_date = now.strftime('%Y-%m-%d %H:%M:%S %z')

        # Add the variable "MISTRAL_API_KEY" to your system environment variable with this value enviBHq5z75SvzYYlNjtDQm4HK4tKvTINjJG
        api_key = os.environ["MISTRAL_API_KEY"]

        client = Mistral(api_key=api_key)

        chat_response = client.agents.complete(
            agent_id= "ag:96b775aa:20250310:chall48h:07bbfff0",
            messages=[
                {
                    "role": "user",
                    "name" : "Guillaume Tournier",
                    "creation-date": "2023-11-16 16:13:18 +01:00",
                    "content": f"Auteur : {name}, Date de création : {creates_at}, Date Actuelle {formatted_date}, Contenu : {content}",
                },
            ],
        )

        a = chat_response.choices[0].message.content.split('{')
        b = a[1].split('}')
        jsonOutput = '{'f"{b[0]}"'}'
        print(jsonOutput)


        #convert string to  object
        json_object = json.loads(jsonOutput)
        print(json_object)

        output = [
            {
                "delai":"temps ecoulés depuis la date de creation du tweet",
                "mot-clés" : [],
                "gravité": "int",
                "classification" : "string",
                "categorie": "string",
            },
        ],