import requests
import json

url = 'http://localhost:8000/summarize'

data = {
    'sentence': "La révolution industrielle a été une période de transformation majeure dans l'histoire, marquée par l'avènement de nouvelles technologies et de changements sociaux significatifs. Elle a commencé au XVIIIe siècle en Europe et a conduit à des avancées majeures dans la production, les transports et la vie quotidienne. Les machines à vapeur, l'essor de l'industrie textile et l'utilisation accrue du charbon ont été des éléments clés de cette révolution. Ces changements ont eu un impact profond sur la société, transformant les modes de travail, les villes et les économies."
}

payload = json.dumps(data)

headers = {'Content-Type': 'application/json'}

response = requests.post(url, headers=headers, data=payload)

if response.status_code == 200:
    result = response.json()
    print("Résumé généré :")
    print(result['summary'])
else:
    print("La requête n'a pas abouti :", response.status_code)
    print("Contenu de la réponse :", response.text)
