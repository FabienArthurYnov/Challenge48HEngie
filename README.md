# Challenge48HEngie  

### Objectif
Remonté des informations des plaintes SAV clients sur un dashboard PowerBI clair, catégorisant notamment :  
- Le type de plainte  
- La priorité  
- La gravité  

### Méthodologie
Pour le traitement des tweets, nous avons suivi les étapes suivantes :
1. Collecte des tweets et stockage dans un fichier CSV.
2. Prétraitement des données pour nettoyer et structurer les informations.
3. Analyse des tweets pour extraire des informations clés telles que les mentions, les délais, les pannes, les urgences et les scandales.
4. Utilisation d'un agent IA pour classifier les tweets et extraire des mots-clés pertinents.

### KPI Retenus
Les KPI retenus pour ce projet incluent :
- **Type de plainte** : Catégorisation des plaintes en fonction de leur nature.
- **Priorité** : Niveau d'urgence de la plainte.
- **Gravité** : Impact potentiel de la plainte sur le service.
- **Délai** : Temps écoulé depuis la création du tweet.
- **Mots-clés** : Termes récurrents dans les plaintes.

### Analyse de Sentiment
L'analyse de sentiment a été réalisée en utilisant des techniques de traitement du langage naturel pour déterminer le ton général des tweets (positif, négatif, neutre).

### Création des Agents IA
Le processus de création des agents IA inclut :
- **Logique de détection** : Utilisation de règles et de modèles d'apprentissage automatique pour identifier les types de réclamations.
- **Prompts et Fine-tuning** : Ajustement des modèles pour améliorer la précision des classifications.
- **Exemples d'interactions** : 
  - **Utilisateur** : "Auteur : John Doe, Date de création : 2023-10-01, Contenu : Mon service est en panne depuis 3 jours."
  - **Agent** : "Classification : Panne, Priorité : Haute, Catégorie : Service, Mots-clés : [panne, service], Délai : 3 jours."

### Choix Technologiques pour la Visualisation
Pour la visualisation des données, nous avons choisi d'utiliser PowerBI en raison de ses capacités robustes de création de tableaux de bord interactifs. 

### Pour lancer
- Coller le csv dans ressources/input/filtered_tweets_engie.csv
- Sur Windows : exécuter runWin.cmd  
  
- Les graphiques sont chargés dans ressources/img/graph  
- Les nouveaux csv sont chargés dans ressources/generated  

### Stack
- Python
    - Pandas  
    - Matplotlib  
- PowerBI  
  
### Dépendences
`pip install mistralai  `
    
    
__Auteurs__ : Sami HMIDA, Massil BRAIK, Dallas ABEYAGUNAWARDENA, Abdoulaye WANE, Zineb RIDAOUI, Fabien ARTHUR
