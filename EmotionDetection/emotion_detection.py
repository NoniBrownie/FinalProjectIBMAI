import requests
import json

def emotion_detector(text_to_analyze):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}

    # Make the API request
    response = requests.post(url, headers=headers, json=input_json)

    if response.status_code == 200:
        result = response.json()  # Convert the response into a dictionary
        
        # Extract emotions from the API response
        emotions = result.get("emotionPredictions", [{}])[0].get("emotion", {})

        # Assign the emotion scores
        anger_score = emotions.get("anger", 0)
        disgust_score = emotions.get("disgust", 0)
        fear_score = emotions.get("fear", 0)
        joy_score = emotions.get("joy", 0)
        sadness_score = emotions.get("sadness", 0)

        # Find the dominant emotion (highest score)
        scores = {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score
        }
        dominant_emotion = max(scores, key=scores.get)  # Emotion with the highest score

        # Return the requested format
        return {
            'anger': anger_score,
            'disgust': disgust_score,
            'fear': fear_score,
            'joy': joy_score,
            'sadness': sadness_score,
            'dominant_emotion': dominant_emotion
        }
    else:
        # If the API response has an error, return the error code and message
        return {"error": response.status_code, "message": response.text}
