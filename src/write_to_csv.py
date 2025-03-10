import csv

def write_responses_to_csv(responses, filename):
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # Écrire l'en-tête
        writer.writerow([
            'id', 'screen_name', 'name', 'created_at', 'full_text', 'classification', 'priority',
            'category', 'key_words', 'days_elapsed', 'length', 'engieMention', 'delaiMention',
            'panneMention', 'urgenceMention', 'scandaleMention'
        ])
        # Écrire les données
        for response in responses:
            writer.writerow([
                response.id, response.screen_name, response.name, response.created_at, response.full_text,
                response.classification, response.priority, response.category, response.key_words,
                response.days_elapsed, response.length, response.engieMention, response.delaiMention,
                response.panneMention, response.urgenceMention, response.scandaleMention
            ])
            
            

