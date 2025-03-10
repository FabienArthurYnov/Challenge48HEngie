import os
import time
from mistralai import Mistral
from datetime import datetime
import json
from response import Response
from writer import Writer


repCsv = []
def ask_agent(messages) :
    for message in messages :
        name = message.name
        content = message.full_text
        creates_at = message.created_at

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

        resp = Response(
            days_elapsed = json_object["delai"] ,
            key_words = json_object["mot-cles"],
            classification = json_object["gravite"],
            priority =json_object["classification"],
            category =json_object["categorie"]
        )

        repCsv.append(resp)

        

        print(json_object)

        output = [
            {
                "delai":"temps ecoulés depuis la date de creation du tweet",
                "mot-cles" : [],
                "gravite": "int",
                "classification" : "string",
                "categorie": "string"
            },
        ],
        time.sleep(3)

    w =  Writer("./ressources/generated/response.csv")
    w.write_from_array_obj(repCsv)

