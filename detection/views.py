import joblib  # For loading the model
from django.shortcuts import render

# Load the model at the start
model = joblib.load('detection/ml_models/language_detection_model.pkl')

def detection(request):
    if request.method == 'POST':
        # Get the text input from the form
        text = request.POST.get('text')
        
        # Preprocess and make a prediction
        prediction = model.predict([text])  # assuming predict returns the language
        
        # Send the prediction to the template
        return render(request, 'index.html', {'prediction': prediction[0]})
    
    return render(request, 'index.html')
