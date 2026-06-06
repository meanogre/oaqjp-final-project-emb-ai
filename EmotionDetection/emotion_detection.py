import requests

def emotion_detector(text_to_analyze):
    url =  'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    obj = { "raw_document": { "text": text_to_analyze} }
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json=obj, headers=headers)
    rslt = response.json()['emotionPredictions'][0]['emotion']
    return rslt
    # return response.text
