import json

from flask import Flask, request, render_template
import requests
from requests.auth import HTTPBasicAuth

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/dialogflow', methods=['POST'])
def search():
    body = request.get_json()
    query = body["queryResult"]["queryText"]
    url = 'https://b4d1b062b9ba4dd5affb0e4518fab213.asia-east1.gcp.elastic-cloud.com:9243/product/_search'
    json_body = {
        'query': {
            'match': {
                'name': query
            }
        }
    }
    auth = HTTPBasicAuth('elastic', 'zGmTrU0EhUGlsCOHEvyjmD6U')
    results = requests.post(url=url, json=json_body, auth=auth).json()['hits']['hits']
    names = [r['_source']['name'] for r in results]

    return json.dumps({
        "fulfillmentMessages": [
            {
                "text": {
                    "text": [
                        names
                    ]
                }
            }
            # {
            #   "card": {
            #     "title": "Products",
            #     "subtitle": "\n".join(names),
            #     "imageUri": "https://example.com/images/example.png",
            #     "buttons": [
            #       {
            #         "text": "button text",
            #         "postback": "https://example.com/path/for/end-user/to/follow"
            #       }
            #     ]
            #   }
            # }
        ]
    })
