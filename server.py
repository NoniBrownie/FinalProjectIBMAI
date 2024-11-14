from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector  # Ensure the emotion_detector function is correctly imported

app = Flask(__name__)
@app.route('/') # Route for loading the HTML
def home():
    return render_template('index.html')  # Ensure your 'index.html' is in the templates folder

@app.route('/emotionDetector', methods=['GET']) # Route to process the text sent from the client
def emotion_detector_route():
    text_to_analyze = request.args.get('textToAnalyze')    # Get the 'textToAnalyze' parameter from the URL

    if not text_to_analyze:
        return jsonify({'error': 'No text provided'}), 400

    result = emotion_detector(text_to_analyze)     # Call the 'emotion_detector' function to get the analysis

    dominant_emotion = result.get('dominant_emotion')    # Extract the emotions and the dominant emotion from the result
    emotion_scores = {
        'anger': result.get('anger'),
        'disgust': result.get('disgust'),
        'fear': result.get('fear'),
        'joy': result.get('joy'),
        'sadness': result.get('sadness')
    }
    # Format the response as a message in the required format
    response_message = (f"For the given statement, the system response is "
                        f"'anger': {emotion_scores['anger']}, "
                        f"'disgust': {emotion_scores['disgust']}, "
                        f"'fear': {emotion_scores['fear']}, "
                        f"'joy': {emotion_scores['joy']} "
                        f"and 'sadness': {emotion_scores['sadness']}. "
                        f"The dominant emotion is {dominant_emotion}.")
    return response_message     # Return the response message as plain text

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
