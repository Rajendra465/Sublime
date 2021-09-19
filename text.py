import requests
import json
import sys
url = "https://question-generator.p.rapidapi.com/"
text = sys.argv[1]

querystring = {"text":text}

r = requests.post(
    "https://api.deepai.org/api/summarization",
    data={
        'text': text,
    },
    headers={'api-key': '<key>'}
)
bp = r.json()





headers = {
    'x-rapidapi-key': "<key>",
    'x-rapidapi-host': "question-generator.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

dip = {"ques":response.text.split('?')}
 

bullet_points = []
bpr = [r.json()['output'].split('.')]
dictt = {"key":bpr[0]}


final_dict = {"summary":r.json()['output'], "checkYK": dip['ques'], "points": dictt['key']}
print(json.dumps(final_dict))
