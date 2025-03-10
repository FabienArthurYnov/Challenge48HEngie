import os
from mistralai import Mistral

# Add the variable "MISTRAL_API_KEY" to your system environment variable with this value enviBHq5z75SvzYYlNjtDQm4HK4tKvTINjJG
api_key = os.environ["MISTRAL_API_KEY"]

client = Mistral(api_key=api_key)

chat_response = client.agents.complete(
    agent_id= "ag:96b775aa:20250310:chall48h:07bbfff0",
    messages=[
        {
            "role": "user",
            "name" : "Guillaume Tournier",
            "date": "2023-11-16 16:13:18 +01:00",
            "content": "c'est une dinguerie a quel point c'est éteint",
        },
    ],
)
print(chat_response.choices[0].message.content)

