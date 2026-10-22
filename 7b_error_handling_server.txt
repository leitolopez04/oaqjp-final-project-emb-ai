''' Servidor Flask que despliega la aplicación de detección de emociones
    en localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emot_detector():
    ''' Recibe el texto desde la interfaz HTML, ejecuta la detección de
        emociones y devuelve el resultado en el formato pedido por el cliente.
    '''
    # Recuperar el texto a analizar de los argumentos de la solicitud
    text_to_analyze = request.args.get('textToAnalyze')
    # Ejecutar la detección de emociones
    response = emotion_detector(text_to_analyze)

    # Extraer cada emoción y la emoción dominante
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']
    sadness = response['sadness']
    dominant_emotion = response['dominant_emotion']

    # Manejo de errores: si no hay emoción dominante, la entrada fue inválida
    if dominant_emotion is None:
        return "¡Texto inválido! ¡Por favor, inténtalo de nuevo!"

    # Devolver el texto en el formato solicitado
    return (
        f"Para la declaración dada, la respuesta del sistema es "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} y 'sadness': {sadness}. "
        f"La emoción dominante es {dominant_emotion}."
    )


@app.route("/")
def render_index_page():
    ''' Muestra la página principal de la aplicación. '''
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)