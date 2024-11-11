import joblib  # For loading the model
from django.shortcuts import render

# Load the model at the start
model = joblib.load('detection/ml_models/language_detection_model.pkl')
# Load the CountVectorizer
cv = joblib.load('detection/ml_models/count_vectorizer.pkl')
le = joblib.load('detection/ml_models/label_encoder.pkl')


def detection(request):
    if request.method == 'POST':
        text = request.POST.get('text')
        if text:  # Ensure the input is not empty
            print(f"Input Text: {text}")

            # Preprocess the text using CountVectorizer
            # Convert text to bag-of-words
            text_vectorized = cv.transform([text]).toarray()

            # Make a prediction
            prediction_encoded = model.predict(text_vectorized)

            # Decode the numerical label back to the language name
            prediction = le.inverse_transform(prediction_encoded)[0]
            print(f"Predicted Language: {prediction}")

            # Send the prediction to the template
            return render(request, 'index.html', {'prediction': prediction})

    # Render the form initially
    return render(request, 'index.html')
