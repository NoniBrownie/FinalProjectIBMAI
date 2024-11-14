"""Flask app for emotion analysis using IBM's Watson API."""

from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    """
    Renders the homepage, which allows the user to input text for emotion analysis.
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_route():
    """
    Receives input text, processes it through the emotion detector,
    and returns the emotion analysis result.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    # Check if text is provided
    if not text_to_analyze:
        return jsonify({'error': 'Invalid text! Please try again!'}), 400

    result = emotion_detector(text_to_analyze)

    # Check if the result contains a valid dominant emotion
    if result.get('dominant_emotion') is None:
        return jsonify({'error': 'Invalid text! Please try again!'}), 400

    return jsonify({'response': result})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
