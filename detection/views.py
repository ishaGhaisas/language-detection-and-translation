import joblib 
from django.shortcuts import render
import tensorflow as tf

model = joblib.load('detection/ml_models/language_detection_model.pkl')
cv = joblib.load('detection/ml_models/count_vectorizer.pkl')
le = joblib.load('detection/ml_models/label_encoder.pkl')


def detection(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:
            print(f"Input Text: {text}")
            text_vectorized = cv.transform([text]).toarray()

            prediction_encoded = model.predict(text_vectorized)

            prediction = le.inverse_transform(prediction_encoded)[0]
            print(f"Predicted Language: {prediction}")

            return render(request, 'index.html', {'prediction': prediction})

    return render(request, 'index.html')


