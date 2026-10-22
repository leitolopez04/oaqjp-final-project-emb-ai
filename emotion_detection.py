import requests


def emotion_detector(text_to_analyze):
    # URL del servicio de detección de emociones de Watson NLP
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Encabezado con el ID del modelo que se va a usar
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Texto a analizar, en el formato JSON que espera el servicio
    myobj = {"raw_document": {"text": text_to_analyze}}
    # Enviar la solicitud POST y devolver la respuesta como texto
    response = requests.post(url, json=myobj, headers=headers)
    return response.text