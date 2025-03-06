import requests
import json

def sentiment_analyzer(text_to_analyse):
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'  # URL of the sentiment analysis service
    myobj = { "raw_document": { "text": text_to_analyse } }  # Create a dictionary with the text to be analyzed
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}  # Set the headers required for the API request
    response = requests.post(url, json = myobj, headers=header)  # Send a POST request to the API with the text and headers
    output = {
        'label': None,
        'score': None
    }
    if response.status_code == 200:
        formatted_response = json.loads(response.text)
        output = {
            'label': formatted_response["documentSentiment"]["label"],
            'score': formatted_response["documentSentiment"]["score"]
        }

    return output  # Return the response text from the API