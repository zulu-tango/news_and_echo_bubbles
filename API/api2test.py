import requests
import json

# URL de votre API en cours d'exécution localement
url = 'http://127.0.0.1:5000/summarize'

# Texte à envoyer pour le résumé
text_to_summarize = "L'intelligence artificielle révolutionne de nombreux domaines. Elle est utilisée dans la santé pour diagnostiquer des maladies, dans les voitures autonomes pour la conduite, et même dans la finance pour prédire les marchés. Cependant, son développement nécessite une attention particulière à l'éthique pour éviter les biais et les conséquences négatives."

# Données à envoyer sous forme de JSON
data = {'text': text_to_summarize}

# Envoi de la requête POST à l'API
response = requests.post(url, json=data)

# Vérification du code de statut de la réponse
if response.status_code == 200:
    # Affichage de la réponse JSON contenant le résumé
    print("Résumé généré :")
    print(json.dumps(response.json(), indent=2))
else:
    print("Erreur :", response.status_code)
