import json
import requests


def emotion_detector(text_to_analyze):
    # URL del servicio de detección de emociones de Watson NLP
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Encabezado con el ID del modelo que se va a usar
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Texto a analizar, en el formato JSON que espera el servicio
    myobj = {"raw_document": {"text": text_to_analyze}}
    # Enviar la solicitud POST
    response = requests.post(url, json=myobj, headers=headers)

    # Manejo de errores: si la entrada está en blanco, el servicio responde con 400
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None,
        }

    # 1. Convertir el texto de la respuesta en un diccionario
    formatted_response = json.loads(response.text)

    # 2. Extraer el diccionario que contiene las emociones y sus puntajes
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']

    # 3. Encontrar la emoción dominante (la de mayor puntaje)
    scores = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
    }
    dominant_emotion = max(scores, key=scores.get)

    # 4. Devolver el formato pedido
    return {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion,
    }